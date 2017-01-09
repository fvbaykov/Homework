# coding=utf-8
import random

def organising_array(way_to_file):
    f = open(way_to_file, 'r', encoding = 'utf-8')
    file = f.read()
    arr = file.split('\n')
    return arr

def noun_phrase():
    adjectives = organising_array('./1.txt')
    adjective = random.choice(adjectives)
    nouns = organising_array('./2.txt')
    noun = random.choice(nouns)
    return adjective + ' ' + noun

def clause():
    clauses = organising_array('./3.txt')
    return random.choice(clauses)

def adverb():
    adverbs = organising_array('./4.txt')
    return random.choice(adverbs)

def clause2():
    clitics = organising_array('./5.txt')
    clitic = random.choice(clitics)
    pronouns = organising_array('./6.txt')
    pronoun = random.choice(pronouns)
    verbs = organising_array('./7.txt')
    verb = random.choice(verbs)
    return clitic + ' ' + pronoun + ' ' + verb

def objects():
    objects = organising_array('./8.txt')
    return random.choice(objects) 

def patient():
    patients = organising_array('./9.txt')
    return random.choice(patients)

def verb():
    verbs = organising_array('./10.txt')
    return random.choice(verbs)

def praep_phrase():
    praeps = organising_array('./11.txt')
    praep = random.choice(praeps)
    nouns = organising_array('./12.txt')
    noun = random.choice(nouns)
    return praep + ' ' + noun

def adjective():
    adjectives = organising_array('./13.txt')
    return random.choice(adjectives)

def punctuation():
    marks = organising_array('./14.txt')
    return random.choice(marks)

def verse1():
    return noun_phrase()+ punctuation() + ' ' + clause() + punctuation()

def verse2():
    return adverb() + ' ' + clause2() + ' ' + objects() + punctuation()

def verse3():
    return patient() + ' ' + verb() + ' ' + praep_phrase() + ' ' + adjective() + punctuation()

def make_verse():
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()

for n in range(4):
    print(make_verse())
