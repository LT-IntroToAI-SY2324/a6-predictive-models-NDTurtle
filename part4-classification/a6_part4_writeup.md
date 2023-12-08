# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
It becomes completely wrong, and the predicted y values are all 0. This is because the StandardScaler puts the measurements on a common scale, and removing it leads to problems with data interpretation and inaccurate predictions. 
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
It's fairly accurate, with an 89% accuracy level compared to 60% without the scaler. This is accurate enough for the use case, as predicting if someone will buy an SUV doesn't require 100% accuracy, just enough to help with sales or whatever a model like this would be used for.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
It did well. When it was incorrect, it seemed to be when it was predicting that someone would buy an SUV, but rarely when someone wouldn't buy an SUV.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
The model predicts NO
