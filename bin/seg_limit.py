# Segmentation des images par seuil

import bin.treatment as tr
treatment = tr.Treatment()

class SegLimit():

    def __init__(self):
        # Initialisation de la classe
        self.seuil = 200

    def fit(self, img_2d):
        # Segmentation d'image par seuil
        for x in range(img_2d.shape[0]):
            for y in range(img_2d.shape[1]):
                if img_2d[x,y] > self.seuil:
                    img_2d[x,y] = 1
                else:
                    img_2d[x,y] = 0

        return img_2d
    
    def get_img_denoise(self, img_2d):
        # Retourne l'image debruitee
        return treatment.median_filter(img_2d, 5)
