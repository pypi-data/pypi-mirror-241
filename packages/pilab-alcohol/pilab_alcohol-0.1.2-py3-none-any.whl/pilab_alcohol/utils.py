import os
import sys
import pandas as pd
import json
import numpy as np
import nibabel as nib
from binama.utils import center_of_mass

def to_float64(val):
    '''
    Used if *val* is an instance of numpy.float32.
    '''

    return np.float64(val)


def makedir(dir_path):

    if not(os.path.exists(dir_path)):
        try:
            os.makedirs(dir_path)
        except OSError:
            print('Creation of the directory %s failed' % dir_path)
        else:
            print('Successfully created the directory %s ' % dir_path)


def folder_patients(root, patient_list, sub_files):

    atlas_dir = os.path.join(root, 'Atlas')
    makedir(atlas_dir)

    patient_dir = os.path.join(root, 'alcoholic_study', 'registration')
    makedir(patient_dir)

    for i in patient_list:
        out_dir = os.path.join(patient_dir, i + '/')
        makedir(out_dir)

        for j in sub_files:
            out_dir_sub = os.path.join(out_dir, j + '/')
            makedir(out_dir_sub)


# %% Cell 1 - Registration
def get_atlas_list(folder):
    '''
    Creation of a list with all atlases and their path, name, thresholds and indexes.

    Parameters
    ----------
    folder : string
        Path to the atlas file.

    Returns
    -------
    atlas_list : tuple
        Resume of all the information for each atlas needed for the analyses.

    '''

    atlas_list = []

    seuil_cerebellar = 0.2
    seuil_cerebellum = 50
    seuil_xtract = 30
    seuil_harvard = 30
    seuil_lobes = 30
    seuil_cortex = 30
    seuil_CC = 0.9

    for filename in os.listdir(folder):
        if (filename in ['FSL_HCP1065_FA_1mm.nii.gz', '00Average_Brain.nii']):
            continue
        else:
            subfile_name = folder + '/' + filename

            for atlas_name in os.listdir(subfile_name):
                atlas_path = filename + '/' + atlas_name

                if('Cerebellar' in atlas_path):
                    atlas_list.append([atlas_path, seuil_cerebellar, 3])
                elif('Cerebellum' in atlas_path):
                    atlas_list.append([atlas_path, seuil_cerebellum, 4])
                elif('harvardoxford-subcortical' in atlas_path):
                    atlas_list.append([atlas_path, seuil_harvard, 2])
                elif('harvardoxford-cortical' in atlas_path):
                    atlas_list.append([atlas_path, seuil_cortex, 0])
                elif('mni_prob' in atlas_path):
                    atlas_list.append([atlas_path, seuil_lobes, 5])
                elif('xtract_prob' in atlas_path):
                    atlas_list.append([atlas_path, seuil_xtract, 1])

    corpus_callosum = 'CC/corpus_callosum_hand_drawn_smoothed.nii.gz'
    atlas_list.append([corpus_callosum, seuil_CC, 6])
    corpus_callosum_genu = 'CC/corpus_callosum_genu.nii.gz'
    atlas_list.append([corpus_callosum_genu, seuil_CC, 6])
    corpus_callosum_anterior_midbody = 'CC/corpus_callosum_anterior_midbody.nii.gz'
    atlas_list.append([corpus_callosum_anterior_midbody, seuil_CC, 6])
    corpus_callosum_posterior_midbody = 'CC/corpus_callosum_posterior_midbody.nii.gz'
    atlas_list.append([corpus_callosum_posterior_midbody, seuil_CC, 6])
    corpus_callosum_isthmus = 'CC/corpus_callosum_isthmus.nii.gz'
    atlas_list.append([corpus_callosum_isthmus, seuil_CC, 6])
    corpus_callosum_splenium = 'CC/corpus_callosum_splenium.nii.gz'
    atlas_list.append([corpus_callosum_splenium, seuil_CC, 6])

    return atlas_list


