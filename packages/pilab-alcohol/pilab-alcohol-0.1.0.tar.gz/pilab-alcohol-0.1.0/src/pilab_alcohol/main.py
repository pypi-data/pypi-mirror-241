import os
import json
from preprocessing import (elikopy_preprocessing, white_mask, dti_model, noddi_model,
                           diamond_model, odf_model, mf_model, basic_tracking, clean_our_study)
from registration import cc_division
from analyse import difference_temps
from utils import (folder_patients, get_diamond_fractions, get_mf_fractions,
                   get_cMetrics, get_wMetrics)

if __name__ == '__main__':

    e_mail = 'manon.dausort@gmail.com'

    root = '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/'

    f_path = root + 'alcoholic_study/'
    dic_path = '/CECI/proj/pilab/static_files_ELIKOPY/mf_dic/dictionary_fixed_rad_dist_StLuc-GE.mat'

    patient_with_problem = ['sub06_E1', 'sub67_E1']  # Patients needing to be reslice
    mask_type = 'wm_mask_FSL_T1'

    atlas_path = root + 'Atlas/'
    static_file = atlas_path + 'FSL_HCP1065_FA_1mm.nii.gz'
    name_part = ['corpus_callosum_splenium', 'corpus_callosum_isthmus', 'corpus_callosum_posterior_midbody', 'corpus_callosum_anterior_midbody', 'corpus_callosum_genu']
    division_frac = [1 / 4, 1 / 3, 1 / 2, 5 / 6]

    patient_path = f_path + 'subjects/subj_list.json'
    with open(patient_path, 'r') as read_file:
        patient_list = json.load(read_file)

    slurm_path = root + 'Pipeline/submitIter.sh'
    code_path = root + 'Pipeline/'

    # =============================================================================
    # Step 1
    # =============================================================================
    # print('Preprocessing of all patients')
    # elikopy_preprocessing(f_path, e_mail, patient_with_problem)

    # =============================================================================
    # Step 2
    # =============================================================================
    # Step 1 must be finished before starting Step 2 !
    # print('White matter mask of all patients')
    # white_mask(f_path, e_mail, mask_type)

    # =============================================================================
    # Step 3
    # =============================================================================
    # Step 2 must be finished before starting Step 3 !
    # The following lines can be launch at the same time but ODF must be finished before launching MF !

    # print('DTI of all patients')
    # dti_model(f_path, e_mail)

    # print('NODDI of all patients')
    # noddi_model(f_path, e_mail)

    # print('DIAMOND of all patients')
    # diamond_model(f_path, e_mail)

    # print('ODF of all patients')
    # odf_model(f_path, e_mail)

    # print('MF of all patients')
    # mf_model(f_path, e_mail, dic_path)

    # =============================================================================
    # Step 4
    # =============================================================================
    # print('Tractography of all patients')
    # basic_tracking(f_path, e_mail)

    # =============================================================================
    # Step 5
    # =============================================================================
    # print('Creation of corpus callosum divisions')
    # for patient in patient_list:
    #     os.system('sbatch -J ' + 'cc_' + patient + ' ' + slurm_path + ' ' + code_path + 'registration.py' + ' ' + 'cc_division' + ' ' + atlas_path + 'CC/' + ' ' + name_part + ' ' + division_frac)

    # sub_files = ['CC', 'Cerebellar', 'Cerebellum', 'Harvard', 'Harvard_cortex', 'Lobes', 'XTRACT']
    # folder_patients(root, patient_list, sub_files)

    # =============================================================================
    # Step 6
    # =============================================================================
    # print('Registration of the atlases for all patient')
    # for patient in patient_list:
    #     os.system('sbatch /CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'registration' + ' ' + f_path + ' ' + atlas_path + ' ' + static_file + ' ' + patient)

    # =============================================================================
    # Step 7
    # =============================================================================
    # print('Creation of the compartiment fractions')
    # for patient in patient_list:
    #     os.system('sbatch -J ' 'diamond_frac_' + str(patient) + ' ' + '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'diamond_frac' + ' ' + f_path + ' ' + patient)
    #     os.system('sbatch -J ' 'mf_frac_' + str(patient) + ' ' + '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'mf_frac' + ' ' + f_path + ' ' + patient)

    # print('Creation of the DIAMOND metrics')
    # for patient in patient_list:
    #     os.system('sbatch -J ' 'CMetric_' + str(patient) + ' ' + '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'CMetric' + ' ' + f_path + ' ' + patient)
    #     os.system('sbatch -J ' 'WMetric_' + str(patient) + ' ' + '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'WMetric' + ' ' + f_path + ' ' + patient)

    # =============================================================================
    # Step 8
    # =============================================================================
    print('Analyses by ROI')
    output_path = '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/Slurm/'

    os.system('sbatch -J ' 'Mean_ROI' + ' ' + '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/submitIter.sh ' + 'Mean_ROI' + ' ' + f_path + ' ' + output_path)

    # print('Difference between time')
    # dataframe1 = difference_temps(patient_list, 'Mean', output_path)
