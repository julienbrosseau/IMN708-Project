# Segmentation des images par seuil

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
