# Test traitement d images

from bin import traitement
import matplotlib.pyplot as plt

path             = "data/nifti"
analyse_axial    = "14971938_T2_AX_FS_20110309130206_8.nii"
analyse_coronal  = "14971938_T2_STIR_CORO_20110309130206_7.nii"
analyse_sagittal = "14971938_T1_TSE_SAG_FS_GADO_20110309130206_13.nii"

# Test ouverture d un fichier
img_3d = traitement.open_file(path, analyse_axial)

# Test debruitage d un fichier
denoise = traitement.debruitage(img_3d, 15)

# Test recuperation taile de l image
print(traitement.get_shape(img_3d))

# Test recuperation d une coupe
fig, ax = plt.subplots(nrows=2)
#fig, ax = plt.subplots(ncols=2)
ax[0].imshow(traitement.get_slice(img_3d, "axial", 15), cmap='gray')
ax[0].axis('off')
ax[1].imshow(traitement.get_slice(denoise, "axial", 15), cmap='gray')
ax[1].axis('off')
fig.tight_layout()
plt.show()