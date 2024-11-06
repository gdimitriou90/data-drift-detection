import pandas as pd
from frouros.detectors.concept_drift import ADWIN
from sklearn.preprocessing import MinMaxScaler

file_path = "test_unorm.csv"
df = pd.read_csv(file_path)

scaler = MinMaxScaler()
df[['HB_1', 'HB_2']] = scaler.fit_transform(df[['HB_1', 'HB_2']])

adwin_hb1 = ADWIN()
adwin_hb2 = ADWIN()

print("Starting drift detection with ADWIN...")

noise_HB_1 = []
noise_HB_2 = []

for index in range(len(df)):
    point_hb1 = df['HB_1'].iloc[index]
    point_hb2 = df['HB_2'].iloc[index]

    drift_detected_hb1 = adwin_hb1.update(value=point_hb1)
    drift_detected_hb2 = adwin_hb2.update(value=point_hb2)

    noise_indicator_hb1 = 1 if drift_detected_hb1 else 0
    noise_indicator_hb2 = 1 if drift_detected_hb2 else 0

    noise_HB_1.append(noise_indicator_hb1)
    noise_HB_2.append(noise_indicator_hb2)

    if noise_indicator_hb1 > 0 or noise_indicator_hb2 > 0:
        print(f"Index {index} - HB_1 Noise: {noise_indicator_hb1}, HB_2 Noise: {noise_indicator_hb2}")

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

output_file_path = "drift_detection_adwin.csv"
output_df.to_csv(output_file_path, index=False)

print(f"Drift detection results saved to {output_file_path}")