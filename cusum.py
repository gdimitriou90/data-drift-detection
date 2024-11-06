import pandas as pd
import numpy as np

df = pd.read_csv("test_unorm.csv")

def cusum(data, threshold=1):
    mean = np.mean(data)
    pos_cusum = np.zeros(len(data))
    neg_cusum = np.zeros(len(data))
    for i in range(1, len(data)):
        pos_cusum[i] = max(0, pos_cusum[i-1] + (data[i] - mean) - threshold)
        neg_cusum[i] = min(0, neg_cusum[i-1] + (data[i] - mean) + threshold)
    drift_pos = np.where(pos_cusum > threshold)[0]
    drift_neg = np.where(neg_cusum < -threshold)[0]
    return drift_pos, drift_neg

noise_HB_1 = [0] * len(df)
noise_HB_2 = [0] * len(df)

drift_pos_hb1, drift_neg_hb1 = cusum(df['HB_1'])
drift_pos_hb2, drift_neg_hb2 = cusum(df['HB_2'])

for idx in drift_pos_hb1:
    noise_HB_1[idx] = 1
for idx in drift_pos_hb2:
    noise_HB_2[idx] = 1

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

output_file_path = "drift_detection_cusum.csv"
output_df.to_csv(output_file_path, index=False)
print(f"Drift detection results saved to {output_file_path}")