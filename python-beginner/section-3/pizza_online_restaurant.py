print("----------------------------------------")
print("---Welcome to Python Pizza Deliveries---")
print("----------------------------------------\n")

size = input("What size pizza do you want? S, M or L:\n").upper()
pizza_type = input("Which pizza do you want? Marguerita or Meat Lovers?\n")
extra_pepperoni = input("Want to add pepperoni on your pizza? Y or N:\n").upper()
extra_cheese = input("Want to add extra cheese on your pizza? Y or N:\n").upper()

total_cost = 0

if size == "S":
    total_cost += 15
elif size == "M":
    total_cost += 20
else:
    total_cost += 25

if extra_cheese == "Y":
    total_cost += 1

if extra_pepperoni == "Y":
    if size == "S":
        total_cost += 2
    else:
        total_cost += 3

print(f"Total of your {pizza_type} pizza, size {size} is ${round(total_cost, 2)}")
