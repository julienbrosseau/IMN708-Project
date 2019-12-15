# Segmentation des images par innondation

from skimage import filters
from skimage.segmentation import flood

import bin.treatment as tr
treatment = tr.Treatment()

class SegFlooding():
    
    def __init__(self):
        # Initialisation de la classe
        pass

    def set_sobel(self, img_2d):
        # Transformee de Sobel
        return filters.sobel(img_2d)

    def fit(self, sobel, pixel_ref, tolerance):
        # Segmentation d'image par baguette magique & innondation
        return flood(sobel, (pixel_ref[0], pixel_ref[1]), tolerance=tolerance)
    
    def get_img_denoise(self, img_2d):
        # Retourne l'image debruitee
        return treatment.median_filter(img_2d, 5)