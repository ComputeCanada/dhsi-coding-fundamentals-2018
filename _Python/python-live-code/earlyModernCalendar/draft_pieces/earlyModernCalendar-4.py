#This program will convert an early modern (1582-1752) Gregorian calendar date into the Julian calendars of England or Scotland.

#ask user for input and error check
try:
    #ask for month and check for validity
    GregorianMonth = int(raw_input('Enter a month in numerical form, e.g. "12" is December: '))
    if (GregorianMonth < 1 or GregorianMonth > 12):
        print("There are only 12 months in a year.")
        
    #ask for day and check for validity
    GregorianDay = int(raw_input('Enter a day: '))
    if (GregorianDay > 28 and GregorianMonth == 2):
        print("February only has 28 days.")
    elif ((GregorianDay == 31) and (GregorianMonth == 4 or GregorianMonth == 6 or GregorianMonth == 9 or GregorianMonth == 11)):
        GregorianYear = "error"
        print("That month only has 30 days.")
    elif (GregorianDay < 1 or GregorianDay > 31):
        print("There are between 1 and 31 days in a month.")
        
    #ask for year and check for validity
    GregorianYear = int(raw_input('Enter a year between 1582 and 1752: '))
    if (GregorianYear < 1582) or (GregorianYear > 1753):
        print("That is not a year between 1582 and 1752.")

except ValueError:
    print("Please enter valid numbers.")
    
#determine how many days must be subtracted to convert from Gregorian to Julian date
if (GregorianYear < 1700 or (GregorianYear == 1700 and GregorianMonth < 3)):
    tempDay = GregorianDay - 10
else:
    tempDay = GregorianDay - 11

#convert from Gregorian to Julian Year in the English calendar, whose New Year begins March 25
if (GregorianMonth < 3) or (GregorianMonth == 3 and tempDay < 25):
    JulianYear = GregorianYear - 1
else:
    JulianYear = GregorianYear

#provide human-readable output

#run repeatedly if user requests