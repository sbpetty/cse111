"""
You work for a retail store that wants to increase sales on Tuesday and 
Wednesday, which are the store’s slowest sales days. On Tuesday and 
Wednesday, if a customer’s subtotal is $50 or greater, the store will 
discount the customer’s subtotal by 10%.
"""

from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

subtotal = 0

while True:
    price = float(input("Please enter a price (0 when done): "))
    if price == 0:
        break
    quantity = float(input("Please enter a quantity: "))
    subtotal += price * quantity

print(f"Subtotal: {subtotal}")
discount = 0.0

if day_of_week in [1, 2]:
    if subtotal >= 50.00:
        discount = round(subtotal * 0.1, 2)
        print(f"Discount amount: {discount:.2f}")
    else:
        print(f"Additional amount needed to receive discount: {50.00 - subtotal}")

subtotal -= discount
sales_tax = round(subtotal * 0.06, 2)

print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:.2f}")