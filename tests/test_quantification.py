# Test du fichier "quantification.py"

import numpy as np

import bin.treatment as tr
import bin.quantification as qu
import bin.seg_meanshift as seg

path             = "data/nifti"
analyse_axial    = "14971938_T2_AX_FS_20110309130206_8.nii"
analyse_coronal  = "14971938_T2_STIR_CORO_20110309130206_7.nii"
analyse_sagittal = "14971938_T1_TSE_SAG_FS_GADO_20110309130206_13.nii"

# Initialisation de la classe "Treatment"
treatment = tr.Treatment()

# Initialisation de la classe "KMeans"
mean_shift = seg.SegMeanShift()

# Initialisation de la classe "Quantification"
quantification = qu.Quantification()

# Traitement de l'image ----------------------------------------------
# Ouverture du fichier
img_3d = treatment.get_file(path, analyse_coronal)
data_img_3d = treatment.open_file(path, analyse_coronal)

# Debruitage de l'image
data_img_3d = treatment.debruitage(data_img_3d, 5)
# --------------------------------------------------------------------

# Segmentation de l'image --------------------------------------------
list_area = []

# Tumeur de l'image 6 à 21 pour la coupe 'axial'
for i in range(6, 22):

#for i in range(data_img_3d.shape[2]):
    img_2d = treatment.get_slice(data_img_3d, "axial", i)
    img_2d = treatment.set_box(img_2d, 150, 150)

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
    # --------------------------------------------------------------------

    # Quantification de l'image ------------------------------------------
    # Recuperation de la taille des voxels
    quantification.set_voxels(img_3d)

    # Recuperation du nombre de pixels de la segmentation
    nb_pixels = quantification.get_nb_pixels(img_denoise)

    # Recuperation de l'aire de la segementation
    seg_area = quantification.get_area(nb_pixels)

    list_area.append(seg_area)
    print("Aire de la segmention :", "{0:.2f}".format(seg_area), "mm², soit :", "{0:.2f}".format(seg_area/100), "cm².")

seg_volume = quantification.get_volume(list_area)
print("\nVolume de la segmention :", "{0:.2f}".format(seg_volume), "mm³, soit :", "{0:.2f}".format(seg_volume/1000), "cm³.")