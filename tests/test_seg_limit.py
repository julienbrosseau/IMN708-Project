# Test du fichier "seg_limit.py"

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

import bin.treatment as tr
import bin.seg_limit as seg

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
img_2d = treatment.set_box(img_2d, 150, 150)

# Initialisation de la classe "SegLimit"
seg_limit = seg.SegLimit()

# Segmentation "seuil"
img_2d_seg = seg_limit.fit(img_2d)

plt.imshow(img_2d)
plt.show()
