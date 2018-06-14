# This is a booster for a group that would like to do counts of words in a text.
# The current version will do the top 10.
# Extenstions could include (is rough order of increasing difficulty...):
# 0. Modify stop_words to take your own additional words and handle punctuation.
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
        #print(line)
        wordList = line.split()
        #print(wordList)
        for word in wordList:
            word = word.lower()
            #print(word)
            if word not in stop_words:
                wordCounter.update([word]) #why is the counter object being passed a list of one item?
                #print(wordCounter)

#print(dicthist)

print(wordCounter.most_common(10))


import matplotlib.pyplot as plt

#special ipython/jupyter command that keeps the output in this window rather than opening another one.
#aka, if you want to use this in jupyter then you should uncomment the next line.
#%matplotlib inline 

# this is a sample figure.  Play with it and understand it.
# Once you have a handle on what it is doing then consider commenting it out and 
# uncommenting the version below (which you'll need to correct.)

plt.figure()
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.bar([1,2,3,4],[12,3,25,18], width=0.2, align='center')
plt.xlim(0.5, 4.5)
plt.ylim(0,50)
plt.show()


#import matplotlib.pyplot as plt
#%matplotlib inline

#Note that there is some fanciness used below. [x[1] for x in L] is the format for what
# is known as "list comprehension".  It let's us go through a list---on a single line---
# and create a new list out of its components---on the fly!  Make sure you understand what
# wordCounter.most_common(10) is returning, how the above matPlotLib example works
# and what is happening with the list comprehension used here.

#plt.figure()
#plt.bar(range(10),[x[1] for x in wordCounter.most_common(10)])
#plt.xticks(range(10), [x[0] for x in wordCounter.most_common(10)],rotation='vertical')

#plt.show()