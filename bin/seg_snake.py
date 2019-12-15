# Segmentation des images pas snake

import numpy as np
import skimage.draw as draw
import skimage.segmentation as seg

class SegSnake():

    def __init__(self):
        # Initialisation de la classe
        self.points = []
        self.labels = []

    def set_circle_points(self, resolution, center, radius):    
        # Fixe un cercle d'interet sur l'image avec son ensemble de points
        radians = np.linspace(0, 2*np.pi, resolution)    
        
        c = center[1] + radius*np.cos(radians)
        r = center[0] + radius*np.sin(radians)
        
        self.points = np.array([c, r]).T
    
    def get_points(self):
        # Retourne les points du cercle
        return self.points

    def get_active_contour(self, img_2d, alpha, beta):
        # Retourne la segmentation de l'image
        return seg.active_contour(img_2d, self.points, alpha=alpha, beta=beta)
    
    def set_labels(self, img_2d, center, radius):
        # Fixe les labels de l'image
        labels = np.zeros(img_2d.shape, dtype=np.uint8) 

        indices = draw.circle_perimeter(center[0], center[1], radius)

        labels[indices] = 1
        labels[self.points[:, 1].astype(np.int), self.points[:, 0].astype(np.int)] = 2

        self.labels = labels
    
    def get_seg(self, img_2d, beta):
        # Retroune la segmentation de l'image
        return seg.random_walker(img_2d, self.labels, beta=beta)
