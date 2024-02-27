# https://ascii.co.uk/art
'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
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

     