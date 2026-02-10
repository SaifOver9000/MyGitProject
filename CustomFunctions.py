#contains our custom functions
bags_size = []
bags_cost = []
product_names = []
highest_expensiveitem_pergram = []
most_expensiveitme_pergram = []
go = True
while (go):
  ans = input("Do you want to input data? (say 'yes' to contuine and 'done' to stop):")
  if ans == "yes":
    bag_size = float(input("What is the size of the bag of vegitable purchased in grams?"))
    bags_size.append(bag_size)
    bag_cost = float(input("What is the cost of the bag of vegitable purchesd"))
    bags_cost.append(bag_cost)
    product_name = float(input("What is the name of the product?"))
    product_names.append(product_name)
    cost_per_100g = (bag_cost/ bag_size)*100
    print(f"{product_name}  costs per 100g is ${cost_per_100g:.3f}/100 grams")
    go = True
  elif ans == "done":
    go = False
  else:
    print("Please write the correct ans")

import statistics

if len(bags_cost)>0:
  overall_cost = sum(bags_cost)
  print(overall_cost)
  overall_cost_per_100g = (overall_cost/ overall_weight)*100
  print(overall_cost_per_100g)
  mean_cost_perbag = (overall_cost)/len(bags_cost)
  print(mean_cost_perbag)
else:
  print("havent entered anything")
