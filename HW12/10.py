import re

def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    arr = text.split()
    for index, elem in enumerate(arr):
        arr[index] = elem.strip(',.;:!?\n ')
    return arr

def main():
    reglex = 'на(й(ти|д(я|ут?|((е|ё)(шь|т|м|те)|ен(а|о|ы)?)))|ш((е|ё)л|л(а|о|и))|шедш(е(е|й|го|му?)|ая|ую|и(й|е|х|ми?))|йденн(о(е|го|ому?)|ая|ой|ую|ы(й|е|х|ми?))(с(ь|я))?)'
    fname = input()
    arr = open_text(fname)
    array = []
    for elem in arr:
        m = re.search(reglex, elem)
        if m != None:
            if elem not in array:
                array.append(elem)
    return array

result = main()
print(result)







