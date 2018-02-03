import urllib.request
import re
import os

def download_page(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as responce:
        html = responce.read().decode('utf-8')
    return html

def clean_html(file):
    tags = re.compile('<.*?>', flags = re.DOTALL)
    scripts = re.compile('<script .*? </script>', flags = re.DOTALL)
    clean = scripts.sub("", file)
    clean = tags.sub("", clean)
    return clean

def find(file):
    regex = re.compile(' с.*?[ |.|!|<|>|\?|;|:|,|»]', flags = re.DOTALL)
    words = regex.findall(file)
    regex1 = re.compile(' С.*?[ |.|!|<|>|\?|;|:|,|»]', flags = re.DOTALL)
    words1 = regex1.findall(file)
    for i in words1:
        words.append(i)
    new_words = []
    for i in words:
        rex = re.compile('<.*?>')
        j = rex.sub("", i)
        rex2 = re.compile('[<|>| |.|!|"|\?|;|:|»|,]')
        j = rex2.sub("", j)
        new_words.append(j)
    return(new_words)

def main():
    page = 'http://web-corpora.net/Test2_2016/short_story.html'
    html = download_page(page)
    clean = find(html)
    res = []
    for i in clean:
        if not (i == 'с&nbsp'):
            res.append(i)
    return res



res = main()
for i in res:
    print(i)
way = '.\\input_texts\\1.txt'
    

