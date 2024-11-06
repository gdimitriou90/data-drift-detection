import pandas as pd
from scipy.stats import entropy

df = pd.read_csv("test_unorm.csv")

def kl_divergence(window1, window2):
    return entropy(window1, window2)

window_size = 500
significance_threshold = 0.1
noise_HB_1 = [0] * len(df)
noise_HB_2 = [0] * len(df)

for i in range(0, len(df) - window_size, window_size):
    if len(df['HB_1'].iloc[i + window_size:i + 2 * window_size]) < window_size:
        continue
    kl_hb1 = kl_divergence(df['HB_1'].iloc[i:i + window_size], df['HB_1'].iloc[i + window_size:i + 2 * window_size])
    kl_hb2 = kl_divergence(df['HB_2'].iloc[i:i + window_size], df['HB_2'].iloc[i + window_size:i + 2 * window_size])
    if kl_hb1 > significance_threshold:
        noise_HB_1[i + window_size:i + 2 * window_size] = [1] * window_size
    if kl_hb2 > significance_threshold:
        noise_HB_2[i + window_size:i + 2 * window_size] = [1] * window_size

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

output_file_path = "drift_detection_kl.csv"
output_df.to_csv(output_file_path, index=False)
print(f"Drift detection results saved to {output_file_path}")