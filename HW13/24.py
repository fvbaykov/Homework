import re

def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def search(text):
    text1 = re.sub('<.*?>', '', text, flags = re.DOTALL)
    text2 = re.sub('\n', '', text1, flags = re.DOTALL)
    m = re.findall('Часовой поясUTC.?[0-9]', text2)
    return m

def write(arr, way_to_file2):
    with open(way_to_file2, 'a', encoding = 'utf-8') as f:
        for elem in arr:
            newtext = f.write(elem)
    return newtext

def main():
    fname1 = input()
    fname2 = input()
    t = open_text(fname1)
    txt = search(t)
    res = write(txt, fname2)
    return res

a = main()
