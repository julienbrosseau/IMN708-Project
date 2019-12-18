# Quantification des images

import numpy as np

class Quantification():

    def __init__(self):
        # Initialisation de la classe
        self.voxels = ()

    def set_voxels(self, img_3d):
        # Fixe la taille des voxels
        self.voxels = img_3d.header.get_zooms()

    def get_nb_pixels(self, img_2d):
        # Retourne le nombre de pixels de la segmentation
        nb_pixels = 0
        for i in range(img_2d.shape[0]):
            for j in range(img_2d.shape[1]):
                if img_2d[i][j] != 0:
                    nb_pixels += 1
        
        return nb_pixels
    
    def get_area(self, nb_pixels):
        # Retourne l'aire de la segmentation
        return nb_pixels * self.voxels[0] * self.voxels[1]
    
    def get_volume(self, list_area):
        # Retourne le volume de la segmentation
        return self.voxels[2] * np.sum(list_area)