import markovify
from bs4 import BeautifulSoup as Soup
import re
import json
import os

def Read(path):
    with open(path, 'r', encoding='utf-8') as xml:
        soup = Soup(xml, 'xml')

    bufStr = ""

    for buf in soup.body.find_all('p'):
        bufStr += (buf.get_text(strip=False)+' ')

    url_pattern = r'http\S* '
    bufStr = re.sub(url_pattern, " ", bufStr)
    bufStr = bufStr.replace("...", " ")
    
    letterList = r"!?@#$&*()<>[]_=+—«»\"–:;/„”…“~"
    
    for letter in letterList:
        bufStr = bufStr.replace(letter, " ")

    bufStr = re.sub(r'(i|I)*\s', " ", bufStr)
    bufStr = re.sub(r'\s*\s', " ", bufStr)

    return bufStr.lower()

#text_model = markovify.NewlineText(Read(r'fanfiction/Cto-delat-esli-tvoj-klassnyj-rukovoditel-Satana.fb2'))

directory = "fanfiction"
files = os.listdir(directory)

MegaString=""

for doc in files:
    MegaString += Read(directory+'/'+doc)
    print("Текст " + doc + " обработан!")
print("Все тексты обработаны!")

ResultMegaString = ""
StringList = MegaString.split('.')
count = 0

file =  open('MarkovModelDict.txt', 'w', encoding='utf-8')
for line in MegaString.split('. '):
    file.write(line + "\n")
print("Все тексты записаны!")