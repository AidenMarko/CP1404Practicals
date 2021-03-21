"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sale_amount = 0
while sale_amount >= 0:
    sale_amount = float(input("Sale amount: "))
    if sale_amount <= 0:
        print("Invalid option")
    elif sale_amount < 1000:
        bonus = 0.1
        print("Bonus: {}".format(sale_amount * 0.1))
    elif sale_amount >= 1000:
        bonus = 0.15
        print("Bonus: {}".format(sale_amount * bonus))
