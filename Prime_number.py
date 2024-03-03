def is_prime(number):
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")     
    else:
        print("It is not a prime number.")    

n = int(input())
is_prime(number = n)












# # importing sympy module
# from sympy import *
 
# # calling isprime function on different numbers
# geek1 = isprime(30)
# geek2 = isprime(13)
# geek3 = isprime(2)
 
# print(geek1) # check for 30 is prime or not
# print(geek2) # check for 13 is prime or not
# print(geek3) # check for 2 is prime or not
 