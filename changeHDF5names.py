import os, glob, re, shutil

TRAIN_PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5/train'
TEST_PATH = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5/test'

# Change filenames so that the numbers are consecutive
# shutil copy the files to the appropriate folders

new_hdf5_path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5_consecutive'
os.makedirs(new_hdf5_path, exist_ok=True)

# add train and test folders
new_train_path = os.path.join(new_hdf5_path, 'train')
new_test_path = os.path.join(new_hdf5_path, 'test')
os.makedirs(new_train_path, exist_ok=True)
os.makedirs(new_test_path, exist_ok=True)


# convert .im files train
files = sorted(glob.glob(os.path.join(TRAIN_PATH, '*.im')))
print(len(files))
for i, file in enumerate(files):
    print(file)
    print(i)
    new_name = f'HDF5_{i}.im'
    print(new_name)
    shutil.copy(file, os.path.join(new_train_path, new_name))

# convert .seg files
files = sorted(glob.glob(os.path.join(TRAIN_PATH, '*.seg')))
print(len(files))
for i, file in enumerate(files):
    print(file)
    print(i)
    new_name = f'HDF5_{i}.seg'
    print(new_name)
    shutil.copy(file, os.path.join(new_train_path, new_name))

files = sorted(glob.glob(os.path.join(TEST_PATH, '*.im')))
print(len(files))
for i, file in enumerate(files):
    print(file)
    print(i)
    new_name = f'HDF5_{i}.im'
    print(new_name)
    shutil.copy(file, os.path.join(new_test_path, new_name))

# convert .seg files
files = sorted(glob.glob(os.path.join(TEST_PATH, '*.seg')))
print(len(files))
for i, file in enumerate(files):
    print(file)
    print(i)
    new_name = f'HDF5_{i}.seg'
    print(new_name)
    shutil.copy(file, os.path.join(new_test_path, new_name))


