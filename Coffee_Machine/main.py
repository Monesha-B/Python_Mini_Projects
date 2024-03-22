# TODO program requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 750,
    "coffee": 350,
}


def resources_report():
    print(f"water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")


def coffee_machine():
    user_choice = input("What would you like? Espresso/latte/Cappuccino/Report: ").lower()
    print("Please insert coins.")

    def calculations():
        quarters = 0.25 * int(input("How many quarters?:"))
        dimes = 0.10 * int(input("How many dimes?:"))
        nickels = 0.05 * int(input("How many nickels?:"))
        pennies = 0.01 * int(input("How many pennies?:"))
        total = quarters + dimes + nickels + pennies
        change = total - MENU[user_choice]["cost"]
        # print(total)
        if total == MENU[user_choice]["cost"]:
            print("There is no change, you paid the exact amount.")
        elif total < MENU[user_choice]["cost"]:
            print("Amount is not sufficient")
        elif total > MENU[user_choice]["cost"]:
            print(f" Please collect your {round(change, 2)} change")

    def resources_calc(passing_resources):
        water_remain = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        resources["water"] = water_remain
        milk_remain = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
        resources["milk"] = milk_remain
        coffee_remain = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
        resources["coffee"] = coffee_remain
        # print(f"water: {resources["water"]}")
        # print(f"Milk: {resources["milk"]}")
        # print(f"Coffee: {resources["coffee"]}")

    def cap_latte():
        if MENU[user_choice]["ingredients"]["water"] <= resources["water"]:
            if MENU[user_choice]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[user_choice]["ingredients"]["coffee"] <= resources["coffee"]:
                    calculations()
                    print(f"Here is your {user_choice}. Enjoy!")
                    resources_calc()
                    coffee_machine()
                else:
                    print("Not enough ingredients available at the moment. Try again alter!")
            else:
                print("Not enough ingredients available at the moment. Try again alter!")
        else:
            print("Not enough ingredients available at the moment. Try again alter!")

    should_continue = False
    while not should_continue:
        if user_choice == "report":
            resources_report()
            coffee_machine()
        elif user_choice == "espresso":
            MENU[user_choice]["ingredients"]["milk"] = 0
            cap_latte()
        elif user_choice == "latte" or user_choice == "cappuccino":
            cap_latte()
        elif user_choice == "":
            should_continue = True




coffee_machine()
