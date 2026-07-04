import joblib
import pandas as pd

# ----------------------------
# Load the Best Model
# ----------------------------
model = joblib.load("models/best_model.pkl")

# ----------------------------
# Sample House Details
# ----------------------------
house = {
    "area": [7500],
    "bedrooms": [4],
    "bathrooms": [2],
    "stories": [2],
    "mainroad": [1],
    "guestroom": [0],
    "basement": [1],
    "hotwaterheating": [0],
    "airconditioning": [1],
    "parking": [2],
    "prefarea": [1],
    "furnishingstatus": [0]
}

# Convert dictionary to DataFrame
house_df = pd.DataFrame(house)

# ----------------------------
# Predict House Price
# ----------------------------
predicted_price = model.predict(house_df)

print("=" * 50)
print("HOUSE PRICE PREDICTION")
print("=" * 50)
print(f"Predicted Price: ₹ {predicted_price[0]:,.2f}")