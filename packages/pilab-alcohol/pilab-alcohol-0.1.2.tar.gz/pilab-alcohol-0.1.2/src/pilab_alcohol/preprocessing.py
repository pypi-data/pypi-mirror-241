
import os
import json
import elikopy

# %% Step 1 - Preprocessing
def elikopy_preprocessing(f_path, e_mail, patient_with_problem):
    '''
    Submission of the preprocessing job.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.
    patient_with_problem : list
        List of the patients name which need to be resliced.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True, slurm_email=e_mail, cuda=False)
    patient_path = f_path + 'subjects/subj_list.json'
    patient_with_problem = ['sub06_E1', 'sub67_E1']

    if os.path.exists(patient_path):
        patient_list = json.load(patient_path)
    else:
        study.patient_list()
        with open(patient_path, 'r') as read_file:
            patient_list = json.load(read_file)

    for i in patient_list:
        if i in patient_with_problem:
            study.preproc(eddy=True, topup=True, denoising=True, forceSynb0DisCo=True, patient_list_m=[i],
                          report=True, qc_reg=False, slurm_timeout="36:00:00", cpus=16)
        else:
            study.preproc(eddy=True, topup=True, denoising=True, forceSynb0DisCo=True, patient_list_m=[i],
                          reslice=True, report=True, qc_reg=False, slurm_timeout="36:00:00", cpus=16)


# %% Step 2 - White matter mask
def white_mask(f_path, e_mail, mask_type):
    '''
    Submission of the job creating the white matter mask.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.
    mask_type : string
        White matter type typically, 'wm_mask_FSL_T1'.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)

    study.white_mask(mask_type, corr_gibbs=True, cpus=2, debug=False)

# %% Step 3 - Microstructural models
def dti_model(f_path, e_mail):
    '''
    Submission of the job to compute the DTI model.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.dti()

def noddi_model(f_path, e_mail):
    '''
    Submission of the job to compute the NODDI model.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.noddi(slurm_timeout="30:00:00", cpus=8)

def diamond_model(f_path, e_mail):
    '''
    Submission of the job to compute the DIAMOND model.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.diamond(slurm_timeout="30:00:00", cpus=8)

def odf_model(f_path, e_mail):
    '''
    Submission of the job to compute the ODF model.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.odf_msmtcsd(num_peaks=2, peaks_threshold=0.25, slurm_timeout="5:00:00",
                      cpus=6)

def mf_model(f_path, e_mail, dic_path):
    '''
    Submission of the job to compute the MF model.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.
    dic_path : string
        Path of the dictionary to be used to compute MF.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.fingerprinting(dictionary_path=dic_path, patient_list_m=["sub26_E2", "sub64_E2", "sub02_E2", "sub40_E2", "sub18_E2", "sub70_E2", "sub52_E2", "sub51_E2", "sub36_E2", "sub48_E2", "sub46_E2", "sub03_E2", "sub41_E2", "sub27_E3", "sub34_E3", "sub09_E3", "sub02_E3", "sub30_E3", "sub17_E3", "sub36_E3", "sub45_E3", "sub22_E3", "sub20_E3", "sub39_E3", "sub03_E3"], mfdir="mf", cpus=8,
                         peaksType="MSMT-CSD", slurm_mem=3096)


# %% Step 4 - Basic tractography
def basic_tracking(f_path, e_mail):
    '''
    Submission of the job to compute a basic tractography.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.tracking()


# %% Step 5 - Cleaning
def clean_our_study(f_path, e_mail):
    '''
    Submission of the job to clean the study and suppression of some files.

    Parameters
    ----------
    f_path : string
        Path of the study.
    e_mail : string
        Email address to which the failed job will be send.

    Returns
    -------
    None.

    '''
    study = elikopy.core.Elikopy(f_path, slurm=True,
                                 slurm_email=e_mail, cuda=False)
    study.clean_study(f_path, raw_bool=True)
