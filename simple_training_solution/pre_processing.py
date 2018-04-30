

from nltk.tokenize import word_tokenize
import re

# open here file that have skills for example in random way and not with number to make it better .
with open('dataset/fra.txt', 'r',encoding='utf8') as myfile:
    data = myfile.read()

data = data.lower()
data = re.sub(r'\d+', '', data)

data = re.sub(r'[^\w\s]', '', data)

# tokenizing for words
words = word_tokenize(data)
with open("dataset/fra_after_processing.txt", "a",encoding='utf8') as myfile:
    myfile.write(str(words))




with open('dataset/fra_after_processing.txt', 'r',encoding='utf8') as myfile:
    data = myfile.read()

data = re.findall(r'\'(.*?)\'', data)

with open("dataset/fra_after_processing.txt", "w",encoding='utf8') as myfile:
    myfile.write("\n".join(data))




