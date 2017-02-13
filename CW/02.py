def open_text(way):
    with open(way, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    arr = text.split()
    for index, elem in enumerate(arr):
        arr[index] = elem.strip(',.;:!?-"')
    return arr

def freq_list(arr):
    d = {}
    for elem in arr:
        if elem not in d.keys():
            d[elem] = 1
        else:
            d[elem] = d[elem] + 1
    return d

def sort(d):
    array = []
    for elem in d.keys():
        array.append(elem)
    arr = []
    for i in range(len(array)):
        temp = array[i]
        for index, elem in enumerate(array):
            if elem < temp:
                t = temp
                temp = elem
                array[index] = t
        if temp not in arr:
            arr.append(temp)
    return arr

def write(fname, d, arr):
    with open(fname, 'a', encoding = 'utf-8') as f:
        for elem in arr:
            f.write(elem)
            f.write(',')
            f.write(str(d[elem]))
            f.write('\n')

fname = input()
fname2 = input()
arr = open_text(fname)
d = freq_list(arr)
a = sort(d)
write(fname2, d, a)  
