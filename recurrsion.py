def factorial(a):
    if a==1:return 1
    return a *factorial(a-1)
print(factorial(4))