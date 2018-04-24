#This program will convert an early modern (1582-1752) Gregorian calendar date into the Julian calendars of England or Scotland.

def calendarInput():
    #ask user for input and error check
    failure = 0
    try:
        #ask for month and check for validity
        GregorianMonth = int(raw_input('Enter a month in numerical form, e.g. "12" is December: '))
        if (GregorianMonth < 1 or GregorianMonth > 12):
            failure = "n"
            print("There are only 12 months in a year.")
            
        #ask for day and check for validity
        GregorianDay = int(raw_input('Enter a day: '))
        if (GregorianDay > 28 and GregorianMonth == 2):
            failure = "n"
            print("February only has 28 days.")
        elif ((GregorianDay == 31) and (GregorianMonth == 4 or GregorianMonth == 6 or GregorianMonth == 9 or GregorianMonth == 11)):
            GregorianYear = "error"
            print("That month only has 30 days.")
        elif (GregorianDay < 1 or GregorianDay > 31):
            failure = "n"
            print("There are between 1 and 31 days in a month.")
            
        #ask for year and check for validity
        GregorianYear = int(raw_input('Enter a year between 1582 and 1752: '))
        if (GregorianYear < 1582) or (GregorianYear > 1753):
            failure = "n"
            print("That is not a year between 1582 and 1752.")

    except ValueError:
        failure = "n"
        print("Please enter valid numbers.")
        
    #create a temporary placeholder day variable to convert from Gregorian to Julian date
    if (GregorianYear < 1700):
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
    print ("The date " + str(GregorianMonth) + "-" + str(GregorianDay) + "-" + str(GregorianYear) + " on the Continent was " + str(JulianMonth) + "-" + str(JulianDay) + "-" + str(JulianYear) + " in England")

    #add in the Scotland year
    if (JulianYear > 1599 and ((JulianMonth == 3 and JulianDay < 25) or (JulianMonth < 3))):
        ScottishYear = JulianYear - 1
        print ("and " + str(JulianMonth) + "-" + str(JulianDay) + "-" + str(ScottishYear) + " in Scotland.")

    return failure

failure = 0
while type(failure) is int:
	GregorianYear = calendarInput()

#the comment below is a description of the task

"""
After 1582, to convert from the Gregorian to Julian calendar requires subtracting 10 days. After the leap year in 1700, it requires subtracting 11. Also, the English New Year's Day is March 25th.
"""