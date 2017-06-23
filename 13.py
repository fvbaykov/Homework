import re
import os

def auth(direct):
    d = {}
    for root, dirs, files in os.walk(direct):
        for file in files:
            with open(os.path.join(direct, file)) as f:
                text = f.read()
            regex1 = 'content=".*" name="author"'
            a = re.findall(regex1, text)
            for elem in a:
                b = re.sub('content="', '', elem)
                c = re.sub('" name="author"', '', b)
                d[file] = c
    return d

def topic(direct):
    d = {}
    for root, dirs, files in os.walk(direct):
        for file in files:
            with open(os.path.join(direct, file)) as f:
                text = f.read()
            regex1 = 'content=".*" name="topic"'
            a = re.findall(regex1, text)
            for elem in a:
                b = re.sub('content="', '', elem)
                c = re.sub('" name="topic"', '', b)
                d[file] = c
    return d

def main():
    direct = './news'
    d1 = auth(direct)
    d2 = topic(direct)
    with open('./15.csv', 'w', encoding='utf-8') as f:
        for key in d1.keys():
            f.write('\n{}'.format(key))
            f.write(' {} '.format(d1[key]))        
            f.write('{}'.format(d2[key]))

main()





