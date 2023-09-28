# Vox to vox attempt. 
## Task: trying to generate synthetic CTAs using MRAs from the TopCOW23 challenge
# Components
## 1. Registration
   - Currently using Lucas' data on the [google drive](https://drive.google.com/drive/folders/145M45MfUUFYcWKULO5a-EKX-3w9Ar0hh?usp=drive_link)
      - This data has been resampled (BSline) to 256x256x200 --> this may not be ideal for final model if vox2vox performs well since small vessels may be lost (e.g. Acomm and Pcomm)
   - Cropping the MRA
     - the z-axis extent of the MRA is shorter than the CTA especially at the superior margin (i.e. the MRA does not extend as far superiorly as the CTA)
     - I have a code under crop.py to dynamically crop the MRA (calculates the superior and inferior margins) based on the number of voxels in a slice that are above a certain value. 
       - This was guestimated using Slicer and the value (values were after the normalization) with a proportion of filled voxels above 0.8. 
   - Next approach:
     - Normalize CTA and MRA and resample to 512 x 512 x 256 (most CTAs have around 200-250 slices)
       - (ChatGPT recommended to normalize and resample to a common resolution prior to registration to help with registration)
     - Register MRA to CTA
       - Use Lucas's code (seeems to be from the simpleITK jupyter notebook tutorial including 'multiresolution registration')
       - Seems to help to have to at least 2 registration attempts. 
       - TODO : save the transformation matrix so that this could be used to register the masks as wells 
         - There is indeed some deformation of the MRA and CTA (may be due to MRI distortion correction ?).

## 2. pix2pix vs vox2vox
   - Currently attempting vox2vox
   - Should take a look at pix2pix later

   

## 3. Data location
1. Cropped registered resampled (MUST BE A MULTIPLE OF 8 OR 64), else the model will not work (e.g. 256x256x256):
   - /home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/cropped...
   - TODO : try 256 x 256 x 128 (256 x 256 x 256 was too much for the model to handle)
   - TODO : may consider windowing the CTA data (but may not work well with the input of the next model)
2. Original data
    - /home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/DATA 2023 MICCAI TopCOW23 Challenge-20230908T120155Z-008/2023 MICCAI TopCOW23 Challenge/DATA/CT or MR...

## 4. Main LLG files
    - STEP 0. Jupyter notebook with slider under /home/llg/Dropbox/CHUM/RECHERCHE/2024 CTA COW/Register/code to_register.ipynb
    -   - a critical part is the intensity threshold and proportion of voxels, not perfect. Some MRAs have been 
    - Code has been changed to keep only numpy arrays
    - STEP 1. splitmovetraintest.py :
        - allows to perform a train test split and copy the nii.gz in the appropriate folder. 
        - need to specify the right data folder, subfolder and output directory at the top of the file
    - STEP 2. Convert to hdf5 : convert2h5v2.py -> skip the numpy saving and save right away in numpy the hdf5. Note that using the slicer kernal h5py was crashing...
        - TODO : correct the order of .im and .seg they are reversed. 
    - STEP 3. ahge HDF5 names (so that they are consecutives). The data loader is configured to work with this. 
    - STEP 4. optional checkshapes
    - STEP 5. switch_im_seg.py  to correcte the wrong order of .im and .seg
    - STEP 6. train.py
        