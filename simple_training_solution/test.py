from nltk.tokenize import word_tokenize
import re


text = "ich komme aus "

text = text.lower()
text = re.sub(r'\d+', '', text)
text = re.sub(r'[^\w\s]', '', text)
words=word_tokenize(text)

languages_ratios={}
trained_languages_paths=["eng_trained.txt","deu_trained.txt","fra_trained.txt"]
trained_languages=["eng","deu","fra"]


data = {}
for language in trained_languages:
    data[language]={}
    languages_ratios[language]=0



for (path,language) in zip(trained_languages_paths,trained_languages):
    with open("dataset/"+path) as f:
        for line in f:
            name, var = line.partition(" ")[::2]
            data[language][name.strip()] = var


count={}
items_ratio={}
for word in words:
    tracker = 0
    language_tracker="eng"
    for key in data:
        temp=data[key]
        for sub_key in temp:
            if(sub_key==word):
                if(tracker<int(temp[sub_key])):
                    tracker=int(temp[sub_key])
                   # print(tracker)
                    #print(word, " found in ", key, "times = ", temp[sub_key])
                    language_tracker=key
    languages_ratios[language_tracker]=(languages_ratios[language_tracker]+tracker)


print(languages_ratios)



most_count = 0
most_language = "eng"
for language_ratio in languages_ratios:
    if(int(languages_ratios[language_ratio])>most_count):
        most_count=int(languages_ratios[language_ratio])
        most_language=language_ratio


print(most_language , most_count)


