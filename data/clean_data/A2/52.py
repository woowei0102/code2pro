def factorial (n):
    ans = 1
    for i in range(n):
        ans *= i+1
    return ans
print(factorial(10))
