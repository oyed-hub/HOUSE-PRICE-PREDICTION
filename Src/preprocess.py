import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("data/Housing.csv")

print("Original Dataset")
print(data.head())

# ---------------------------------------
# Create Label Encoder
# ---------------------------------------
encoder = LabelEncoder()

# ---------------------------------------
# Find all categorical columns
# ---------------------------------------
categorical_columns = data.select_dtypes(include=['object']).columns

print("\nCategorical Columns:")
print(categorical_columns)

# ---------------------------------------
# Convert text into numbers
# ---------------------------------------
for column in categorical_columns:
    data[column] = encoder.fit_transform(data[column])

print("\nDataset After Encoding")
print(data.head())

# ---------------------------------------
# Save processed dataset
# ---------------------------------------
data.to_csv("data/processed_housing.csv", index=False)

print("\nProcessed dataset saved successfully!")