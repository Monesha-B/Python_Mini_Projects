print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
split_bills = int(input("How many people to split the bill? $"))
percent_tip = int(input("What percent tip would you like to give? 10, 12 or 15? $"))
overal_pay = (total_bill) + (total_bill*(percent_tip/100))
each_pay = overal_pay/split_bills

#round function work round the decimal places
# print("Each Person should pay including tip: $" + str(round(each_pay, 2))) 
final_value1 = round(each_pay, 2)
# format function to bring exactly 2 values after decimal
final_value2 = "{:.2f}".format(each_pay)#



print(f"Each Person should pay including tip: ${final_value1}") 
print(f"Each Person should pay including tip: ${final_value2}") 



