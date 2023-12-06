# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The r squared coefficient is 0.85. This means that a larger proportion of the variance in the dependent variable (the target) can be explained by the independent variables (the features) in the model
2. Is your model accurate? Why or why not?
It's decently accurate, the predicted price is usually pretty close to the actual price. 
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
10 year old car: $8983.56
20 year old car: $1912.18
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
The model is going beyond the constraints of the data set. 