way = input('Введите путь к файлу без дополнительных символов: ', )
f = open(way, 'r', encoding = 'utf-8')
text = f.read()
f.close()
min = len(text)
max = 0
arr = text.split('\n')
for el in arr:
    if len(el) > max:
        max = len(el)
    if len(el) < min:
        min = len(el)
k = max/min
print('Самая короткая строка короче самой длинной в ', k, ' раз(а)')


