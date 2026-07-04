import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/Housing.csv")

# -----------------------------
# 1. Area vs Price Scatter Plot
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["area"], data["price"])

plt.title("Area vs Price")
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price")

plt.show()

# -----------------------------
# 2. Price Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
plt.hist(data["price"], bins=20)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Houses")

plt.show()

# -----------------------------
# 3. Bedrooms Distribution
# -----------------------------
plt.figure(figsize=(6, 4))
data["bedrooms"].value_counts().plot(kind="bar")

plt.title("Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")

plt.show()

# -----------------------------
# 4. Box Plot for Price
# -----------------------------
plt.figure(figsize=(6, 4))
plt.boxplot(data["price"])

plt.title("Price Box Plot")

plt.show()