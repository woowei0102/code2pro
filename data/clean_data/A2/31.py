def factorial (n):
    temp = 1
    for i in range(n):
        temp = temp * (i+1)
    return temp
print(factorial(10))
