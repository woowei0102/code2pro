def factorial (n):
    sum=1
    ans=0
    for i in range(1,n+1):
        sum*=i
        ans+=sum
    return ans
print(factorial(10))
