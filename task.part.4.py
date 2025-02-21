import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
lung_cancer_df = pd.read_csv("lung_cancer_prediction_dataset.csv")
air_pollution_df = pd.read_csv("global_air_pollution_dataset.csv")

# Dynamically detect the country columns
lung_country_col = next((col for col in lung_cancer_df.columns if 'country' in col.lower()), None)
pollution_country_col = next((col for col in air_pollution_df.columns if 'country' in col.lower()), None)

# Dynamically detect AQI, age, and lung cancer diagnosis columns
aqi_column = next((col for col in air_pollution_df.columns if 'pm2.5' in col.lower()), None)
age_column = next((col for col in lung_cancer_df.columns if 'age' in col.lower()), None)
lung_cancer_column = next((col for col in lung_cancer_df.columns if 'lung_cancer' in col.lower()), None)

# Raise errors if columns are not found
if lung_country_col is None or pollution_country_col is None:
    raise ValueError("Country column not found in one of the datasets.")

if aqi_column is None:
    raise ValueError("PM2.5 AQI Value column not found in air pollution dataset.")

if age_column is None:
    raise ValueError("AGE column not found in lung cancer dataset.")

if lung_cancer_column is None:
    raise ValueError("LUNG_CANCER column not found in lung cancer dataset.")

# Convert both columns to strings for merging
lung_cancer_df[lung_country_col] = lung_cancer_df[lung_country_col].astype(str)
air_pollution_df[pollution_country_col] = air_pollution_df[pollution_country_col].astype(str)

# Merge datasets
merged_df = pd.merge(
    lung_cancer_df,
    air_pollution_df,
    left_on=lung_country_col,
    right_on=pollution_country_col,
    how='inner'
)

# Scatter Plot: Lung Cancer Incidence vs. PM2.5 AQI Values
plt.figure(figsize=(12, 7))
plt.scatter(
    merged_df[aqi_column],
    merged_df[age_column],
    c=merged_df[lung_cancer_column],
    cmap='coolwarm',
    edgecolor='black'
)
plt.title("Lung Cancer Incidence vs. PM2.5 AQI Values")
plt.xlabel("PM2.5 AQI Value")
plt.ylabel("Age")
plt.colorbar(label="Lung Cancer Diagnosis (0 = No, 1 = Yes)")
plt.grid(True)
plt.show()

# Aggregated Scatter Plot: Lung Cancer Cases by Country
country_stats = lung_cancer_df.groupby(lung_country_col).agg(
    cancer_cases=(lung_cancer_column, "sum"),
    average_age=(age_column, "mean")
).reset_index()

plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=country_stats,
    x="cancer_cases",
    y="average_age",
    hue=lung_country_col,
    palette="Set3",
    s=100,
    edgecolor="black"
)
plt.title("Aggregated Lung Cancer Cases by Country")
plt.xlabel("Total Cancer Cases")
plt.ylabel("Average Age")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.grid(True)
plt.show()

# Jitter Plot: Age Distribution by Gender
gender_column = next((col for col in lung_cancer_df.columns if 'gender' in col.lower()), None)
if gender_column is None:
    raise ValueError("Gender column not found in lung cancer dataset.")

plt.figure(figsize=(12, 7))
sns.stripplot(
    data=lung_cancer_df,
    x=gender_column,
    y=age_column,
    jitter=True,
    palette={"M": "#5469f1", "F": "#d554f1"}
)
plt.title("Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.grid(True)
plt.show()

# Bar Plot: AQI Category Distribution
aqi_category_column = next((col for col in air_pollution_df.columns if 'aqi.category' in col.lower()), None)
if aqi_category_column is None:
    raise ValueError("AQI Category column not found in air pollution dataset.")

plt.figure(figsize=(12, 7))
sns.countplot(
    data=air_pollution_df,
    x=aqi_category_column,
    palette="viridis"
)
plt.title("AQI Category Distribution")
plt.xlabel("AQI Category")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
