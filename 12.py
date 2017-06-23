import re
import os

def number_sent(direct):
    d = {}
    for root, dirs, files in os.walk(direct):
        for file in files:
            with open(os.path.join(direct, file)) as f:
                text = f.read()
            regex = '<se>'
            arr = re.findall(regex, text)
            d[file]=len(arr)
    return d

def main():
    direct = './news'
    d = number_sent(direct)
    with open('./11.txt', 'w', encoding='utf-8') as f:
        for key in d.keys():
            f.write('\n{} {}'.format(key, d[key]))

main()
    
