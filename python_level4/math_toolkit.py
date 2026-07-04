import math
def area_circle(r):
    return math.pi * r * r
def area_rectangle(w, h):
    return w * h
def is_even(n):
    return n % 2 == 0
def factorial(n):
    return math.factorial(n)
print(f"Area of Circle (r=5): {area_circle(5):.2f}")
print(f"Area of Rectangle (w=4, h=6): {area_rectangle(4, 6)}")
print(f"Is 10 Even? {is_even(10)}")
print(f"Factorial of 5: {factorial(5)}")