def factorial (n):
    fact = int(1)
    for i in range(1,n+1): 
        fact *= i 
    return fact
print(factorial(10))