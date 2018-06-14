# This is a sample chunk of code that extract snippets of text around a search term

# load re module
import re

# create and write header to output file - this is a tsv, a tab-separated-value file, so that commas do not break the program
results = open('results.tsv', 'w+')
results.write('File Name\tSearch Term\tSnippet\r\n')

# set up repeatable code
repeat = "go"

while repeat != "stop":
    # ask user for file name and search term
    filename = input("What is the name of the file you would like to search? Include file extension, i.e. 'shakespeare.txt'?: ")
    searchterm = input("What is the term you would like to search on?: ")

    text = open(filename, 'r')

    # for each line in the file
    for line in text:
        # find mentions of search term
        start_index = 0
        for mention in re.finditer(searchterm, line):
            start_index = mention.start()
            if (start_index > 0):
                results.write(filename + '\t' + searchterm + '\t' + line + '\n')
    text.close
    repeat = input("Type 'stop' to end program, or press enter to repeat: ")

# close the results file
results.close