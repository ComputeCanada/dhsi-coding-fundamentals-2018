#This program will convert an early modern (1582-1752) Gregorian calendar date into the Julian calendars of England or Scotland.

import csv

def calendarInput():
    #ask user for input and error check
    try:
        #ask for complete date and check for validity
        GregorianDate = row[0]
        GregorianDate = GregorianDate.split("/")
        print(GregorianDate)

        #ask for month and check for validity
        GregorianMonth = int(GregorianDate[0])
        print(GregorianMonth)
        if (GregorianMonth < 1 or GregorianMonth > 12):
            print("There are only 12 months in a year.")
            
        #ask for day and check for validity
        GregorianDay = int(GregorianDate[1])
        print(GregorianDay)
        if (GregorianDay > 28 and GregorianMonth == 2):
            print("February only has 28 days.")
        elif ((GregorianDay == 31) and (GregorianMonth == 4 or GregorianMonth == 6 or GregorianMonth == 9 or GregorianMonth == 11)):
            GregorianYear = "error"
            print("That month only has 30 days.")
        elif (GregorianDay < 1 or GregorianDay > 31):
            print("There are between 1 and 31 days in a month.")
            
        #ask for year and check for validity
        GregorianYear = int(GregorianDate[2])
        print(GregorianYear)
        if (GregorianYear < 1582) or (GregorianYear > 1753):
            print("That is not a year between 1582 and 1752.")
        
        #create a temporary placeholder day variable to convert from Gregorian to Julian date
        if ((GregorianYear < 1700) or (GregorianYear == 1700 and GregorianMonth < 3)):
            tempDay = GregorianDay - 10
        else:
            tempDay = GregorianDay - 11
    
        #convert from Gregorian to Julian Year in the English calendar, whose New Year begins March 25
        if (GregorianMonth < 3) or (GregorianMonth == 3 and tempDay < 25):
            JulianYear = GregorianYear - 1
        else:
            JulianYear = GregorianYear
    
        #convert from Gregorian to Julian Month and Day
        if (tempDay > 0):
            JulianMonth = GregorianMonth
            JulianDay = tempDay
        else:
            JulianMonth = GregorianMonth - 1
            if (JulianMonth == 2 and (GregorianYear % 4) != 0): # year not divisible by 4, non-leap year
                JulianDay = 28 + tempDay
            elif (JulianMonth == 2 and (GregorianYear % 4) == 0): # year divisible by 4, leap year
                JulianDay = 29 + tempDay
            elif (JulianMonth == 4 or JulianMonth == 6 or JulianMonth == 9 or JulianMonth == 11):
                JulianDay = 30 + tempDay
            else:
                JulianDay = 31 + tempDay

        #sanity check on the month variable
        if (JulianMonth == 0):
            JulianMonth = 12

    	#provide human-readable output
        print ("The date " + str(GregorianMonth) + "/" + str(GregorianDay) + "/" + str(GregorianYear) + " on the Continent was " + str(JulianMonth) + "/" + str(JulianDay) + "/" + str(JulianYear) + " in England")

        #add in the Scotland year
        if (JulianYear > 1599 and ((JulianMonth == 3 and JulianDay < 25) or (JulianMonth < 3))):
            ScottishYear = JulianYear - 1
            print ("and " + str(JulianMonth) + "/" + str(JulianDay) + "/" + str(ScottishYear) + " in Scotland.")

        #write dates to csv
        convertedDatesFile.write(str(GregorianMonth) + "/" + str(GregorianDay) + "/" + str(GregorianYear) + "," + str(JulianMonth) + "/" + str(JulianDay) + "/" + str(JulianYear) + "," + str(JulianMonth) + "/" + str(JulianDay) + "/")
        if (JulianYear > 1599 and ((JulianMonth == 3 and JulianDay < 25) or (JulianMonth < 3))):
            convertedDatesFile.write(str(ScottishYear) + "\n")
        else:
            convertedDatesFile.write(str(JulianYear) + "\n")

    except ValueError:
        print("Header or row with invalid format was skipped.")

# open files and create Header Row for export .csv
originalDatesFile = open('originalDates.csv')
originalDatesReader = csv.reader(originalDatesFile)

convertedDatesFile = open('convertedDates.csv', 'w+')
convertedDatesFile.write('Gregorian Date,English Julian Date,Scottish Julian Date\n')
    
for row in originalDatesReader:
	GregorianYear = calendarInput()

# close files
originalDatesFile.close()
convertedDatesFile.close()

#the comment below is a description of the task

"""
After 1582, to convert from the Gregorian to Julian calendar requires subtracting 10 days. After the leap year in 1700, it requires subtracting 11. Also, the English New Year's Day is March 25th.
"""