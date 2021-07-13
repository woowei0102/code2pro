def factorial (n):
    count = n
    answer = 1
    while count >= 1:
      answer = answer*count
      count = count - 1
    return answer
print(factorial(10))
