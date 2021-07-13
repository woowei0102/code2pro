def factorial (n):
    if n==1:
        return n
    else:
        result = n*factorial(n-1)
        
    return result
        
        
print(factorial(10))
