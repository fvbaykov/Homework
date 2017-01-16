def open_text(way_to_file):
    with open(way_to_file, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    arr = text.split()
    for index, elem in enumerate(arr):
        arr[index] = elem.strip(',.;:!?\n ')
    return arr

def first_letter(letter, way_to_file):
    arr = open_text(way_to_file)
    array = []
    for elem in arr:
        if elem[0] == letter:
            array.append(elem)
    return array

def questions():
    letter = input()
    fname = input()
    result = first_letter(letter, fname)
    return result

result = questions()
print(result)


