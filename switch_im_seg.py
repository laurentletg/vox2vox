import os, glob, re, shutil
path = '/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/HDF5_consecutive'

path_out = os.path.join('/home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA','HDF5_consecutive_predict_CTs')
os.makedirs(path_out, exist_ok=True)


for dirname, dirnames, filenames in os.walk(path):
# print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))
        # print path to all filenames.
    if 'train' in dirname:
        for filename in filenames:
            print(os.path.join(dirname, filename))
            if filename.endswith('.im'):
                src = os.path.join(dirname, filename)
                newfilename = filename.replace('.im', '.seg')
                dst = os.path.join(path_out, 'train', newfilename)
                os.makedirs(dst, exist_ok=True)
                shutil.copy(src, dst)
            if filename.endswith('.seg'):
                src = os.path.join(dirname, filename)
                newfilename = filename.replace('.seg', '.im')
                dst = os.path.join(path_out, 'train', newfilename)
                os.makedirs(dst, exist_ok=True)
                shutil.copy(src, dst)
    if 'test' in dirname:
        for filename in filenames:
            print(os.path.join(dirname, filename))
            if filename.endswith('.im'):
                src = os.path.join(dirname, filename)
                newfilename = filename.replace('.im', '.seg')
                dst = os.path.join(path_out, 'test', newfilename)
                os.makedirs(dst, exist_ok=True)
                shutil.copy(src, dst)
            if filename.endswith('.seg'):
                src = os.path.join(dirname, filename)
                newfilename = filename.replace('.seg', '.im')
                dst = os.path.join(path_out, 'test', newfilename)
                os.makedirs(dst, exist_ok=True)
                shutil.copy(src, dst)





# # rename files ending with .im as .seg and those ending with .seg as .im and copy to path_out
# files = sorted(glob.glob(os.path.join(path, '*.im')))
# print(len(files))
# for i, file in enumerate(files):
#     print(file)
#     print(i)
#     new_name = f'HDF5_{i}.seg'
#     print(new_name)
#     shutil.copy(file, os.path.join(path_out, new_name))
#
# files = sorted(glob.glob(os.path.join(path, '*.seg')))
# print(len(files))
# for i, file in enumerate(files):
#     print(file)
#     print(i)
#     new_name = f'HDF5_{i}.im'
#     print(new_name)
#     shutil.copy(file, os.path.join(path_out, new_name))