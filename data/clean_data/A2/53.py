def factorial (n):
    x=int(1)
    for i in range(1,n+1):
        x*=i
    return x
print(factorial(10))
