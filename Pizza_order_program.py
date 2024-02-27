# Instructions

# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N: ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N

Small_pizza_cost = 15
Medium_pizza_cost = 20
Large_pizza_cost = 25
Pepperoni_cost_for_small = 2
Pepperoni_cost_for_med_or_large = 3
cheese_cost = 1

if size == 'S' and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${Small_pizza_cost+Pepperoni_cost_for_small+cheese_cost}.")
elif size == 'S' and add_pepperoni == "N" and extra_cheese == "Y":  
    print(f"Your final bill is: ${Small_pizza_cost+cheese_cost}.")
elif size == 'S' and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${Small_pizza_cost+Pepperoni_cost_for_small}.")
elif size == 'S' and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${Small_pizza_cost}.")

if size == 'M' and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${Medium_pizza_cost+Pepperoni_cost_for_med_or_large+cheese_cost}.")
elif size == 'M' and add_pepperoni == "N" and extra_cheese == "Y":  
    print(f"Your final bill is: ${Medium_pizza_cost+cheese_cost}.")
elif size == 'M' and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${Medium_pizza_cost+Pepperoni_cost_for_med_or_large}.")
elif size == 'M' and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${Medium_pizza_cost}.")

if size == 'L' and add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${Large_pizza_cost+Pepperoni_cost_for_med_or_large+cheese_cost}.")
elif size == 'L' and add_pepperoni == "N" and extra_cheese == "Y":  
    print(f"Your final bill is: ${Large_pizza_cost+cheese_cost}.")
elif size == 'L' and add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${Large_pizza_cost+Pepperoni_cost_for_med_or_large}.")
elif size == 'L' and add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${Large_pizza_cost}.")


# if size == 'L':
#   if add_pepperoni == "Y":
#     if extra_cheese == "Y":
#       print(f"Your final bill is: ${Large_pizza_cost+Pepperoni_cost_for_med_or_large+cheese_cost}.")
#     else:
#       print(f"Your final bill is: ${Large_pizza_cost+Pepperoni_cost_for_med_or_large}.")
#   else:
#     print(f"Your final bill is: ${Large_pizza_cost}.")    


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.")

    
    
    
