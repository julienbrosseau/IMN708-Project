# Test de segmentation pour l'image IRM en entier avec la methode "mean-shift"

import matplotlib.pyplot as plt
import numpy as np

import bin.treatment as tr
import bin.seg_meanshift as seg

path             = "data/nifti"
analyse_axial    = "14971938_T2_AX_FS_20110309130206_8.nii"
analyse_coronal  = "14971938_T2_STIR_CORO_20110309130206_7.nii"
analyse_sagittal = "14971938_T1_TSE_SAG_FS_GADO_20110309130206_13.nii"

# Initalisation de la classe "Treatment"
treatment = tr.Treatment()

# Ouverture du fichier
img_3d = treatment.open_file(path, analyse_axial)

# Debruitage de l'image
img_3d = treatment.debruitage(img_3d, 5)

# Recuperation des tranches
list_img_2d = []

# Initialisation de la classe "KMeans"
mean_shift = seg.SegMeanShift()

# Tumeur de l'image 8 à 23
for i in range(img_3d.shape[2]):
    img_2d = treatment.get_slice(img_3d, "axial", i)
    img_2d = treatment.set_box(img, 150, 150)

    # Entrainement du modele
    flat_img = np.reshape(img_2d, [-1, 1])
    mean_shift.fit(flat_img)

    # Recuperer et fixer les labels
    mean_shift.set_labels(mean_shift.get_labels())

    # Recupere l'image avec tous les labels
    img_reshape = mean_shift.get_img_reshape(150, 150)

    # Fixe le label qui nous interresse et debruite l'image
    mean_shift.set_clustering()

    img_denoise = mean_shift.get_img_denoise(150, 150)

    # Affichage
    fig, ax = plt.subplots(ncols=3)

    ax[0].title.set_text("Image d'origine")
    ax[0].imshow(img_2d, cmap='gray')

    ax[1].title.set_text("'Clustering' par 'Mean Shift'")
    ax[1].imshow(img_reshape, cmap='gray')

    ax[2].title.set_text("Post-traitement")
    ax[2].imshow(img_denoise, cmap='gray')

    plt.show()