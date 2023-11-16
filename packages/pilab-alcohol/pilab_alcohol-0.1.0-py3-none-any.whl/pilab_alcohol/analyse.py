import sys
import json
import numpy as np
import pandas as pd
import nibabel as nib
import seaborn as sns
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from mpl_toolkits.mplot3d import Axes3D
from statannot import add_stat_annotation
from sklearn.mixture import GaussianMixture as GMM
from utils import get_atlas_list, get_corr_atlas_list, to_float64, jsonToPandas


def mean_by_ROI(code, f_path, output_path):

    atlas_list = get_atlas_list('/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Atlas/')
    atlas_list_name = get_corr_atlas_list(atlas_list)

    patient_path = f_path + 'subjects/subj_list.json'
    with open(patient_path, 'r') as read_file:
        patient_list = json.load(read_file)

    metric_name = ['FA', 'MD', 'AD', 'RD', 'noddi_fintra', 'noddi_fextra', 'noddi_fiso',
                   'noddi_odi', 'diamond_wFA', 'diamond_wMD', 'diamond_wRD',
                   'diamond_wAD', 'diamond_frac_ftot',
                   'diamond_frac_csf', 'mf_frac_csf', 'mf_fvf_tot', 'mf_wfvf', 'mf_frac_ftot']

    dataframe = {}
    dataframe['Mean'] = {}
    dataframe['Dev'] = {}

    for patient in tqdm(patient_list):
        if patient not in ['sub06_E1', 'sub67_E1']:

            dataframe['Mean'][patient] = {}
            dataframe['Dev'][patient] = {}

            brain_mask = nib.load(f_path + '/subjects/' + patient + '/masks/' + patient + '_brain_mask_dilated.nii.gz').get_fdata()

            wm_mask = nib.load(f_path + '/subjects/' + patient + '/masks/' + patient + '_wm_mask_FSL_T1.nii.gz').get_fdata()

            for atlas_path in atlas_list_name:

                dataframe['Mean'][patient][str(atlas_path[0])] = {}
                dataframe['Dev'][patient][str(atlas_path[0])] = {}

                atlas_name = str(atlas_path[1])
                new_atlas_name = atlas_name.replace('/', '/' + patient + '_')

                atlas = nib.load(f_path + 'registration/' + patient + '/' + new_atlas_name).get_fdata()

                if(atlas_path[3] == "0" or atlas_path[3] == "2" or atlas_path[3] == "4" or atlas_path[3] == "5" or atlas_path[3] == "6"):
                    mask_zone = atlas * brain_mask
                elif(atlas_path[3] == "1" or atlas_path[3] == "3"):  # WHITE MATTER
                    mask_zone = atlas * wm_mask
                else:
                    print('Not ok again')

                for k, m in enumerate(metric_name):

                    if m in ['FA', 'MD', 'RD', 'AD']:
                        model = 'dti'
                    elif m in ['noddi_fintra', 'noddi_fextra', 'noddi_fiso',
                               'noddi_odi']:
                        model = 'noddi'
                    elif m in ['diamond_wFA', 'diamond_wMD', 'diamond_wRD',
                               'diamond_wAD', 'diamond_frac_ftot',
                               'diamond_frac_csf']:
                        model = 'diamond'
                    else:
                        model = 'mf'

                    metric_map = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/' + model + '/' + patient + '_' + m + '.nii.gz').get_fdata()

                    interm = metric_map * mask_zone

                    mean_ROI = np.mean(interm[interm != 0], where=~np.isnan(interm[interm != 0]))
                    std_ROI = np.std(interm[interm != 0], where=~np.isnan(interm[interm != 0]))

                    dataframe['Mean'][patient][str(atlas_path[0])][m] = mean_ROI
                    dataframe['Dev'][patient][str(atlas_path[0])][m] = std_ROI

    json.dump(dataframe, open(output_path + 'mean_by_ROI.json', 'w'), default=to_float64)


