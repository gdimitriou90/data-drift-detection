import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

df = pd.read_csv("test_unorm.csv")

def pca_drift_detection(data, baseline_window):
    pca = PCA(n_components=0.95)
    pca.fit(baseline_window)
    return pca.explained_variance_ratio_

baseline_size = 100
window_size = 500
noise_HB_1 = [0] * len(df)
noise_HB_2 = [0] * len(df)

baseline_hb1 = df['HB_1'].iloc[:baseline_size].values.reshape(-1, 1)
baseline_hb2 = df['HB_2'].iloc[:baseline_size].values.reshape(-1, 1)

for i in range(baseline_size, len(df) - window_size, window_size):
    window_hb1 = df['HB_1'].iloc[i:i + window_size].values.reshape(-1, 1)
    window_hb2 = df['HB_2'].iloc[i:i + window_size].values.reshape(-1, 1)
    var_ratio_hb1 = pca_drift_detection(window_hb1, baseline_hb1)
    var_ratio_hb2 = pca_drift_detection(window_hb2, baseline_hb2)
    if abs(var_ratio_hb1[0] - np.mean(var_ratio_hb1)) > 0.05:
        noise_HB_1[i:i + window_size] = [1] * window_size
    if abs(var_ratio_hb2[0] - np.mean(var_ratio_hb2)) > 0.05:
        noise_HB_2[i:i + window_size] = [1] * window_size

output_df = pd.DataFrame({
    'HB_1': df['HB_1'],
    'HB_2': df['HB_2'],
    'time': df['time'],
    'seq_id': df['seq_id'],
    'night': df['night'],
    'majority': df['majority'],
    'noise_HB_1': noise_HB_1,
    'noise_HB_2': noise_HB_2
})

output_file_path = "drift_detection_pca.csv"
output_df.to_csv(output_file_path, index=False)
print(f"Drift detection results saved to {output_file_path}")