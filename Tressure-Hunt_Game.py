print("Welcome to Treasure Island. Your mission is to find the treasure")

first = input("You're at a cross rood now.\nWhere do you want to go? Type 'left' or 'right':  ")

if first == 'left':
    second = input("You came to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. type 'swim' to swim across:  ")
    if second == "wait":
        third = input("You arrived at the island unharmed. There is a house with 3 doors.\none red, one yellow and one blue. which color do you choose?\n")
        if third == "red":
            print("you are Burned by fire. Game Over")
        elif third == "blue":
            print("you are Eaten by beasts. Game Over.")
        elif third == "yellow":
            print("You win!")    
else:    
    print("Fall into a hole. Game Over")

     