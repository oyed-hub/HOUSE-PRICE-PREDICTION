import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ------------------------------
# Load Dataset
# ------------------------------

data = pd.read_csv("data/processed_housing.csv")

# ------------------------------
# Features and Target
# ------------------------------

X = data.drop("price", axis=1)
y = data["price"]

# ------------------------------
# Split Dataset
# ------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ------------------------------
# Models
# ------------------------------

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}

results = []

best_model = None
best_score = -1

print("=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": name,
        "MAE": round(mae, 2),
        "RMSE": round(rmse, 2),
        "R2 Score": round(r2, 4)
    })

    print(f"\n{name}")
    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²   : {r2:.4f}")

    if r2 > best_score:
        best_score = r2
        best_model = model

# ------------------------------
# Comparison Table
# ------------------------------

comparison = pd.DataFrame(results)

print("\n")
print("=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)
print(comparison)

# ------------------------------
# Save Best Model
# ------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/best_model.pkl")

print("\nBest model saved successfully!")