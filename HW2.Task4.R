knitr::opts_chunk$set(echo = TRUE)

# Load necessary libraries
if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

library(ggplot2)
library(dplyr)

lung_cancer_df <- read.csv("lung_cancer_prediction_dataset.csv")
air_pollution_df <- read.csv("global_air_pollution_dataset.csv")

lung_country_col <- grep("country", tolower(colnames(lung_cancer_df)), value = TRUE)
pollution_country_col <- grep("country", tolower(colnames(air_pollution_df)), value = TRUE)
aqi_column <- grep("pm2.5", tolower(colnames(air_pollution_df)), value = TRUE)
age_column <- grep("age", tolower(colnames(lung_cancer_df)), value = TRUE)
lung_cancer_column <- grep("lung_cancer", tolower(colnames(lung_cancer_df)), value = TRUE)

if (length(lung_country_col) == 0 || length(pollution_country_col) == 0) {
  stop("Country column not found in one or both datasets.")
}
if (length(aqi_column) == 0) {
  stop("PM2.5 AQI column not found in air pollution dataset.")
}
if (length(age_column) == 0) {
  stop("AGE column not found in lung cancer dataset.")
}
if (length(lung_cancer_column) == 0) {
  stop("LUNG_CANCER column not found in lung cancer dataset.")
}

lung_cancer_df[[lung_country_col]] <- as.character(lung_cancer_df[[lung_country_col]])
air_pollution_df[[pollution_country_col]] <- as.character(air_pollution_df[[pollution_country_col]])

merged_df <- merge(
  lung_cancer_df,
  air_pollution_df,
  by.x = lung_country_col,
  by.y = pollution_country_col,
  all = TRUE
)

if (nrow(merged_df) == 0) {
  stop("Merge failed: Check for mismatched country names or missing data.")
}

ggplot(merged_df, aes(x = .data[[aqi_column]], y = .data[[age_column]], color = factor(.data[[lung_cancer_column]]))) +
  geom_point(size = 3, alpha = 0.7) +
  scale_color_manual(values = c("0" = "blue", "1" = "red"), labels = c("No", "Yes")) +
  labs(
    title = "Lung Cancer Incidence vs. PM2.5 AQI Values",
    x = "PM2.5 AQI Value",
    y = "Age",
    color = "Lung Cancer Diagnosis"
  ) +
  theme_minimal()


# 2. Aggregated Lung Cancer Cases by Country (Scatter Plot with Categorical Coloring)

# Aggregate data
country_stats <- lung_cancer_df %>%
  group_by(COUNTRY) %>%
  summarise(
    cancer_cases = sum(LUNG_CANCER, na.rm = TRUE),
    average_age = mean(AGE, na.rm = TRUE)
  )

# Scatter plot
ggplot(country_stats, aes(x = cancer_cases, y = average_age, color = COUNTRY)) +
  geom_point(size = 4) +
  labs(
    title = "Aggregated Lung Cancer Cases by Country",
    x = "Total Cancer Cases",
    y = "Average Age"
  ) +
  theme_minimal() +
  theme(legend.position = "bottom") +
  scale_color_viridis_d()

# 3. Age Distribution by Gender (Jitter Plot)

# Jitter plot
ggplot(lung_cancer_df, aes(x = GENDER, y = AGE, color = GENDER)) +
  geom_jitter(width = 0.2, size = 3) +
  scale_color_manual(values = c("M" = "#5469f1", "F" = "#d554f1")) +
  labs(
    title = "Age Distribution by Gender",
    x = "Gender",
    y = "Age"
  ) +
  theme_minimal()

# 4. AQI Category Distribution (Bar Plot with Viridis Color Scale)

# Bar plot for AQI categories
ggplot(air_pollution_df, aes(x = AQI.Category, fill = AQI.Category)) +
  geom_bar() +
  scale_fill_viridis_d(option = "plasma") +
  labs(
    title = "AQI Category Distribution",
    x = "AQI Category",
    y = "Frequency"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

