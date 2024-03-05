# to print how many days in a month for the input given by the user

def is_prime(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False    

def finding_days_in_a_month(year, month):
    month_in_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_prime:
        return 29
    else:
        return month_in_days[month-1]

''' 
month_name = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
'''           
year = int(input("Enter the year: ")) # in int format
month = int(input("Enter the month: ")) # in int format
days = finding_days_in_a_month(year, month)
print(f"No of days: {days}")
