import re

def open_text(way):
    with open(way, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = re.sub(',.:;!?-"()\n', '', text)
    arr = text.split()
    return arr

def search(arr):
    result = []
    regex = '\\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+аго\\b \\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+\\b'
    for i in range(len(arr) - 7):
        current = ' '.join(arr[i:i+7])
        m = re.search(regex, current)
        if m is not None:
            result.append(current)
    return result

def write(fname, m):
    with open(fname, 'a', encoding = 'utf-8') as f:
        for elem in m:
            f.write(elem)
            f.write('\n')

way = input()
fname = input()
text = open_text(way)
m = search(text)
write(fname, m)
        
