"""
Here we will run the functions created in CustonFunctions.py
We wil also test the thing here
"""
import CustomFunctions.py

costs = []
weights = []
names = []
done = ""

#main stuff
while done != "y" or done != "Y":
    names.append(input("What is the name of the item in letters?: "))
    costs.append(float(input("What is the cost of the item in dollars?: ")))
    weights.append(float(input("What is the weight of the item in grams?: ")))
    done = input("Are you done? (Y/n): ")

TotalCost(costs)
TotalWeight(weights)
OverallCostPer100Grams(costs,weights)
MeanCost(costs)
MedianCost(costs)
MinCost(costs)
MaxCost(costs)
MostExpensive(costs,names)
MostExpensivePerGram(costs,names,weights)
