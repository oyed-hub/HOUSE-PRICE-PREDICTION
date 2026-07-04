import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ------------------------------------
# Load Dataset
# ------------------------------------

data = pd.read_csv("data/processed_housing.csv")

# ------------------------------------
# Features and Target
# ------------------------------------

X = data.drop("price", axis=1)
y = data["price"]

# ------------------------------------
# Split Dataset
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ------------------------------------
# Train Model
# ------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

print("Model trained successfully!")

# ------------------------------------
# Predictions
# ------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------
# Evaluation
# ------------------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("MODEL EVALUATION")
print("==============================")

print(f"MAE : {mae:.2f}")
print(f"MSE : {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# ------------------------------------
# Actual vs Predicted
# ------------------------------------

results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\nActual vs Predicted")
print(results.head(10))

# ------------------------------------
# Save Model
# ------------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/house_price_model.pkl")

print("\nModel saved successfully!")