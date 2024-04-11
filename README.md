# Eyestate

The following script loads and runs the eeg dataset which also looks at eye detection and accordingly creates a heatmap, correlates the different EEG nodes with the eye state (open or close) and also runs a machine learning model to predict the eye state using the eeg data

The correlation and p values values obtained for each node with the eye state are as follows - 

F7: Correlation Coefficient = -0.080, p-value = < 0.001
FC6: Correlation Coefficient = 0.064, p-value = < 0.001
F4: Correlation Coefficient = 0.048, p-value = < 0.001
T8: Correlation Coefficient = 0.047, p-value = < 0.001
F3: Correlation Coefficient = 0.039, p-value = < 0.001
O2: Correlation Coefficient = 0.025, p-value = 0.002
F8: Correlation Coefficient = 0.013, p-value = 0.108
AF3: Correlation Coefficient = 0.010, p-value = 0.201
P8: Correlation Coefficient = 0.010, p-value = 0.241
P7: Correlation Coefficient = -0.008, p-value = 0.337
AF4: Correlation Coefficient = -0.008, p-value = 0.356
FC5: Correlation Coefficient = -0.008, p-value = 0.357
O1: Correlation Coefficient = -0.007, p-value = 0.377
T7: Correlation Coefficient = -0.000, p-value = 0.964


## The Heatmap of the Correlation Coefficients

![image](https://github.com/shannferns/Eyestate/assets/64725637/40b42145-c2d5-4116-a84d-6342aa6b5322)
