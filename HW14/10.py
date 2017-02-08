import re

def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def replace1(txt):
    m = re.sub(r'\bвикинг(а(ми?|х)?|у|о(м|в)|е|и)?\b', r'\bбурундук\1', txt, flags = re.DOTALL)
    return m

def replace2(txt):
    n = re.sub(r'\bВикинг(а(ми?|х)?|у|о(м|в)|е|и)?\b', r'\bБурундук\1', txt, flags = re.DOTALL)
    return n

def write(txt, way_to_file2):
    with open(way_to_file2, 'w', encoding = 'utf-8') as f:
        newtext = f.write(txt)
    return newtext

def main():
    fname1 = input()
    fname2 = input()
    txt = open_text(fname1)
    r = replace1(txt)
    res = replace2(r)
    result = write(res, fname2)
    return result

a = main()
