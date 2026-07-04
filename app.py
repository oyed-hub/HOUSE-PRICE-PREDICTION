import streamlit as st
import pandas as pd
import joblib

# ----------------------------------
# Load Trained Model
# ----------------------------------
model = joblib.load("models/best_model.pkl")

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict the price.")

# ----------------------------------
# User Inputs
# ----------------------------------

area = st.number_input("Area (Square Feet)", min_value=500, max_value=20000, value=1000)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

stories = st.number_input("Stories", min_value=1, max_value=5, value=2)

mainroad = st.selectbox("Main Road", ["Yes", "No"])

guestroom = st.selectbox("Guest Room", ["Yes", "No"])

basement = st.selectbox("Basement", ["Yes", "No"])

hotwater = st.selectbox("Hot Water Heating", ["Yes", "No"])

airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])

parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

furnishing = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

# ----------------------------------
# Convert Inputs
# ----------------------------------

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwater = 1 if hotwater == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

furnishing_map = {
    "Furnished": 0,
    "Semi-Furnished": 1,
    "Unfurnished": 2
}

furnishing = furnishing_map[furnishing]

# ----------------------------------
# Prediction
# ----------------------------------

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwater],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishing]
    })

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")