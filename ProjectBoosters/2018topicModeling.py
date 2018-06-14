#from https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/

# import modules
import nltk
nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string

import gensim
from gensim import corpora

# open file and read text, run topic modeling while the file is open and afterwards it will close itself automatically
with open("test.txt","r") as file:

    # create an empty list
    doc_complete = []
    
    # add each line of the file as another string in the list
    for line in file:
        doc_complete.append(line)
    
    # create variables for stopwords, punctuation
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation) 
    lemma = WordNetLemmatizer()
    
    # create a function that "cleans" text, i.e. removes stopwords and punctuation
    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    # run the function to clean text
    doc_clean = [clean(doc).split() for doc in doc_complete]  

    # create the term dictionary of our courpus, where every unique term is assigned an index. 
    dictionary = corpora.Dictionary(doc_clean)

    # convert list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # create the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel

    # run and train LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)

    # print results
    print(ldamodel.print_topics(num_topics=5, num_words=10))