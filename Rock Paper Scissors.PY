import random

print("""Welcome to the Rock, Paper and Scissors game!\n
Below are rules sets for this game\n
I - Rock wins against scissors.\n
II - Paper wins against rock.\n
III - Scissors win against paper.\n      
you get to play with computer and check your luck if you can beat
""")
global computer_select
def rps():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    select_index = [rock, paper, scissors]
    selected_index = len(select_index) - 1

    # Human's choice
    Human = int(input("What do you want to choose? select 0 for rock, 1 for paper, and 2 for scissors: "))
    
    if Human >= 3 or Human < 0:
         print("You typed an invalid number, you lose!")
    else:     
        Human_select = select_index[Human]
    
        print(Human_select)

        # computer's choice in 0,1,2
        selected_index = len(select_index) - 1
        final_select = random.randint(0,selected_index)
        print("Computer's choice:\n")
        computer_select = select_index[final_select]
        print(computer_select)

        if computer_select == Human_select:
            print("Draw")
        elif (Human_select == rock and computer_select == scissors) :
            print("You win!")
        elif (Human_select == paper and computer_select == rock) :
            print("You win!")
        elif (Human_select == scissors and computer_select == paper) :
            print("You win!")
        else:
            print("Computer wins!")    


# calling the function to start the game 
rps()

# below while loop will make the game continue or exit as per the user input
# looping tp play again
Play_again = input("Would you like to give it a go again. Choose y to continue and n to exit: ").capitalize()
while Play_again != "N":  
        rps()
        Play_again = input("Would you like to give it a go again. Choose y to continue and n to exit: ").capitalize()
