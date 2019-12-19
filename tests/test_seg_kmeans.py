# Test du fichier "seg_kmeans.py"

import matplotlib.pyplot as plt
import numpy as np

import bin.treatment as tr
import bin.seg_kmeans as seg

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
img_2d = treatment.set_box(img_2d, (180, 100), 150, 150)

# Initialisation de la classe "KMeans"
k_means = seg.SegKMeans()

# Entrainement du modele
flat_img = np.reshape(img_2d, [-1, 1])
k_means.fit(flat_img)

# Recuperer et fixer les labels
k_means.set_labels(k_means.get_labels())

# Recupere l'image avec tous les labels
img_reshape = k_means.get_img_reshape(150, 150)

# Fixe le label qui nous interresse et debruite l'image
k_means.set_clustering()

img_denoise = k_means.get_img_denoise(150, 150)

# Affichage
fig, ax = plt.subplots(ncols=3)

ax[0].title.set_text("Image d'origine")
ax[0].imshow(img_2d, cmap='gray')

ax[1].title.set_text("'Clustering' par 'K-Means'")
ax[1].imshow(img_reshape, cmap='gray')

ax[2].title.set_text("Post-traitement")
ax[2].imshow(img_denoise, cmap='gray')

plt.show()