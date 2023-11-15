import numpy as np
import matplotlib.pyplot as plt
import os
from deep_lc.classifier import DeepLC


dc_combined = DeepLC(combined_model="/home/ckm/Projects/Transformer-trial/NTS_S/models/combined_17_conformal.ckpt", conformal_calibration=True, device='cpu')

# from glob import glob
# ktz3_path = "/home/ckm/Projects/Transformer-trial/data/Kep_ZTF_dataset/training-data-preparation/balona_lightcurves"
# data_path = np.random.choice(glob(ktz3_path u+ "/*.npy"), 1)[0]

# use specific data
data_path = "/home/ckm/Projects/Transformer-trial/data/Kep_ZTF_dataset/training-data-preparation/balona_lightcurves/12268220.npy"

# print file name without extension
print(os.path.splitext(os.path.basename(data_path))[0])
data = np.load(data_path, allow_pickle=True)

dc_combined.predict(data, show_intermediate_results=True, return_conformal_predictive_sets=True)