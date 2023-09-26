import os, re, glob, shutil
import torch
from sklearn.model_selection import train_test_split
import nibabel as nib

# Check if gpu is available
print(torch.cuda.is_available())
print(torch.cuda.device_count())
# Check if cudnn is enabled
print(torch.backends.cudnn.enabled)

# get the data
data_path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/vox2vox/data/data for registered and resampled volumes'
print(data_path)
#get the CT (volume) and MR (target)
ct_path = os.path.join(data_path, 'CTwhole_resampled_norm')
mr_path = os.path.join(data_path, 'MRIregistration_resampled_norm')

# get the list of files
ct_files = sorted(os.listdir(ct_path))
print(f'CT files: {len(ct_files)}')
mr_files = sorted(os.listdir(mr_path))
print(f'MR files: {len(mr_files)}')

# split the data into train and test
ct_train, ct_test, mr_train, mr_test = train_test_split(ct_files, mr_files, test_size=0.2, random_state=42)
print(ct_train[0])
print(f'CT train: {len(ct_train)}')
print(f'CT test: {len(ct_test)}')
print(f'MR train: {len(mr_train)}')
print(f'MR test: {len(mr_test)}')
# move the files to the appropriate folders

# Create directories for volumes and masks, train and test
train_dir = os.path.join(data_path, 'train')
test_dir = os.path.join(data_path, 'test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# create directories for volumes and targets in each train and test
train_ct_dir = os.path.join(train_dir, 'ct')
train_mr_dir = os.path.join(train_dir, 'mr')
test_ct_dir = os.path.join(test_dir, 'ct')
test_mr_dir = os.path.join(test_dir, 'mr')
os.makedirs(train_ct_dir, exist_ok=True)
os.makedirs(train_mr_dir, exist_ok=True)
os.makedirs(test_ct_dir, exist_ok=True)
os.makedirs(test_mr_dir, exist_ok=True)

# copy files only if not done before
# for ct, mr in zip(ct_train, mr_train):
#     shutil.copy(os.path.join(ct_path, ct), train_ct_dir)
#     shutil.copy(os.path.join(mr_path, mr), train_mr_dir)
#
# for ct, mr in zip(ct_test, mr_test):
#     shutil.copy(os.path.join(ct_path, ct), test_ct_dir)
#     shutil.copy(os.path.join(mr_path, mr), test_mr_dir)

# Read .nii.gz using nibabel
ct = nib.load(os.path.join(ct_path, ct_train[0]))
ct_data = ct.get_fdata()
print(ct_data.shape)




