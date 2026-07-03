text=input("Enter a text:")
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1
print("Vowels Count:",count)