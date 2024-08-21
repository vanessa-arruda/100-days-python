print("-----------------------------------")
print("---Welcome to the Tip Calculator---")
print("-----------------------------------\n")


def calculate_tip(bill_total: float, tip: int, split_amount: int):
    return (bill_total + (bill_total * (tip / 100))) / split_amount


bill_total = float(input("What is the total bill?\n"))
tip_percentage = int(
    input("How much tip would you like to give? 10, 12, 15, 17, 20?\n")
)
split_amount = int(input("How many people to split the bill?\n"))

print(
    f"\nEach person should pay: ${round(calculate_tip(bill_total, tip_percentage, split_amount), 2)}"
)
