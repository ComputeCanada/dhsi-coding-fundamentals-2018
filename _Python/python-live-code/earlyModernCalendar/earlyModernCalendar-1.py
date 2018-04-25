#This program will convert an early modern (1582-1752) Gregorian calendar date into the Julian calendars of England or Scotland.

try:
    #ask for month and check for validity
    GregorianMonth = int(raw_input('Enter a month in numerical form, e.g. "12" is December: '))
            
    #ask for day and check for validity
    GregorianDay = int(raw_input('Enter a day: '))
            
    #ask for year and check for validity
    GregorianYear = int(raw_input('Enter a year between 1582 and 1752: '))

except ValueError:
    print("Please enter valid numbers.")
        
#determine how many days must be subtracted to convert from Gregorian to Julian date

#convert from Gregorian to Julian Year in the English calendar, whose New Year begins March 25
#convert from Gregorian to Julian Month and Day
#sanity check on the month variable

#provide human-readable output

#run repeatedly if user requests