def get_corr_atlas_list(atlas_list):
    '''
    Correct the name of the atlases to be used in graphs.

    Parameters
    ----------
    atlas_list : tuple
        Resume of all the information for each atlas needed for the analyses.

    Returns
    -------
    atlas_name : tuples.
        Same list of tuples of atlas list but with an extra component in the tuple corresponding to a corrected name of the atlas.

    '''

    atlas_name = np.array(['altas_corr', 'atlas', 0, 0])

    for i in range(len(atlas_list)):
        name = (atlas_list[i])[0]
        if('xtract' in name):
            name = name.replace('xtract_prob_', '')
        if('harvardoxford' in name):
            name = name.replace('harvardoxford-subcortical_', '')
            name = name.replace('harvardoxford-cortical_', '')
            name = name.replace('prob_', '')
        if('mni_' in name):
            name = name.replace('mni_prob_', '')
        if('cerebellum_mniflirt_prob_' in name):
            name = name.replace('mniflirt_prob_', '')
        if('Cerebellar/' in name):
            name = name.replace('Cerebellar/', '')
        if('Cerebelar' in name):
            name = name.replace('Cerebelar', 'Cerebellar')
        if('Cerebellum/' in name):
            name = name.replace('Cerebellum/', '')
        if('Harvard/' in name):
            name = name.replace('Harvard/', '')
        if('Harvard_cortex/' in name):
            name = name.replace('Harvard_cortex/', '')
        if('Lobes/' in name):
            name = name.replace('Lobes/', '')
        if('XTRACT/' in name):
            name = name.replace('XTRACT/', '')
        if('CC/' in name):
            name = name.replace('CC/', '')
        if('Juxtapositional' in name):
            name = name.replace('(formerly_Supplementary_Motor_Cortex)', '')
        if('cerebellum' in name):
            name = name.replace('cerebellum', 'Cerebellum')
        if('Amygdala' in name):
            name = name.replace(' Amygdala', 'Amygdala')
        if('Thalamus' in name):
            name = name.replace(' Thalamus', 'Thalamus')
        if('Caudate' in name):
            name = name.replace(' Caudate', 'Caudate')
        if('Cerebral' in name):
            name = name.replace(' Cerebral', 'Cerebral')
        if('Hippocampus' in name):
            name = name.replace(' Hippocampus', 'Hippocampus')
        if('Putamen' in name):
            name = name.replace(' Putamen', 'Putamen')
        if('Right' in name):
            name = name.replace('Right', '')
            name = name + ' R'
        if('Left' in name):
            name = name.replace('Left', '')
            name = name + ' L'
        if('_hand_drawn_morpho' in name):
            name = name.replace('_hand_drawn_morpho', '')
        name = name.replace('.nii.gz', '')
        name = name.replace('_', ' ')

        vecteur = np.array([name, (atlas_list[i])[0], (atlas_list[i])[1], (atlas_list[i])[2]])
        atlas_name = np.append(atlas_name, vecteur, axis=0)

    atlas_name = np.reshape(atlas_name, ((len(atlas_list) + 1), 4))
    atlas_name = np.delete(atlas_name, (0), axis=0)
    atlas_name = atlas_name.tolist()
    atlas_name = sorted(atlas_name, key=lambda x: x[0])
    atlas_name = np.array(atlas_name)

    return atlas_name


def search_size(corpus_callosum, axis):

    # Search for the size of the CC
    ymin = 1000
    ymax = 0

    centre_mass = center_of_mass(corpus_callosum)

    a = [centre_mass[k] if axis == k else slice(None) for k in range(len(corpus_callosum.shape))]  # 5
    slice_cut = corpus_callosum[a]

    somme = np.sum(slice_cut, axis=0)

    indx = np.argwhere(somme > 0)
    ymax = max(indx)
    ymin = min(indx)

    len_cc = ymax - ymin

    return ymax, ymin, len_cc

# %% Cell 2 - Registration

