import os
import sys
import numpy as np
import nibabel as nib
import regis.core as rg
from binama.utils import find_largest_volume
from utils import get_atlas_list, get_corr_atlas_list, search_size

def cc_division(code, path, name_part, division_frac):
    '''


    Parameters
    ----------
    path : TYPE
        DESCRIPTION.
    axis : TYPE
        DESCRIPTION.
    name_part : TYPE
        DESCRIPTION.
    division_frac : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    cc_path = path + "corpus_callosum_hand_drawn_smoothed.nii.gz"

    corpus_callosum_load = nib.load(cc_path)
    corpus_callosum = corpus_callosum_load.get_fdata().astype(np.float32)

    corpus_callosum[corpus_callosum != 0] = 1

    ymax, ymin, len_cc = search_size(corpus_callosum, 0)

    cut_indexes = np.zeros(len(name_part) + 1)
    cut_indexes[1:len(name_part)] = np.round(ymin + len_cc * np.array(division_frac))
    cut_indexes[-1] = corpus_callosum.shape[0]

    for i in range(len(name_part)):
        subdivision = np.zeros(corpus_callosum.shape)

        coord1 = int(cut_indexes[i])
        coord2 = int(cut_indexes[i + 1])

        subdivision[:, coord1:coord2, :] = corpus_callosum[:, coord1:coord2, :]
        subdivision = find_largest_volume(subdivision).astype(np.float32)

        out1 = nib.Nifti1Image(subdivision.astype(np.float32), affine=corpus_callosum_load.affine, header=corpus_callosum_load.header)
        out1.to_filename(path + name_part[i] + '.nii.gz')


def registration_atlas(code, f_path, path, moving_file, patient):
    '''


    Parameters
    ----------
    f_path : TYPE
        DESCRIPTION.
    static_file : TYPE
        DESCRIPTION.
    patient : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    atlas_list = get_atlas_list(path)
    atlas_name_list = get_corr_atlas_list(atlas_list)

    static_file = f_path + '/subjects/' + patient + '/dMRI/microstructure/dti/' + patient + '_FA.nii.gz'

    mapping = rg.find_transform(moving_file, static_file, only_affine=False, diffeomorph=True)

    for atlas in atlas_name_list:
        atlas_name = str(atlas[1])

        moving_file_bis = '/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Atlas/' + atlas_name

        new_atlas_name = atlas_name.replace('/', '/' + patient + '_')

        output_path = f_path + 'registration/' + patient + '/' + new_atlas_name
        rg.apply_transform(moving_file_bis, mapping, static_file, output_path, binary_thresh=float(atlas[2]), binary=True)


def registration_time(code, f_path, patient, model):
    '''
    Get the registered file for one patient btween two scan times.

    Parameters
    ----------
    f_path : TYPE
        DESCRIPTION.
    patient : list
        Name of the patient to register. For example, ['sub01_E1', 'sub01_E2'] with respectivelly the static and the moving file.
    model : list
        List containing the string of the model and one of its metrics. For example, ['dti', 'FA']

    Returns
    -------
    None.

    '''

    static_file = f_path + '/subjects/' + patient[0] + '/dMRI/microstructure/' + model[0] + '/' + patient[0] + '_' + model[1] + '.nii.gz'
    moving_file = f_path + '/subjects/' + patient[1] + '/dMRI/microstructure/' + model[0] + '/' + patient[1] + '_' + model[1] + '.nii.gz'

    output_path = f_path + '/registration/' + patient[1] + '/dMRI/microstructure/' + model[0] + '/' + patient[1] + '_on_' + patient[0] + '_' + model[1] + '.nii.gz'

    mapping = rg.find_transform(moving_file, static_file, only_affine=False, diffeomorph=True)
    rg.apply_transform(moving_file, mapping, static_file, output_path, binary=True)


def atlas_correction(f_path, path, patient):

    atlas_list = get_atlas_list(path)
    atlas_name_list = get_corr_atlas_list(atlas_list)

    for atlas in atlas_name_list:
        atlas_name = str(atlas[1])

        new_atlas_name = atlas_name.replace('/', '/' + patient + '_')

        output_path = f_path + 'registration/' + patient + '/' + new_atlas_name
        brain_path = f_path + 'subjects/' + patient + '/masks/' + patient + '_brain_mask_dilated.nii.gz'

        atlas = nib.load(output_path).get_fdata()
        brain_mask = nib.load(brain_path).get_fdata()

        new_mask = atlas * brain_mask

        out1 = nib.Nifti1Image(new_mask.astype(np.float32), affine=nib.load(output_path).affine, header=nib.load(output_path).header)
        out1.to_filename(f_path + 'registration/' + patient + '/' + new_atlas_name)


if __name__ == '__main__':

    code = sys.argv[1]

    if code == 'cc_division':
        path = sys.argv[2]
        name_part = sys.argv[3]
        division_frac = sys.argv[4]

        cc_division(code, path, name_part, division_frac)
    elif code == 'registration':
        f_path = sys.argv[2]
        path = sys.argv[3]
        static_file = sys.argv[4]
        patient = sys.argv[5]

        registration_atlas(code, f_path, path, static_file, patient)
        atlas_correction(f_path, path, patient)
