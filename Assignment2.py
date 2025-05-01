# Task 1

n = int(input("Enter a number: "))
if n % 2 == 0:
    print(n, "is an even number")
else:
    print(n, "is an odd number")
    
    
# Task 2

sumofNumbersUpto50 = 0
for i in range(1, 51):
    sumofNumbersUpto50 += i
print("The sum of numbers from 1 to 50 is:", sumofNumbersUpto50)