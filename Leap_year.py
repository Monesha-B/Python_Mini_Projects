# Leap year

Year = int(input("Enter the year to find it's a leap year or not: "))
if Year % 4 == 0:
    if Year % 100 != 0:
        print("Leap year")
    elif Year % 400  == 0:
        print("Leap year")  
    else:
        print("Not leap year")     
else:
    print("Not leap year")


# # Which year do you want to check?
# year = int(input())

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")    