text=input()
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
if text==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")