def get_cMetrics(code, f_path, patient):
    '''
    Creation of files containing the cFA, cMD, cAD and cRD for each patient. 'c' stands for compartment.

    Parameters
    ----------
    folder_path : string
        Path of the study.
    patient : string
        Name of a patient.

    Returns
    -------
    None.

   '''

    tenseur_list = ['t0', 't1']

    for tenseur in tenseur_list:

        path = f_path + '/subjects/' + patient + '/dMRI/microstructure/dti/' + patient + '_FA.nii.gz'

        comp = f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_' + tenseur + '.nii.gz'
        comp = nib.load(comp).get_fdata()

        MD = np.zeros((comp.shape[0], comp.shape[1], comp.shape[2]))
        AD = np.zeros((comp.shape[0], comp.shape[1], comp.shape[2]))
        RD = np.zeros((comp.shape[0], comp.shape[1], comp.shape[2]))
        FA = np.zeros((comp.shape[0], comp.shape[1], comp.shape[2]))

        D = np.array([[np.squeeze(comp[:, :, :, :, 0]), np.squeeze(comp[:, :, :, :, 1]), np.squeeze(comp[:, :, :, :, 3])],
                      [np.squeeze(comp[:, :, :, :, 1]), np.squeeze(comp[:, :, :, :, 2]), np.squeeze(comp[:, :, :, :, 4])],
                      [np.squeeze(comp[:, :, :, :, 3]), np.squeeze(comp[:, :, :, :, 4]), np.squeeze(comp[:, :, :, :, 5])]])

        for i in range(comp.shape[0]):
            for j in range(comp.shape[1]):
                for k in range(comp.shape[2]):

                    valeurs_propres = np.array(np.linalg.eigvals(D[:, :, i, j, k]))
                    max_valeur = max(np.abs(valeurs_propres))
                    index_lambda = [l for l in range(len(valeurs_propres)) if abs(valeurs_propres[l]) == max_valeur]

                    copy_valeurs_propres = np.copy(valeurs_propres)
                    copy_valeurs_propres = np.delete(copy_valeurs_propres, index_lambda[0])
                    copy_valeurs_propres = np.array(copy_valeurs_propres)

                    MD[i, j, k] = (valeurs_propres[0] + valeurs_propres[1] + valeurs_propres[2]) / 3
                    AD[i, j, k] = valeurs_propres[index_lambda[0]]
                    RD[i, j, k] = (copy_valeurs_propres[0] + copy_valeurs_propres[1]) / 2

                    if((valeurs_propres[0]**2 + valeurs_propres[1]**2 + valeurs_propres[2]**2) == 0):
                        FA[i, j, k] = 0
                    else:
                        FA[i, j, k] = np.sqrt(3 / 2) * np.sqrt(((valeurs_propres[0] - MD[i, j, k])**2 + (valeurs_propres[1] - MD[i, j, k])**2 + (valeurs_propres[2] - MD[i, j, k])**2) / (valeurs_propres[0]**2 + valeurs_propres[1]**2 + valeurs_propres[2]**2))

        MD[np.isnan(MD)] = 0
        out = nib.Nifti1Image(MD, affine=nib.load(path).affine, header=nib.load(path).header)
        out.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_MD_' + tenseur + '.nii.gz')

        AD[np.isnan(AD)] = 0
        out1 = nib.Nifti1Image(AD, affine=nib.load(path).affine, header=nib.load(path).header)
        out1.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_AD_' + tenseur + '.nii.gz')

        RD[np.isnan(RD)] = 0
        out2 = nib.Nifti1Image(RD, affine=nib.load(path).affine, header=nib.load(path).header)
        out2.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_RD_' + tenseur + '.nii.gz')

        FA[np.isnan(FA)] = 0
        out3 = nib.Nifti1Image(FA, affine=nib.load(path).affine, header=nib.load(path).header)
        out3.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_FA_' + tenseur + '.nii.gz')


