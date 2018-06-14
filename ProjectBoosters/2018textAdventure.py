"""
Text Adventure Booster
This is meant to get you started thinking about how to implement the basic structure of a text adventure in Python. You need to be clear about what you want player's to be able to do in the adventure. Start simple, we can always add complexity later. So, it is better to get something working that allows a player to just move through the game first and then take a copy of that and modify it to make it necessary for the player to collect and carry objects.

It will be really important for you to understand loops, conditionals, and either lists or dictionaries.

Michael and Jennifer built a Star Trek text adventure in the 2014 class. The code that they used is fully functional and below.
Note that it needs to be accompanied by a specially formatted text file.
The format of this file is key to understanding how everything works.

Make sure you understand the code and what is going on in general by:

1. Adding comments to the code to explain it to your future self.
2. Uncommenting the print statements (or add your own) to figure out what is being done when (feel free to add your own too).
3. Coming up with a different way to hold the information needed to hold the information needed to hold the data for your story.

There is also a library for creating text adventures that seems decent.  
See: https://github.com/lordmauve/adventurelib 
"""

import re
endTest = re.compile('THE END')

resultDict = dict()

sceneList = []
scene = []
with open('starTrek.txt') as starTrekText:
    for line in starTrekText:
        #print line
        lineSplit = line.split('|')
        scene.append(lineSplit[0].strip())
        lineSplit.pop(0)

        keyFlag = True
        for item in lineSplit:
            if keyFlag == True:
                key = item
                keyFlag = False
            else:
                resultDict[key.strip()]=item.strip()
                keyFlag = True
            #print lineSplit
            #resultDict.append(lineSplit[0] : lineSplit[1])
            #print resultDict
        scene.append(resultDict)
        resultDict = {}
        sceneList.append(scene)
        scene = []

#print sceneList
#print starTrekList[0][0]


# print answer

#print sceneList
sceneIndex = 0
endFlag = False

while endFlag == False:
    print (sceneList[sceneIndex][0])
    if endTest.search(sceneList[sceneIndex][0]) is not None:
        break
    answer = input("Enter command ")

    if answer in sceneList[sceneIndex][1]:
        #if sceneList[0][1][answer]
        try:
            sceneIndex = int(sceneList[sceneIndex][1][answer])
            #print type(sceneIndex)
            #print sceneIndex
            #print "try"
        except:
            print (sceneList[sceneIndex][1][answer])
            #print "except"

    else:
        print ("Subspace communication error, please try again. Type only CAPITAL letters of your chosen option, and check your spelling.")

#error checking
"""
if answer in sceneList:
    print (sceneList)
else:
    print ('Oh dear')

# errorCheck = answer in sceneList
# print errorCheck
"""