# Traitement des images

# Imports
import os
import numpy as np
import nibabel as nib
from skimage.restoration import denoise_nl_means

# Fonctions
def open_file(path, img_nii):
    # Ouvrir l image .nii
    img = nib.load(os.path.join(path, img_nii))
    return np.squeeze(img.get_data())

def debruitage(img_3d, type=0):
    # Debruitage de l image
    patch_kw = dict(patch_size=5,      # 5x5 patches
                patch_distance=6,  # 13x13 search area
                multichannel=True)

    if type == 0:
        # fast algorithm
        denoise = denoise_nl_means(img_3d, h=0.8 * 0.08, fast_mode=True, **patch_kw)
    elif type == 1:
        # slow algorithm
        denoise = denoise_nl_means(img_3d, h=1.15 * 0.08, fast_mode=False, **patch_kw)
    else:
        denoise = "erreur de type"

    return denoise

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
