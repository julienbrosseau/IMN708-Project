# Traitement des images

import os
import numpy as np
import nibabel as nib
from dipy.denoise.nlmeans import nlmeans
import matplotlib.pyplot as plt
from matplotlib import cm

class Treatment():
    def __init__(self):
        # Initialisation de la classe
        pass

    def open_file(self, path, img_nii):
        # Ouvrir l image .nii
        img = nib.load(os.path.join(path, img_nii))
        
        return np.squeeze(img.get_data())

    def debruitage(self, img_3d, sigma, mask=None):
        # Debruitage de l image (bruit ricien)
        return nlmeans(img_3d, sigma, mask, rician=True)

    def median_filter(self, data, sigma):
        # Filtage médian
        return ndimage.median_filter(data, size=sigma)

    def get_slice(self, img_3d, section, slice):
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

    def get_shape(self, img_3d):
        # Retroune la taille de l'image
        return img_3d.shape

    def normalize(self, arr):
        # Normalisation de l'image pour le calcul des contrastes et l'affichage de l'histogramme
        arr_min = np.min(arr)
        
        return (arr-arr_min)/(np.max(arr)-arr_min)

    def get_histogram(self, img_2d):
        # Affiche l'histogramme de l'image
        n, bins, patches = plt.hist(img_2d.reshape(-1), 50, density=1)
        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        for c, p in zip(normalize(bin_centers), patches):
            plt.setp(p, 'facecolor', cm.viridis(c))

        plt.show()

    def set_box(self, img_2d, cropx, cropy):
        # Retroune un box de taille cropx, cropy
        y,x = img_2d.shape
        startx = x//2-(cropx//2)
        starty = y//2-(cropy//2) 

        return img_2d[starty:starty+cropy,startx:startx+cropx]
