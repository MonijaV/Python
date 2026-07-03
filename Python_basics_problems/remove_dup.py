n=[1,2,3,2,1,5,4]
dup=[]
for ch in n:
    if ch not in dup:
        dup.append(ch)
print(dup)