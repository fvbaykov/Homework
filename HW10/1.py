def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    arr = text.split()
    for index, elem in enumerate(arr):
        arr[index] = elem.strip(',.;:!?\n ')
    return arr

def finding_suffix(suffix, way_to_file):
    arr = open_text(way_to_file)
    array = []
    for elem in arr:
        a = len(elem) - len(suffix)
        b = len(elem)
        if elem[a:b] == suffix:
            array.append(elem)
    return array

def one_word_once(array):
    arr = []
    for elem in array:
        if elem not in arr:
            arr.append(elem)
    return arr

def func(array):
    temp = []
    arr = []
    for elem in array:
        if elem not in temp:
            temp.append(elem)
        else:
            arr.append(elem)
    return arr

def count_freq(array):
    result = array
    for i in range(len(array)):
        temp = func(result)
        if len(temp)==0:
            break
        else:
            result = temp
    return result

fname = input()
suffix = 'ness'
arr = finding_suffix(suffix, fname)
array = one_word_once(arr)
print('В тексте имеются следующие слова с суффиксом ', suffix, ':')
for elem in array:
    print(elem)
max_freq = count_freq(arr)
print('Макс. частоту имеет(-ют) слово(-а):', max_freq)
