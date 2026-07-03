def even_odd(num):
    if num%2==0:
        return "The Number is even"
    else:
        return "The Number is odd"
num=int(input("Enter a Number:"))
print(even_odd(num))