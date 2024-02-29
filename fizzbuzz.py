for count in range(1,101):   # can set target = 100 and target+1 in range 
    if count%3 == 0 and count%5 == 0:
      print("FizzBuzz")
    elif count%5 == 0:
      print("Buzz")
    elif count%3 == 0:
      print("Fizz")
    else:  
      print(count)
