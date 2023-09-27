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

   