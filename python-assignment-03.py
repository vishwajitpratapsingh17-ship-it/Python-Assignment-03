n = int(input("What is your lucky number? :  "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(n)
print(result)

