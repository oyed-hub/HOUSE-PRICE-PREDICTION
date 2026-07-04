# 🏠 House Price Prediction using Machine Learning

A complete end-to-end Machine Learning project that predicts house prices based on property features such as area, number of bedrooms, bathrooms, parking availability, and furnishing status. The project includes data preprocessing, model training, evaluation, and deployment using Streamlit.

---

## 📌 Project Overview

This application uses Machine Learning to estimate the selling price of a house. Users can enter house details through a simple web interface, and the trained model predicts the estimated price instantly.

The project demonstrates the complete Machine Learning workflow, from loading and preprocessing data to deploying a trained model as a web application.

---

## 🚀 Features

* Predict house prices based on user inputs
* Clean and interactive Streamlit interface
* Data preprocessing and categorical encoding
* Exploratory Data Analysis (EDA)
* Data visualization
* Multiple Machine Learning model comparison
* Automatic best model selection
* Saved trained model using Joblib
* Real-time prediction using a deployed model

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

### Machine Learning Algorithms

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
HOUSE-PRICE-PREDICTION/
│
├── data/
│   ├── Housing.csv
│   └── processed_housing.csv
│
├── models/
│   ├── best_model.pkl
│   └── house_price_model.pkl
│
├── src/
│   ├── load_data.py
│   ├── eda.py
│   ├── visualization.py
│   ├── preprocess.py
│   ├── train.py
│   ├── model_comparison.py
│   ├── predict.py
│   └── feature_importance.py
│
├── screenshots/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Machine Learning Workflow

1. Load Dataset
2. Perform Exploratory Data Analysis (EDA)
3. Visualize the Data
4. Preprocess the Dataset
5. Encode Categorical Features
6. Split Data into Training and Testing Sets
7. Train Multiple Machine Learning Models
8. Evaluate Model Performance
9. Save the Best Model
10. Deploy with Streamlit

---

## 📈 Evaluation Metrics

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The best-performing model is saved as:

```text
models/best_model.pkl
```

---

## 🖥️ Streamlit Application

The application allows users to:

* Enter property details
* Predict house price instantly
* View prediction results in a user-friendly interface

Run the application using:

```bash
streamlit run app.py
```

---



## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/oyed-hub/HOUSE-PRICE-PREDICTION.git
```

Navigate to the project:

```bash
cd HOUSE-PRICE-PREDICTION
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* Hyperparameter tuning
* XGBoost implementation
* LightGBM implementation
* CatBoost implementation
* Feature importance visualization
* Interactive charts
* Downloadable prediction reports
* Cloud deployment
* REST API integration

---

## 👨‍💻 Author

**Madhu**

* GitHub: https://github.com/oyed-hub

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
