import pandas as pd
from sklearn.model_selection import train_test_split

# Load processed dataset
data = pd.read_csv("data/processed_housing.csv")

# ----------------------------------------
# Separate Features (X) and Target (y)
# ----------------------------------------

X = data.drop("price", axis=1)
y = data["price"]

print("=" * 60)
print("FEATURES (X)")
print("=" * 60)
print(X.head())

print("\nTARGET (y)")
print("=" * 60)
print(y.head())

# ----------------------------------------
# Split the dataset
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data Shape")
print(X_train.shape)

print("\nTesting Data Shape")
print(X_test.shape)