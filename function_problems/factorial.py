def factorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i+=1
    return f"Factorial of {num} is {fact}"
num=int(input("Enter a Number:"))
print(factorial(num))