# Part 5 - Unsupervised Learning Writeup

After completing `a6_part5.py` answer the following questions

## Questions to answer

1. Develop a name for each customer group based on the information from the graph. For example, one group might be called “Frugal” while another might be called “Shopaholic.” Explain your reasoning for each label.
Frugal Low Income: someone who doesn't have a lot of money and doesn't spend much (spending score range: -2.0 to -1.0, income: -2 to -1)
Frugal Middle income: someone who has a medium income and doesn't spend much (spending score range: -2.0 to -1.0, income: -1 to 1)
Frugal High Income: someone who has a high income and doesn't spend much (spending score range: -2.0 to -1.0, income: 1+)
Consumer Low Income: someone who doesn't have a lot of money and spends a good amount (spending score range: -1.0 to 0.5, income: -2 to -1)
Consumer Middle Income: someone who has a medium income and spends a good amount (spending score range: -1.0 to 0.5, income: -1 to 1)
Consumer High Income: someoe who has a high income and spends a good amount (spending score range: -1.0 to 0.5, income: 1+)
Hyper Consumer Low Income: someone who has a low income and spends a lot (spending score range: 0.5+, income -2 to -1)
Hyper Consumer Middle Income: someone who has a medium income and spends a lot (spending score range: 0.5+, income -1 to 1)
Hyper Consumer High Income: someone who has a high income and spends a lot (spending score range: 0.5+, income 1+)
2. What group would a customer who has a medium income and low spending habits be in?
Frugal Middle income
3. Choose one cluster of interest to you. How might the marketing team approach this specific customer group?
A marketing team might advertise a credit card with a high interest rate to Hyper Consumer Low Income, to try to get them to rack up as much debt as possible. 
