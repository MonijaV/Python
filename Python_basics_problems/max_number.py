numbers = [10, 50, 30, 90, 20]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Maximum:", largest)