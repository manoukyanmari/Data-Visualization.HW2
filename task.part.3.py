import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
lung_cancer_df = pd.read_csv('lung_cancer_prediction_dataset.csv')
air_pollution_df = pd.read_csv('global_air_pollution_dataset.csv')

# Check available columns to ensure correct column names
print("Lung Cancer Dataset Columns:", lung_cancer_df.columns)

# Use the correct column name for LUNG_CANCER if different
lung_cancer_column = 'LUNG_CANCER' if 'LUNG_CANCER' in lung_cancer_df.columns else lung_cancer_df.columns[0]

# 1. Boxplot of Lung Cancer Deaths Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=lung_cancer_df, x=lung_cancer_column)
plt.title('Boxplot of Lung Cancer Deaths Distribution')
plt.xlabel('Lung Cancer Diagnosis (1 = Yes, 0 = No)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Histogram of PM2.5 AQI Values
plt.figure(figsize=(10, 6))
pm25_values = air_pollution_df['PM2.5 AQI Value'].dropna()
plt.hist(pm25_values, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of PM2.5 AQI Values')
plt.xlabel('PM2.5 AQI Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 3. Density Plot of Lung Cancer Mortality Rate
# Assuming 'AGE' correlates with mortality (replace if there's a better column)
plt.figure(figsize=(10, 6))
sns.kdeplot(data=lung_cancer_df[lung_cancer_df[lung_cancer_column] == 1], x='AGE', shade=True, color='red', label='Cancer Patients')
sns.kdeplot(data=lung_cancer_df[lung_cancer_df[lung_cancer_column] == 0], x='AGE', shade=True, color='blue', label='Non-Cancer Patients')
plt.title('Density Plot of Lung Cancer Mortality Rate by Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()