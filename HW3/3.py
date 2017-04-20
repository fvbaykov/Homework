a=[]
word=input()
while word:
    a.append(word)
    word=input()
for el in a:
    if len(el)>5:
        print(el)
    else:
        continue
