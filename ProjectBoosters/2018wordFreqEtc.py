# This is a booster for a group that would like to do counts of words in a text.
# The current version will do the top 10.
# Extenstions could include:
# 0. Modify stop_words to take your own additional words.
# 1. Asking a user to input a word and count only that.
# 2. Passing two texts and making a comparison (If this is done then you should be modifying the text to create and call a function)
# 3. Running this for every file in a directory.


from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

from collections import Counter

wordCounter=Counter()
with open("Winter-1859.txt", "r") as inputFile:
    # Process the input word by word, counting each word
    for line in inputFile:
        wordList = line.split()
        for word in wordList:
            word = word.lower()
            #print(word)
            if word not in stop_words:
                wordCounter.update(word)
                print(wordCounter)

#print(dicthist)

print(wordCounter.most_common(10))

