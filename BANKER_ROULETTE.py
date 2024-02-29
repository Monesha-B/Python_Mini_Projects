import random

def names_string():

    n = int(input("Enter the size of the list "))

    num_list = list(str(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

    print("User list: ", num_list)

names = names_string() # names_string is an import module created for  input()
# The code above converts the input into an array seperating
#each name in the input by a comma and space.

random_index = random.randrange(0,len(names)-1) # to get the random index and without or with 0
random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")


# names = names_string.split(", ")

# import random

# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])
# def names_string():

#     n = int(input("Enter the size of the list "))

#     num_list = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

#     print("User list: ", num_list)

