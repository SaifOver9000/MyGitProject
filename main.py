"""
Here we will run the functions created in CustonFunctions.py
We wil also test the thing here
"""
import CustomFunctions

costs = []
weights = []
names = []
done = ""

#main stuff
while done.lower() != 'y':
    names.append(input("What is the name of the item in letters?: "))
    while True:
        try:
            cost = float(input("What is the cost of the item in dollars?: "))
            costs.append(cost)
            break
        except ValueError:
            print("Please enter a valid number for the cost.")
    while True:
        try:
            weight = float(input("What is the weight of the item in grams?: "))
            weights.append(weight)
            break
        except ValueError:
            print("Please enter a valid number for the weight.")
    done = input("Are you done? (Y/n): ")

print(CustomFunctions.TotalCost(costs))
print(CustomFunctions.TotalWeight(weights))
print(CustomFunctions.OverallCostPer100Grams(costs,weights))
print(CustomFunctions.MeanCost(costs))
print(CustomFunctions.MedianCost(costs))
print(CustomFunctions.MinCost(costs))
print(CustomFunctions.MaxCost(costs))
print(CustomFunctions.MostExpensive(costs,names))
print(CustomFunctions.MostExpensivePerGram(costs,names,weights))