def get_wMetrics(code, f_path, patient):
    '''
    Creation of files containing the wFA, wMD, wAD and wRD for each patient. 'w' stands for weigthed.

    Parameters
    ----------
    folder_path : string
        Path of the study.
    patient : string
        Name of a patient.

    Returns
    -------
    None.

    '''

    metrics = ['FA', 'MD', 'AD', 'RD']

    for metric in metrics:
        metric_t0 = f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_' + metric + '_t0.nii.gz'

        metric_t1 = f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_' + metric + '_t1.nii.gz'

        fraction_t0 = f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_f0.nii.gz'

        fraction_t1 = f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_f1.nii.gz'

        cMetric = (nib.load(metric_t0).get_fdata() * nib.load(fraction_t0).get_fdata() + nib.load(metric_t1).get_fdata() * nib.load(fraction_t1).get_fdata()) / (nib.load(fraction_t1).get_fdata() + nib.load(fraction_t0).get_fdata())
        cMetric[np.isnan(cMetric)] = 0

        out = nib.Nifti1Image(cMetric, affine=nib.load(metric_t0).affine, header=nib.load(metric_t0).header)
        out.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_w' + metric + '.nii.gz')


def get_diamond_fractions(code, f_path, patient):

    fractions_diamond = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_fractions.nii.gz')

    fractions_diamond_array = fractions_diamond.get_fdata()

    fraction_f0 = np.squeeze(fractions_diamond_array[:, :, :, :, 0])
    fraction_f1 = np.squeeze(fractions_diamond_array[:, :, :, :, 1])
    fraction_csf = np.squeeze(fractions_diamond_array[:, :, :, :, 2])

    out_f0 = nib.Nifti1Image(fraction_f0, fractions_diamond.affine, header=fractions_diamond.header)
    out_f0.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_f0.nii.gz')

    out_f1 = nib.Nifti1Image(fraction_f1, fractions_diamond.affine, header=fractions_diamond.header)
    out_f1.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_f1.nii.gz')

    out_csf = nib.Nifti1Image(fraction_csf, fractions_diamond.affine, header=fractions_diamond.header)
    out_csf.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_csf.nii.gz')

    out_ftot = nib.Nifti1Image(fraction_f0 + fraction_f1, fractions_diamond.affine, header=fractions_diamond.header)
    out_ftot.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/diamond/' + patient + '_diamond_frac_ftot.nii.gz')


def get_mf_fractions(code, f_path, patient):

    load_path = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_frac_f0.nii.gz')

    path_f0 = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_frac_f0.nii.gz').get_fdata()

    path_f1 = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_frac_f1.nii.gz').get_fdata()

    path_wf0 = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_fvf_f0.nii.gz').get_fdata()

    path_wf1 = nib.load(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_fvf_f1.nii.gz').get_fdata()

    wMetric = ((path_f0 * path_wf0) + (path_f1 * path_wf1)) / (path_f0 + path_f1)
    wMetric[np.isnan(wMetric)] = 0

    out1 = nib.Nifti1Image(path_f0 + path_f1, affine=load_path.affine, header=load_path.header)
    out1.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_frac_ftot.nii.gz')

    # out11 = nib.Nifti1Image(path_wf0 + path_wf1, affine=load_path.affine, header=load_path.header)
    # out11.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_fvf_ftot.nii.gz')

    out2 = nib.Nifti1Image(wMetric, affine=load_path.affine, header=load_path.header)
    out2.to_filename(f_path + '/subjects/' + patient + '/dMRI/microstructure/mf/' + patient + '_mf_wfvf.nii.gz')

# %% Cell 3 - Analyse

def jsonToPandas(jsonFilePath: str):

    file = open(jsonFilePath)
    dic = json.load(file)
    # dic = dic['Mean']
    file.close()

    reform = {(level1_key, level2_key, level3_key, level4_key): values
              for level1_key, level2_dict in dic.items()
              for level2_key, level3_dict in level2_dict.items()
              for level3_key, level4_dict in level3_dict.items()
              for level4_key, values in level4_dict.items()}

    p = pd.DataFrame(reform, index=['Value']).T
    p = p.rename_axis(['Dic', 'Patient', 'Region', 'Metric'])

    return p


if __name__ == '__main__':

    code = sys.argv[1]
    f_path = sys.argv[2]
    patient = sys.argv[3]

    if code == 'CMetric':
        get_cMetrics(code, f_path, patient)

    elif code == 'WMetric':
        get_wMetrics(code, f_path, patient)

    elif code == 'diamond_frac':
        get_diamond_fractions(code, f_path, patient)

    elif code == 'mf_frac':
        get_mf_fractions(code, f_path, patient)
