import re

def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def search(text):
    m = re.findall('\\bдинозавр(a(ми|х)?|у|о(м|в)|е|ы)', text)
    return m

def tags(text):
    m = re.sub('<.*?>', '', text, flags = re.DOTALL)
    return m

def replace(text):
    a = re.sub('\\bдинозавр', 'кот', text, flags = re.DOTALL)
    return a

def images(text):
    n = re.sub('(а|е|ё|и|оуэюя)')

fname = input()
txt = open_text(fname)
res = replace(txt)
print(res)
