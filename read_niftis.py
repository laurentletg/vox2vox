import nibabel as nib
import numpy as np
import os, re, glob, shutil
import h5py

path_train = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/vox2vox/data/data for registered and resampled volumes/train'
path_test = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/vox2vox/data/data for registered and resampled volumes/test'

path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/vox2vox'
print(path)

print(os.listdir(path_train))

# read nifti to numpy array
def read_nifti(path):
    img = nib.load(path)
    data = img.get_fdata()
    return data

# batch read nifti to numpy array and save as h5, the h5 extension needs to be changed to either .im or .seg according if ct or mr
def batch_read_nifti(path, save_path, subfolder = 'train'):
    """
    :param path: either train or test path
    :param save_path: output path
    :return:
    """
    save_path = os.path.join(save_path, subfolder)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    cts = glob.glob(os.path.join(path, 'ct', '*.nii.gz'))
    mrs = glob.glob(os.path.join(path, 'mr', '*.nii.gz'))
    for i, (ct, mr) in enumerate(zip(cts, mrs)):
        print(f'Processing {i}th file')
        print(f'CT: {ct}')
        print(f'MR: {mr}')
        data_ct = read_nifti(ct)
        data_mr = read_nifti(mr)
        print(f'CT shape: {data_ct.shape}')
        print(f'MR shape: {data_mr.shape}')
        # # write ct with .im extension
        # hf_ct = h5py.File(save_path + ct.split('/')[-1].split('.')[0] + '.im', 'w')
        # hf_ct.create_dataset('CTs',  dtype=np.float32, data=data_ct)
        # hf_ct.close()
        # # write mr with .seg extension
        # hf_mr = h5py.File(save_path + mr.split('/')[-1].split('.')[0] + '.seg', 'w')
        # hf_mr.create_dataset('MRs',  dtype=np.float32, data=data_mr)
        # hf_mr.close()
        #
        #

# run script
if __name__ == '__main__':
    batch_read_nifti(path_train, path + '/data/data for registered and resampled volumes', subfolder='train')
    # batch_read_nifti(path_test, path + '/data/data for registered and resampled volumes', subfolder='test')

