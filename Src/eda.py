import pandas as pd

# Load the dataset
data = pd.read_csv("data/Housing.csv")

# -------------------------------
# Display Basic Information
# -------------------------------

print("=" * 60)
print("HOUSE PRICE DATASET")
print("=" * 60)

# First 5 rows
print("\nFirst 5 Rows")
print(data.head())

# Last 5 rows
print("\nLast 5 Rows")
print(data.tail())

# Shape
print("\nShape of Dataset")
print(data.shape)

# Column Names
print("\nColumn Names")
print(data.columns.tolist())

# Data Types
print("\nData Types")
print(data.dtypes)

# Dataset Information
print("\nDataset Information")
data.info()

# Missing Values
print("\nMissing Values")
print(data.isnull().sum())

# Statistical Summary
print("\nStatistical Summary")
print(data.describe())