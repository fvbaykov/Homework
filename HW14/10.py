import os
import re

def dir_choose_kyr(dir_name):
    arr = []
    regex ='[А-Я|Ё|а-я|ё| ]*'
    for root, dirs, files in os.walk(dir_name):
        for elem in dirs:
            r = re.sub(regex, '', elem)
            if r == '':
                arr.append(elem)
    print(arr)
    n = len(arr)
    return n

def main():
    dir_name = '.'
    n = dir_choose_kyr(dir_name)
    print('В папке найдено ', n, ' папок с полностью кириллическими названиями (допускаются пробелы между словами)')
    return n

main()
