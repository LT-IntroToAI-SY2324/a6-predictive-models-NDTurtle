import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(x)
print(y)
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler()
# Step 3: Transform the data
x = scaler.fit_transform(x)
# Step 4: Split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
# Step 5: Fit the data

# Step 6: Create a LogsiticRegression object and fit the data
logreg = linear_model.LogisticRegression()
logreg.fit(xtrain, ytrain)
# Step 7: Print the score to see the accuracy of the model
accuracy = logreg.score(xtest, ytest)
print("\nAccuracy of the model:", accuracy)

# Step 8: Print out the actual ytest values and predicted y values based on the xtest data
y_pred = logreg.predict(xtest)
print("\nActual ytest values:")
print(ytest)
print("\nPredicted y values based on xtest:")
print(y_pred)

# 34 year old female data point
new_data_point = [[34, 56000, 1]]  # Assuming 1 represents Female

# Scaling it
scaled_new_data_point = scaler.transform(new_data_point)

# Make prediction using model
prediction = logreg.predict(scaled_new_data_point)

# Print the prediction
print("Prediction:", prediction)
