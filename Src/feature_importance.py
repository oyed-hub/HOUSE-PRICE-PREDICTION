import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("models/best_model.pkl")

data = pd.read_csv("data/processed_housing.csv")

X = data.drop("price", axis=1)

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance)

plt.figure(figsize=(10,6))
plt.bar(feature_importance["Feature"],
        feature_importance["Importance"])

plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.show()