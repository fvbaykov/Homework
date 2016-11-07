word=input()
for index, elem in enumerate(word):
    if (index + 1) % 2 ==1:
        if elem in 'пое':
            print(elem)
        else:
            continue
    else:
        continue
            
