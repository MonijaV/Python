text=input()
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print("The reversed String:",rev)