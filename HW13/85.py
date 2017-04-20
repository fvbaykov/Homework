import os
import re

def no_numbers():
    num = '(1|2|3|4|5|6|7|8|9|0)'
    file = '\.'
    a = []
    for elem in os.listdir('.'):
        res = re.search(num, elem)
        if res == None:
            result = re.search(file, elem)
            if result:
                a.append(elem)
    n = len(a)
    return n

def no_repet():
    arr = []
    for elem in os.listdir('.'):
        a = re.sub('\..*', '', elem)
        if a not in arr:
            arr.append(a)
    return arr

print('Количество файлов без цифр в названии равно', no_numbers())
print('Найдены следующие файлы и папки (без повторов):', no_repet())



    
