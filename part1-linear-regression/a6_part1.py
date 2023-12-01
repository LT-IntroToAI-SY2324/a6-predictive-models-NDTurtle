import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")

# Extract the features (independent variable) and target (dependent variable)
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1, 1)

# Create the linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Find the coefficient, bias, and r squared values.
coef = round(model.coef_[0], 2)
bias = round(model.intercept_, 2)
r_squared = round(model.score(x, y), 2)

# Print out the linear equation and r squared value
print(f"Linear Equation: Blood Pressure = {coef}*Age + {bias}")
print(f"R-squared Value: {r_squared}")

# Predict the blood pressure of someone who is 43 years old.
prediction_43_years_old = model.predict([[43]])[0]
print(f"Predicted Blood Pressure for 43-year-old: {round(prediction_43_years_old, 2)}")

# Create the model in matplotlib and include the line of best fit
plt.scatter(x, y, label="Data Points")
plt.plot(x, model.predict(x), color='red', label="Line of Best Fit")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Linear Regression: Age vs. Blood Pressure")
plt.legend()
plt.show()
