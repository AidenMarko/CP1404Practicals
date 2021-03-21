"""
CP1404/CP5632 - Practical
Item Price Calculator - Do From Scratch Exercise
"""

choice = int(input("Number of items: >>> "))
total_cost = 0
while choice <= 0:
    print("Invalid number of items!")
    choice = int(input("Number of items: >>> "))
for i in range(0, choice, 1):
    print("Price of item: ", end="")
    item_cost = float(input(">>> "))
    total_cost += item_cost
if total_cost > 100:
    total_cost = total_cost * 0.9
print("Total Price for {} item is ${:.2f}".format(choice, total_cost))
