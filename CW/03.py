import re

def open_text(way):
    with open(way, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('-', '')
    text = text.replace('"', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    return text

def search(text):
    regex = '\\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+аго\\b \\b[\\w]+\\b \\b[\\w]+\\b \\b[\\w]+\\b'
    m = re.findall(regex, text, flags = re.DOTALL)
    return m

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
        
