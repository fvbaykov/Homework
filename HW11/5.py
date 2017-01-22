import random

def opening_csv(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    arr = text.split('\n')
    d = {}
    for elem in arr:
        array = elem.split(',')
        d[array[0]] = array[1]
    return d

def random_key(d):
    array = []
    for elem in d.keys():
        array.append(elem)
    word = random.choice(array)
    return word

def main():
    way_to_file = input()
    vocabul = opening_csv(way_to_file)
    word = random_key(vocabul)
    print(word)
    for i in range(len(vocabul[word])):
        print('_', end = ' ')
    solve = input()
    if solve == vocabul[word]:
        result = 'WIN!!!'
    else:
        result = 'FAIL((('
    return result

res = main()
print(res)
