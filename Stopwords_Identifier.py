from nltk import wordpunct_tokenize
from nltk.corpus import stopwords


def Predictlang (path):
    lang_score = {}
    filetext=""
    with open(path, encoding="utf8") as myfile:
        for line in myfile:
            filetext+=line+" "
    tokens = wordpunct_tokenize(filetext)
    words = [word.lower() for word in tokens]
    for language in stopwords.fileids():
        stopwordsset=set(stopwords.words(language))
        wordsset=set(words)
        commonlang=wordsset.intersection(stopwordsset)
        lang_score[language]=len(commonlang)

    return  max(lang_score, key=lang_score.get)






language=Predictlang("C:\\Users\\Mahmoud\\Desktop\\wortschatz-leipzig-corpus\\train\\spa_news_2011_30K\\spa_news_2011_30K-sentences.txt")
print(language)