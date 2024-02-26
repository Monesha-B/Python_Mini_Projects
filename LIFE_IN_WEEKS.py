age = input("Enter yoyr current age:")

# https://waitbutwhy.com/2014/05/life-weeks.html
C = (90*52)-(int(age) * 52) # 52 weeks in a year and considering 90 is the maximum years an human lives
print(f"You have {C} weeks left.")