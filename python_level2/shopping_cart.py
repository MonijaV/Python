items = [("KitKat", 10), ("Munch", 15), ("MilkyBar", 20)]
print(items)
for item, price in items:
    print(f"{item} costs {price}")
maximum = items[0][1]
minimum = items[0][1]
for i in range(len(items)):
    if items[i][1] > maximum:
        maximum = items[i][1]
    if items[i][1] < minimum:
        minimum = items[i][1]
print("Maximum Cost:", maximum)
print("Minimum Cost:", minimum)