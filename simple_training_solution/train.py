from nltk.tokenize import word_tokenize

with open('dataset/fra_after_processing.txt', 'r') as myfile:
    data = myfile.read()

# tokenizing for words
words=word_tokenize(data)

# like hash map "dictionary" to store word like java and how many times it's appears in above file .
released = {};

#loop over words in file
for i in words:
    i=i.lower()
    if i in released :
        released[i] = (released.get(i)+1)
    # else here as it's first time to see this key so add key with value 1 , the first time this word appears .
    else:
        released[i]=1;








# finally open another file and insert word + space + counter which represent how many times this word appears.
for x in released:
    #first insert new line so every word with it's counter will be in single line for nice format only
    with open("dataset/fra_trained.txt", "a") as myfile:
        myfile.write("\n")
        myfile.write(x + " " + str(released.get(x)))

