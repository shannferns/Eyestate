from scipy.io import arff
import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
import seaborn as sns

data = arff.loadarff('EEG Eye State.arff')
df = pd.DataFrame(data[0])

df.head()

corr_matrix = data.corr()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="crest", fmt=".2f", square=True)
plt.title("Correlation Heatmap")
plt.show()

# correlation coefficients and p-values
correlation_results = []
for column in data.columns:
    if column != "eyeDetection":
        corr_coef, p_value = pearsonr(data[column], data["eyeDetection"])
        correlation_results.append((column, corr_coef, p_value))

correlation_results.sort(key=lambda x: x[2])

for column, corr_coef, p_value in correlation_results:
    if p_value < 0.001:
        p_value_str = "< 0.001"
    else:
        p_value_str = format(p_value, ".3f")
    print(f"{column}: Correlation Coefficient = {corr_coef:.3f}, p-value = {p_value_str}")

