import math
from datetime import datetime

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10_000_000_000

print(f"\nThe approximate volume is {v:.2f} liters")

while True:
    wants_to_buy = input("Do you want to buy a tire with the dimensions you entered? (y/n) ")
    if wants_to_buy == "y":
        phone_number = input("Please enter your phone number: ")
        break
    elif wants_to_buy == "n":
        break
    else:
        print("Invalid input. Please try again.")

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    if wants_to_buy == "y":
        print(f"{current_date_and_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=volumes_file)
    else:
        print(f"{current_date_and_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_file)