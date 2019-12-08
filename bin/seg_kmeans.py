# Segmentation des images par K-Means

from sklearn.cluster import KMeans
import numpy as np

import bin.treatment as tr
treatment = tr.Treatment()

class SegKMeans():

    def __init__(self):
        # Initialisation de la classe
        self.kmeans = KMeans(
            n_clusters = 3, 
            random_state = 0
            )
        self.labels = []

    def fit(self, flat_img):
        # Entrainement du modèle
        self.kmeans = self.kmeans.fit(flat_img)
    
    def get_labels(self):
        # Retourne les labels du modèle
        return self.kmeans.labels_

    def get_img_reshape(self, cropx, cropy):
        # Retourne l'image redimensionnee
        return np.reshape(self.labels, [cropx, cropy])
    
    def get_img_denoise(self, cropx, cropy):
        # Retourne l'image debruitee
        return treatment.median_filter(self.get_img_reshape(cropx, cropy), 7)

    def set_labels(self, labels):
        # Fixe les labels
        self.labels = labels
    
    def set_clustering(self):
        # Traite les labels
        self.labels = np.where(self.labels == 1, self.labels, 0)
    