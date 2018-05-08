def NoOneExpectsTheEnglishInquisition(file):
    # open and read the files, create Header Row for export .csv
    text = open(file, 'r')
    entry = text.readlines()
    inquisitions = open('inquisitions.csv', 'w+')
    inquisitions.write('Entry Number|Weird Duplicate of Entry Number|Name|County|Writ|Other Stuff\n')
    
    # create indices for data type counts
    i = 0
    j = 0
    k = 0
    
    # loop through each individual entry within the xml file, identify the start of an entry by <strong>#</strong>
    for line in entry:
        # obtain the entry number that is indicated between the <strong>#</strong> tags
        start_ID = line.find('<strong>')
        if (start_ID < 0):
            i = i +1
            #continue
        else:
            end_ID = line.find('</strong>')
            entry_ID = line[start_ID+8:end_ID]
            inquisitions.write('\n' + entry_ID + '|')
            i = i +1
        # obtain stuff between the <a> tags, note we still need to delete duplicates
        # start_ID = line.find('<a name="')
        # if (start_ID < 0):
        #    j = j +1
        #else:
        #    end_ID = line.find('"></a>')
        #    entry_ID = line[start_ID+9:end_ID] #should actually be +9 but I'm doing a data check to make sure we don't lose part of the number
        #    inquisitions.write(entry_ID+',')
        #    j = j +1
        #obtain stuff after </a> that ends with </td>
        start_ID = line.find('</a>')
        if (start_ID < 0):
            k = k +1
        else:
            end_ID = line.find('</td>')
            entry_ID = line[start_ID+4:end_ID] #should actually be +9 but I'm doing a data check to make sure we don't lose part of the number
            inquisitions.write(entry_ID+'|')
            k = k +1
    
    # close the files and report success to the console
    text.close
    inquisitions.close
    print("The function to extract all possible inquisition records has run. Look for inquisitions.csv")
# end function

if __name__ == "__main__":
    file_name = 'pp1-20.html'
    NoOneExpectsTheEnglishInquisition(file_name)