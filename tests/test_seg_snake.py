# Test du fichier "seg_snake.py"

import matplotlib.pyplot as plt
import numpy as np

import bin.treatment as tr
import bin.seg_snake as seg

path             = "data/nifti"
analyse_axial    = "14971938_T2_AX_FS_20110309130206_8.nii"
analyse_coronal  = "14971938_T2_STIR_CORO_20110309130206_7.nii"
analyse_sagittal = "14971938_T1_TSE_SAG_FS_GADO_20110309130206_13.nii"

# Initalisation de la classe "Treatment"
treatment = tr.Treatment()

# Ouverture du fichier
img_3d = treatment.open_file(path, analyse_axial)

# Recuperation d'une tranche
img_2d = treatment.get_slice(img_3d, "axial", 15)
img_2d = treatment.set_box(img_2d, (180,100), 150, 150) # Box pour la coupe axiale
#img_2d = treatment.set_box(img_2d, (150,150), 100, 300) # Box pour les coupes coronale et sagittale

# Initialisation de la classe "SegSnake"
snake = seg.SegSnake()

# Définir le cercle de points
snake.set_circle_points(200, [75, 75], 34)

# Contour de l'image
img_contour = snake.get_active_contour(img_2d, 0.05, 0)
img_cercle = snake.get_points()

# Fixe les labels de l'image
snake.set_labels(img_2d, [75, 75], 17)

# Segmentation de l'image
img_seg = snake.get_seg(img_2d, 5000)

# Affichage
fig, ax = plt.subplots(ncols=3)

ax[0].title.set_text("Image d'origine")
ax[0].imshow(img_2d, cmap='gray')

ax[1].title.set_text("Contour de l'image")
ax[1].imshow(img_2d, cmap='gray')
ax[1].plot(img_cercle[:, 0], img_cercle[:, 1], '--r', lw=1)
ax[1].plot(img_contour[:, 0], img_contour[:, 1], '-b', lw=1)

ax[2].title.set_text("Post-traitement")
ax[2].imshow(img_seg, cmap='gray')

plt.show()