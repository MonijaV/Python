num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:"))
num3=int(input("Enter a Number:"))
if num1>=num2 and num1>=num3:
    print("The Largest Number is:",num1)
elif num2>=num1 and num2>=num3:
    print("The Largest Number is:",num2)
else:
    print("The Largest Number is:",num3)