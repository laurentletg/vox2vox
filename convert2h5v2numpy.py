import nibabel as nib
import numpy as np
import os, re, glob, shutil
import h5py
from tqdm import tqdm
import SimpleITK as sitk

path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/vox2vox'
print(path)

path_train = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/cropped_registered_split/train'
path_test = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/cropped_registered_split/test'

train_cts = glob.glob(os.path.join(path_train, 'ct', '*.npy'))
train_mrs = glob.glob(os.path.join(path_train, 'mr', '*.npy'))
print(f'CT train: {len(train_cts)}')
print(f'MR train: {len(train_mrs)}')

test_cts = glob.glob(os.path.join(path_test, 'ct', '*.npy'))
test_mrs = glob.glob(os.path.join(path_test, 'mr', '*.npy'))
print(f'CT test: {len(test_cts)}')
print(f'MR test: {len(test_mrs)}')


# read  numpy array
def read_numpy(path, data=None):
    data = np.load(path)
    return data


# batch read nifti to numpy array and save as h5, the h5 extension needs to be changed to either .im or .seg according if ct or mr
def batch_read_numpy(path, save_path, subfolder='train'):
    """
    :param path: either train or test path
    :param save_path: output path
    :return:
    """
    save_path = os.path.join(save_path, 'HDF5', subfolder)
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    cts = glob.glob(os.path.join(path, subfolder, 'ct', '*.npy'))
    mrs = glob.glob(os.path.join(path, subfolder, 'mr', '*.npy'))

    for i, (ct, mr) in tqdm(enumerate(zip(cts, mrs))):
        print(f'Processing {i}th file')
        print(f'CT: {ct}')
        print(f'MR: {mr}')
        data_ct = read_numpy(ct)
        data_mr = read_numpy(mr)
        print(f'CT shape: {data_ct.shape}')
        print(f'MR shape: {data_mr.shape}')
        # write ct with .im extension
        test_path = os.path.join(save_path, ct.split('/')[-1].split('.')[0] + '_HDF5' + '.im')
        print(f'Test path: {test_path}')
        hf_ct = h5py.File(os.path.join(save_path, ct.split('/')[-1].split('.')[0] + '_HDF5' + '.im'), 'w')
        hf_ct.create_dataset('CTs',  dtype=np.float32, data=data_ct)
        hf_ct.close()
        # write mr with .seg extension
        hf_mr = h5py.File(os.path.join(save_path, mr.split('/')[-1].split('.')[0] + '_HDF5' + '.seg'), 'w')
        hf_mr.create_dataset('MRs',  dtype=np.float32, data=data_mr)
        hf_mr.close()

        #
#
#
# run script
if __name__ == '__main__':
    PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/cropped_registered_split'
    SAVE_PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA'
    batch_read_numpy(PATH, SAVE_PATH, subfolder='train')
    batch_read_numpy(PATH, SAVE_PATH, subfolder='test')
