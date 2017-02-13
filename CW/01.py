def open_text(way):
    with open(way, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    arr = text.split()
    for index, elem in enumerate(arr):
        arr[index] = elem.strip(',.;:!?-')
    return arr

def main():
    fname = input()
    arr = open_text(fname)
    n = len(arr)
    return n

res = main()
print('В файле содержится ', res, ' слов')
