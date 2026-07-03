def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if ch in vowels:
            count+=1
    return f"The number of Vowels in string are {count}"
text=input("Enter a string:")
print(count_vowels(text))