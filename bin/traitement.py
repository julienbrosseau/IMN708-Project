# Traitement des images

# Imports
import os
import numpy as np
import nibabel as nib
from dipy.denoise.nlmeans import nlmeans

# Fonctions
def open_file(path, img_nii):
    # Ouvrir l image .nii
    img = nib.load(os.path.join(path, img_nii))
    return np.squeeze(img.get_data())

def debruitage(img_3d, sigma, mask=None):
    # Debruitage de l image (bruit ricien)
    return nlmeans(img_3d, sigma, mask, rician=True)

def get_slice(img_3d, section, slice):
    # Recupere une image parmi toutes
    if section == 'sagittal':
        try:
            img_2d = np.rot90(img_3d[slice,:,:])
        except:
            print("Error : no section 'sagittal' \n")
    if section == 'coronal':
        try:
            img_2d = np.rot90(np.flip(img_3d, axis=1)[:,slice,:])
        except:
            print("Error : no section 'coronal' \n")
    if section == 'axial':
        try:
            img_2d = np.rot90(np.flip(img_3d, axis=2)[:,:,slice])
        except:
            print("Error : no section 'axial' \n")

    return img_2d

def get_shape(img_3d):
    return img_3d.shape
