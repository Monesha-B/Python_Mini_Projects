# suppose only people with height 120 and above are aloowed to go on a roller coaster.

height = int(input("Enter your height: "))

if height >= 120:
    print("You can ride the roller coaster")
    # assigned different cost of the each age catagories
    age = int(input("Enter your age: "))
    if age <12:
        print("you should pay $5.")
    elif age >= 18: # elif age <= 18: and print as $7
        print("you should pay $12")
    else:
        print("you should pay $7.")        
else:
    print("Sorry, you have to grow taller bfore you can ride")    