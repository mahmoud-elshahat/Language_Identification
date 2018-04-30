
import nltk
from nltk.collocations import BigramCollocationFinder
import re
import string


def train_language():
    path="C:\\Users\\Mahmoud\\Desktop\\wortschatz-leipzig-corpus\\train\\fra_news_2010_30K-text\\fra_news_2010_30K-sentences.txt"
    lang_name="english"
    all_sents = []
    translate_table = dict((ord(char), None) for char in string.punctuation)
    with open(path, encoding="utf8") as myfile:
        for line in myfile:
            # extracting the text sentence from each line
            line = " ".join(line.split()[1:])
            # to lower case
            line = line.lower()
            # remove digits
            line = re.sub(r"\d" , "" , line)
            if len(line) != 0:
                # remove punctuations
                line = line.translate(translate_table)
                all_sents += line
            all_sents.append(" ")
    all_str = ''.join(all_sents)
    all_str = re.sub(' +', ' ', all_str)
    # seq_all = [i for i in all_str]

    # extracting the bi-grams and sorting them according to their
    Bigram = nltk.bigrams(all_str)
    #print(bgs)
    fdist = nltk.FreqDist(Bigram)
    bigram_model = sorted(filter(lambda x: x[1] >= 10, fdist.items()), key=lambda x: x[1], reverse=True)
    thefile = open(lang_name + "train.txt", 'w',encoding="utf8")
    thefile.write('\n'.join('{} {}'.format(x[0], x[1]) for x in bigram_model))
    thefile.close()





train_language()