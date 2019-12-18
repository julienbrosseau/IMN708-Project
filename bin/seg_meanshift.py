# Segmentation des images par Mean Shift

from sklearn.cluster import MeanShift
import numpy as np

import bin.treatment as tr
treatment = tr.Treatment()

class SegMeanShift():

    def __init__(self):
        # Initialisation de la classe
        self.ms = MeanShift(
            bandwidth = 40,
            bin_seeding = True
            )
        self.labels = []

    def fit(self, flat_img):
        # Entrainement du modèle
        self.ms = self.ms.fit(flat_img)
    
    def get_labels(self):
        # Retourne les labels du modèle
        return self.ms.labels_

    def get_img_reshape(self, cropx, cropy):
        # Retourne l'image redimensionnee
        return np.reshape(self.labels, [cropx, cropy])
    
    def get_img_denoise(self, cropx, cropy):
        # Retourne l'image debruitee
        return treatment.median_filter(self.get_img_reshape(cropx, cropy), 5)

    def set_labels(self, labels):
        # Fixe les labels
        self.labels = labels
    
    def set_clustering(self):
        # Traite les labels
        self.labels = np.where(self.labels == 2, self.labels, 0)
    