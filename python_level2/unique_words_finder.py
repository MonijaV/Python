text="Hello Everyone Good Evening Everyone"
words=text.split()
s=set(words)
dup=len(words)-len(s)
print("Duplicate words removed:",dup)