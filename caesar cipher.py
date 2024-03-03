# to execute both encode and decode in the single function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar_cipher(text, shift_level, direction):
    if direction == "encode":
        crypted_text = ""  # encrypted
        for char in text:
            if char in alphabet:
                current_position = alphabet.index(char)
                new_position = current_position + shift_level
                
                if new_position >= 26:
                    alphabet1 = alphabet*new_position # works till 9999999 
                    new_letter = alphabet1[new_position]
                else:
                    new_letter = alphabet[new_position]
                crypted_text += new_letter
            else:
                crypted_text += char        
            
        
    elif direction == "decode":
        crypted_text = "" # decrypted text
        for char in text:
            if char in alphabet:
                current_position = alphabet.index(char)
                new_position = current_position - shift_level
                
                if new_position <= -26: 
                    alphabet1 = alphabet*(-new_position) # works till 9999999 
                    new_letter = alphabet1[new_position]
                else:
                        new_letter = alphabet[new_position]
                crypted_text += new_letter
            else:
                crypted_text += char 

    print(f"Here's the {direction}d result: {crypted_text}")   


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # can use shift = shift % 26 instead if statement
    caesar_cipher(text = text , shift_level = shift, direction = direction)  
    user_input = input("Would you like try again? type 'yes'/'no':")
    if user_input =="no":
        should_continue = False
        print("Thank you, Bye!")
  

         











# seperately executes each functions
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(plain_text, shift_level):
#     encrypted_text = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             current_position = alphabet.index(letter)
#             new_position = current_position + shift_level
            
#             if new_position >= 26:
#                 alphabet1 = alphabet*new_position # works till 9999999 
#                 new_letter = alphabet1[new_position]
#             else:
#                     new_letter = alphabet[new_position]
                
#         encrypted_text += new_letter
#     print(encrypted_text)

# def decrypt(cipher_text, shift_level):
#     decrypted_text = ""
#     for letter in cipher_text:
#         if letter in alphabet:
#             current_position = alphabet.index(letter)
#             new_position = current_position - shift_level
            
#             if new_position <= -26:
#                 alphabet1 = alphabet*(-new_position) # works till 9999999 
#                 new_letter = alphabet1[new_position]
#             else:
#                     new_letter = alphabet[new_position]
                
#         decrypted_text += new_letter
#     print(decrypted_text)
 

# if direction == "encode":
#     encrypt(plain_text = text, shift_level = shift)
# else:
#     decrypt(cipher_text = text , shift_level = shift)   

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 