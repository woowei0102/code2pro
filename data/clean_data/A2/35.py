def factorial (n):
    sum=1
    now=1
    for i in range(n):
        sum=sum*now
        now=now+1
    return sum
print(factorial(10))
