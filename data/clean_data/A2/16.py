def factorial (n):
    sum = 1; total=0
    for i in range(1, n+1):
        sum *= i
        total += sum
    return total
print(factorial(10))
