def divide(a,b):
    try:
        res=float(a)/float(b)
        return res
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Enter Valid Number"
print("10 / 2 =", divide(10, 2))
print("5 / 0 =", divide(5, 0))
print("'abc' / 3 =", divide("abc", 3))