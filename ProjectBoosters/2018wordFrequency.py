# this will determine the frequency of words in a text file; it uses a 'dict' or dictionary, which is an object type we haven't used before
# remember: strings, integers, floats, booleans, and lists are all examples of different types of objects

# import module
import re

# initialize variables and open file
frequency = {}
#print(type(frequency))
document_text = open('test.txt', 'r')

# read in text from file and use regular expressions to create a list of everything that looks like a word
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string) # words 3-15 char long

# loop through list and count how often each word appears
for word in match_pattern:
    count = frequency.get(word,0) # set word's count equal to the number of times the word has already appeared, or 0 if it hasn't appeared yet
    frequency[word] = count + 1 # increase the word's count by one
#print(frequency)

# create a list of each unique word
frequency_list = frequency.keys()
# print(frequency_list)
 
# print each word in frequency and the number of times it appears
for words in frequency_list:
    print(words, frequency[words])

# alternatively, sort the dictionary by most frequent words and print how many times it appears
#for words in sorted(frequency, key=frequency.get, reverse=True):
#    print(words, frequency[words])
    
document_text.close()