# number guessing game

# from random import randint
# instead of this ---> guessed_number = random.randint(0,100) we can use this ---> guessed_number = randint(0,100)

import random 
logo = '''

 _ __                             ,___                                ,___                
( /  )              /            /   /                o              /   /                
 /  /  , , _ _ _   /   _  _     /  __  , , _  (   (  ,  _ _   _,    /  __  __,  _ _ _   _ 
/  (_ (_/_/ / / /_/_) (/_/ (_  (___/  (_/_(/_/_)_/_)_(_/ / /_(_)_  (___/  (_/(_/ / / /_(/_
                                                              /|                          
                                                             (/                           
'''


def start_over():
    print(logo)

    print("Welcome to the number guessing game!")

    print("I am thinking of a number between 1 and 100.")

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    guessed_number = random.randint(0,100)
    # print(guessed_number)

    def number_guessing(level):
        if level == "easy":
            n = 10
        elif level == "hard":
            n = 5
        else:
            print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
            return start_over()    
       
        while n > 0:
                     
            print(f"You have {n} attempts remaining to guess.")
            user_guess = int(input("Make a guess: "))
            if user_guess > guessed_number:
                print("Too high")
                n = n - 1
            elif user_guess < guessed_number:
                print("Too low")   
                n = n - 1 
            elif user_guess == guessed_number:
                print(f"You got it! The answer was {user_guess}.")
                user_choice = input("Guess again? Type 'y' or 'n': ").lower()
                if user_choice == "y":
                    start_over()
                break

    number_guessing(difficulty_level)   

start_over()   
