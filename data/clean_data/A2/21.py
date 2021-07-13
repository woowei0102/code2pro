
def factorial (n):
    k = int (1)
    for i in range(n):
        k = k*(i+1)
    return k
print(factorial(10))
