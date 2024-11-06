This repository implements five popular drift detection methods using the Frouros library. These methods—ADWIN, Page-Hinkley, CUSUM, PCA, and KL Divergence—are designed to monitor data streams for shifts in distribution, indicating potential changes in the underlying process generating the data. This can be especially useful in fields like EEG signal analysis, anomaly detection, and time-series forecasting.

Installation

To use these scripts, install the necessary dependencies: 

pip install frouros pandas matplotlib scipy

Usage

Each method is implemented in a separate script and can be run individually. Each script reads an input CSV file containing data streams (e.g., EEG data) and applies the corresponding drift detection method.

	•	Input Data: Ensure your input CSV file has the columns HB_1, HB_2, time, and seq_id for consistency.
	•	Run the Scripts: Execute each script individually to detect drift using the specified method.

Methods

ADWIN (Adaptive Windowing)

ADWIN is an adaptive sliding window method that dynamically adjusts its window size based on observed changes in the mean of the data stream. It splits the window into two sub-windows and performs a statistical test to check if the mean has shifted significantly. If a drift is detected, ADWIN shrinks the window to exclude the older data, adapting to the new distribution.

	•	Noise Detection Mechanism: ADWIN detects noise by identifying significant shifts in the mean of the data stream. When a shift is detected, ADWIN adjusts the window size, which is helpful for detecting both abrupt and gradual changes in data.
	•	Output: A binary output, with 0 indicating no drift and 1 indicating drift.

Page-Hinkley Test

The Page-Hinkley test monitors cumulative deviations from the mean and flags drift when these deviations consistently surpass a predefined threshold. This method is particularly effective for gradual changes rather than sudden shifts, as it accumulates evidence over time before declaring drift.

	•	Noise Detection Mechanism: Page-Hinkley tracks deviations from the running average and triggers drift if these deviations consistently exceed a threshold, indicating a gradual change in data distribution.
	•	Output: A binary output, with 0 indicating no drift and 1 indicating drift.

CUSUM (Cumulative Sum Control)

CUSUM is a sequential analysis method that accumulates deviations from a target mean value and signals drift when these cumulative deviations exceed a specified threshold. CUSUM is effective at detecting abrupt changes in the mean of the data, as it continuously monitors for sustained shifts away from the baseline.

	•	Noise Detection Mechanism: CUSUM accumulates the difference between observed values and the expected mean. When the cumulative deviation exceeds the threshold, drift is signaled.
	•	Output: A binary output, with 0 indicating no drift and 1 indicating drift.

PCA (Principal Component Analysis)

PCA reduces the data to its principal components, capturing the directions of maximum variance. By monitoring changes in the variance structure of the principal components, PCA can detect changes in the underlying distribution of the data. It flags drift if there are significant deviations in the variance explained by the principal components.

	•	Noise Detection Mechanism: PCA detects drift by analyzing the variance explained by principal components over time. A significant change in this variance indicates that the data structure has shifted, signaling drift.
	•	Output: A binary output, with 0 indicating no drift and 1 indicating drift.

KL Divergence (Kullback-Leibler Divergence)

KL Divergence is a method to measure the divergence between two probability distributions. In drift detection, KL Divergence is calculated between two consecutive windows of data. If the divergence exceeds a threshold, it indicates that the probability distribution of the data has changed significantly, signaling drift.

	•	Noise Detection Mechanism: KL Divergence compares the probability distributions of two consecutive data windows. A high divergence value indicates a change in distribution, signaling drift.
	•	Output: A binary output, with 0 indicating no drift and 1 indicating drift.

Each method has been implemented to give binary outputs for each time step: 0 for no drift detected, and 1 for drift detected. This makes it easy to integrate these methods into other systems for real-time monitoring and alerting.

Example

For each method, the code follows a similar structure:

	1.	Load the input CSV data.
	2.	Apply the drift detection method.
	3.	Output the results, with noise detection markers at significant changes in the signal.

Important: this methods work for a specific dataset containing EEG signals from BitBrain
