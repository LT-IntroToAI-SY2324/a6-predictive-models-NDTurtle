import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

# Load the dataset
data = pd.read_csv("part2-training-testing-data/chirping_data.csv")

# Extract the features (independent variable) and target (dependent variable)
x = data["Age"].values
y = data["Blood Pressure"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1, 1)

# Create the model
model = LinearRegression()

# Fit the model to the training data
model.fit(xtrain, ytrain)

# Find the coefficient, bias, and r squared values.
coef = round(model.coef_[0], 2)
bias = round(model.intercept_, 2)
r_squared = round(model.score(xtrain, ytrain), 2)

# Print out the linear equation and r squared value:
print(f"Linear Equation: Blood Pressure = {coef}*Age + {bias}")
print(f"R-squared Value: {r_squared}")

'''
**********TEST THE MODEL**********
'''

# Reshape the xtest data into a 2D array
xtest = xtest.reshape(-1, 1)

# Get the predicted y values for the xtest values - returns an array of the results
predictions = model.predict(xtest)

# Round the values in the np array to 2 decimal places
predictions = np.round(predictions, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for i in range(len(xtest)):
    print(f"Age: {xtest[i][0]}, Actual Blood Pressure: {ytest[i]}, Predicted Blood Pressure: {predictions[i]}")

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''

# Create a scatter plot of the test data points
plt.scatter(xtest, ytest, label="Actual Data Points")

# Plot the line of best fit using the model's predictions
plt.plot(xtest, predictions, color='red', label="Line of Best Fit")

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Linear Regression: Age vs. Blood Pressure")
plt.legend()
plt.show()
