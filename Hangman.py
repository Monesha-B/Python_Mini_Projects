import random

print("Welocme to Hangman Game!")

words = ['apple', 'orange','pear','peach','strawberry','pineapple']


computer_select = random.randint(0,len(words)-1)
# print(words[computer_select])
Random_word = words[computer_select]
print(Random_word)

guess_word = []
for leter in range(len(Random_word)): # instead of random word can use range(len(random_word))
    guess_word += '_'
    # guess_word = guess_word + "_"
print(guess_word)    
endofgame = False
while not endofgame:
    User_input = input("Guess a word:")

    for position in range(len(Random_word)):
        
        # if  User_input in Random_word:
        #     print("right")
        # else:
        #     print("wrong")    
        letter = Random_word[position]
        if letter == User_input:
            guess_word[position] = letter
    print(guess_word)        
    if "_" not in guess_word:
        endofgame = True
        print("you win!")



# for position in range(len(Random_word)):
    
#     # if  User_input in Random_word:
#     #     print("right")
#     # else:
#     #     print("wrong")    
#     letter = Random_word[position]
#     if letter == User_input:
#         guess_word[position] = letter
# print(guess_word)        

