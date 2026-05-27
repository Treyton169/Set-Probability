import random

# This function calculates the possibility (or percentage of occurances) of a target number appearing in a given set (list).
def possibility(set, target):
    total = len(set)
    num = set.count(target)
    
    
    return f" Possibility is {(num/len(set)) * 100}%"

# Creating a random list and a random target number, you can remove this part if you want to input your own list and target.
lst = [] # If you want to add your own list add the values and remove lines 14-15.
i = 0 
for i in range(random.randint(10, 30)):
    lst.append(random.randint(1, 10))
x = random.randint(1, 10) # Change the variable value to find what you want. Instead of something random.

# Prints Results and Data
print(f"List: {lst}")
print(f"Target: {x}")
print(f"Count of Target in List: {lst.count(x)}")
print(f"Total numbers: {len(lst)}")
print(possibility(lst, x))