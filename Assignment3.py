# Task 1 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number1 = int(input("Enter a number: "))

print("Factorial of", number1, "is", factorial(number1))

# Task 2


import math

number2 = int(input("Enter a number: "))
print("Square root :",math.sqrt(number2))
print("Logrithmic :",math.log(number2))
print("Sine :",math.sin(number2))

