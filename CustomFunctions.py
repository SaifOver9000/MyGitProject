import statistics

def MedianCost(costs):
  """
  Calculates the median cost of a list of costs

  Arguments:
  costs (list)
  """
  try:
    medianCost = statistics.median(costs)
    return(f"The median cost per bag is ${medianCost}")
  except ValueError as e:
    return(f"Error calculating median cost: {e}. Please ensure the costs list is not empty and contains valid numbers.")

def MinCost(costs):
  """
  Calculates the min cost from a list of costs

  Arguments:
  costs (list)
  """
  try:
    minCost = min(costs)
    return(f"The minimum cost per bag is ${minCost}")
  except ValueError as e:
    return(f"Error calculating minimum cost: {e}. Please ensure the costs list is not empty and contains valid numbers.")

def MaxCost(costs):
  """
  Calculates the max cost from a list of costs

  Arguments:
  costs (list)
  """
  try:
    maxCost = max(costs)
    return(f"The maximum cost per bag is ${maxCost}")
  except ValueError as e:
    return(f"Error calculating maximum cost: {e}. Please ensure the costs list is not empty and contains valid numbers.")

def MostExpensive(costs, names):
  """
  Finds the name of the most expensive item

  Arguments:
  costs (list), names (list)
  """
  try:
    mostExpensive = names[costs.index(max(costs))]
    return(f"The most expensive bag is {mostExpensive}")
  except Exception as e:
    return(f"Error finding most expensive bag: {e}. Please ensure the costs and names lists are not empty and have the same length.")

def MostExpensivePerGram(costs, names, weights):
  """
  Finds the name of the most expensive item per gram

  Arguments:
  costs (list), names (list), weights (list)
  """
  #pricePerHundred
  pPH = []
  for i in range(len(names)):
    pPH.append((weights[i]/costs[i])*100)
  mostExpensivePerGram = names[pPH.index(max(pPH))]
  return(f"The most expensive bag per gram is {mostExpensivePerGram}")


def TotalCost(costs):
  """
  Calculates the total cost of a list of costs

  Arguments:
  costs (list)
  """
  try:
    totalCost = sum(costs)
    return(f"The total cost of all the bags is ${totalCost}")
  except ValueError as e:
    return(f"Error calculating total cost: {e}. Please ensure the costs list contains valid numbers.")


def TotalWeight(weights):
  """
  Calculates the total weight of a list of weights

  Arguments:
  weights (list)
  """
  try:
    totalWeight = sum(weights)
    return(f"The total weight of all the bags is {totalWeight} grams")
  except ValueError as e:
    return(f"Error calculating total weight: {e}. Please ensure the weights list contains valid numbers.")

def OverallCostPer100Grams(costs, weights):
  """
  Calculates the overall cost per 100 grams of a list of costs and weights

  Arguments:
  costs (list), weights (list)
  """
  try:
    totalCost = sum(costs)
    totalWeight = sum(weights)
    costPer100Grams = (totalCost/totalWeight)*100
    return(f"The overall cost per 100 grams is ${costPer100Grams}")
  except ValueError as e:
    return(f"Error calculating overall cost per 100 grams: {e}. Please ensure the costs and weights lists contain valid numbers.")
  
def MeanCost(costs):
  """
  Calculates the mean cost of a list of costs

  Arguments:
  costs (list)
  """
  try:
    meanCost = statistics.mean(costs)
    return(f"The mean cost per bag is ${meanCost}")
  except ValueError as e:
    return(f"Error calculating mean cost: {e}. Please ensure the costs list is not empty and contains valid numbers.")  
  