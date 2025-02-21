knitr::opts_chunk$set(echo = TRUE)

# Load necessary libraries
if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

# Load necessary libraries
library(ggplot2)
library(dplyr)

# Load datasets using base R functions
lung_cancer_df <- read.csv('lung_cancer_prediction_dataset.csv')
air_pollution_df <- read.csv('global_air_pollution_dataset.csv')

# Boxplot of Lung Cancer Deaths Distribution
ggplot(lung_cancer_df, aes(x = factor(Level))) +
  geom_boxplot(fill = 'lightblue') +
  ggtitle('Lung Cancer Deaths Distribution') +
  xlab('Cancer Diagnosis Level') +
  theme_minimal()

# Scatter Plot with Random Values
set.seed(42)
normal_values <- rnorm(100)
logistic_values <- rlogis(100)
random_data <- data.frame(normal_values, logistic_values)

ggplot(random_data, aes(x = normal_values, y = logistic_values)) +
  geom_point(color = 'brown') +
  ggtitle('Random Scatter Plot (Normal vs Logistic)') +
  xlab('Normal Distribution Values') +
  ylab('Logistic Distribution Values') +
  theme_solarized(light = FALSE)


