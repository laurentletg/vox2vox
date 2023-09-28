import os, glob, re, shutil
import numpy as np
import h5py

TRAIN_PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5/train'
TEST_PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5/test'

# Change filenames so that the numbers are consecutive
# shutil copy the files to the appropriate folders

new_hdf5_path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5_consecutive'
os.makedirs(new_hdf5_path, exist_ok=True)


files = sorted(glob.glob(os.path.join(TRAIN_PATH, '*.seg')))
print(len(files))
for i, file in enumerate(files):
    print(file)
    # load hdf5
    hf = h5py.File(file, 'r')
    print(hf.keys())
    assert hf['MRs'].shape == (128, 128, 128)
    # array = np.load(file)
    # print(array.shape)
