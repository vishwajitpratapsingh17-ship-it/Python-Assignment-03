n = int(input("What is your lucky number? :  "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(n)
print(result)

print()

import math
n=int(input("Please enter a random number? :  "))
def sqrt(n):
    return math.sqrt(n)
result = sqrt(n)
print(result)
print()
def log(n):
    return math.log(n)
result = log(n)
print(result)
print()
def sin(n):
    return math.sin(n)
result = sin(n)
print(result)