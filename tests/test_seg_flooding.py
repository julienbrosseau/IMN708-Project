# Test du fichier "seg_flooding.py"

import matplotlib.pyplot as plt

import bin.treatment as tr
import bin.seg_flooding as seg

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

# Initialisation de la classe "SegFlooding"
flooding = seg.SegFlooding()

# Segmentation de l'image
img_sobel = flooding.set_sobel(img_2d)
img_flooding = flooding.fit(img_sobel, [85, 75], 0.0012)

# Debruitage de l'image
img_denoise = flooding.get_img_denoise(img_flooding)

# Affichage
fig, ax = plt.subplots(ncols=3)

ax[0].title.set_text("Image d'origine")
ax[0].imshow(img_2d, cmap='gray')

ax[1].title.set_text("Segmentation par innondation")
ax[1].imshow(img_flooding, cmap='gray')
ax[1].plot(75, 85, 'bo')

ax[2].title.set_text("Post-traitement")
ax[2].imshow(img_denoise, cmap='gray')

plt.show()