def difference_temps(patient_list, dic_val, output_path):

    dataframe = jsonToPandas(output_path + 'mean_by_ROI.json')

    name_all = [x.replace('_E1', '').replace('_E2', '').replace('_E3', '') for x in patient_list]

    df_temps = {}
    list_temps = []

    for t in list(dataframe.index.unique(1)):
        if t[-2:] not in list_temps:
            list_temps.append(t[-2:])

    list_temps.sort()

    for region_val in list(dataframe.index.unique(2)):
        for metric_val in list(dataframe.index.unique(3)):
            for i in name_all:
                inter_value = []
                for temps in list_temps:
                    try:
                        inter_value.append(
                            dataframe.loc[dic_val, i + '_' + temps, region_val,
                                          metric_val][0])
                    except KeyError:
                        inter_value.append(float('nan'))
                        continue

                df_temps[dic_val, i, region_val, metric_val] = inter_value

    temps_dataframe = pd.DataFrame(df_temps, index=[list_temps]).T
    temps_dataframe = temps_dataframe.rename_axis(
        ['Dic', 'Patient', 'Region', 'Metric'])
    temps_dataframe = temps_dataframe.sort_values(by='Patient', ascending=True)

    temps_dataframe['Diff E2-E1'] = (np.array(temps_dataframe.loc[:, 'E2']) - np.array(temps_dataframe.loc[:, 'E1']))
    temps_dataframe['Diff E3-E1'] = (np.array(temps_dataframe.loc[:, 'E3']) - np.array(temps_dataframe.loc[:, 'E1']))
    temps_dataframe['Diff E3-E2'] = (np.array(temps_dataframe.loc[:, 'E3']) - np.array(temps_dataframe.loc[:, 'E2']))

    temps_dataframe['Change E2-E1 (%)'] = (np.array(temps_dataframe.loc[:, 'E2']) - np.array(temps_dataframe.loc[:, 'E1'])) * 100 / np.array(temps_dataframe.loc[:, 'E1'])
    temps_dataframe['Change E3-E1 (%)'] = (np.array(temps_dataframe.loc[:, 'E3']) - np.array(temps_dataframe.loc[:, 'E1'])) * 100 / np.array(temps_dataframe.loc[:, 'E1'])
    temps_dataframe['Change E3-E2 (%)'] = (np.array(temps_dataframe.loc[:, 'E3']) - np.array(temps_dataframe.loc[:, 'E2'])) * 100 / np.array(temps_dataframe.loc[:, 'E2'])

    return temps_dataframe


def gaussian_clustering(input_data, nb_cluster, output_path):

    X = input_data
    model = GMM(n_components=nb_cluster)
    model.fit(X)
    labels = model.predict(X)

    fig = plt.figure(figsize=(15, 12))
    ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=10, azim=124)
    labs = []
    for i in range(nb_cluster):
        ax.scatter(X[labels == i, 0], X[labels == i, 1], X[labels == i, 2])
        labs = np.append(labs, 'Cluster ' + str(i))

    ax.legend(labels=labs)

    fig.savefig(output_path + "Clusters_3D.pdf")

    return labels


def t_test_analysis(dataframe, patient_list, region, dic, metric, temps_list):

    df_pval = {}
    df_mean = {}

    region_list = list(dataframe.index.unique(2))
    metric_list = list(dataframe.index.unique(3))

    for r in region_list:

        dfr_dataframe = dataframe.xs(r, level=2)

        for m in metric_list:

            dfm_dataframe = dfr_dataframe.xs(m, level=2)

            df_0 = dfm_dataframe[temps_list[0]].to_numpy().flatten()
            df_1 = dfm_dataframe[temps_list[1]].to_numpy().flatten()

            p = ttest_ind(df_0, df_1, nan_policy='omit', equal_var=False)[1]

            df_pval[dic, metric, temps_list] = p

            if (p < 0.05):

                df_mean[dic, metric, temps_list] = np.array(np.mean(df_0), np.mean(df_1))

    df_pvals = pd.DataFrame(df_pval, index=['pval']).T
    df_pvals = df_pvals.rename_axis(
        ['Dic', 'Region', 'Metric'])

    df_means = pd.DataFrame(df_mean, index=[temps_list]).T
    df_means = df_pvals.rename_axis(
        ['Dic', 'Region', 'Metric'])

    return df_pvals, df_means


if __name__ == '__main__':
    code = sys.argv[1]
    f_path = sys.argv[2]
    output_path = sys.argv[3]

    if code == 'Mean_ROI':
        mean_by_ROI(code, f_path, output_path)
