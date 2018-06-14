# this is a program to convert Gregorian to Julian dates for dates between 1582 and 1752
# for simplicity, we assume the difference between them changes on 1/1/1700 (it really changes on Gregorian date 3/10/1700)

# import the module that lets us easily read csv's
import csv

# open csv file of dates and read in the dates; originalDatesReader is a list of lists
originalDatesFile = open("originalDates.csv")
originalDatesReader = csv.reader(originalDatesFile)

# create csv file where we will write the dates as we process them
newDatesFile = open("newDates.csv", "w")

# assuming the format of the dates is mm/dd/yyyy, split each date into month, day, year and make them integers
#we are looping through each list in originalDatesReader
for date in originalDatesReader:    

    #splitDate is a list of the 3 numbers separated by /                    
    splitDate = date[0].split("/")                      
    month = splitDate[0]
    day = splitDate[1]
    year = splitDate[2]
        
    # the computer is assuming everything is a string, so we convert the numbers into integers
    month = int(month)
    day = int(day)
    year = int(year)
    
    # if the year is before 1700, subtract 10 days; otherwise subtract 11 days
    if year < 1700:
        JulianDay = day - 10
    else:
        JulianDay = day - 11

    # if after subtracting, JulianDay is 0 or negative, subtract 1 from month; otherwise the month stays the same
    if JulianDay <= 0:
        JulianMonth = month - 1
    else:
        JulianMonth = month
    
    # if JulianMonth ends up equal to 0, make it 12 and subtract 1 from year; otherwise the year stays the same
    if JulianMonth == 0:
        JulianMonth = 12
        JulianYear = year - 1
    else:
        JulianYear = year

    # if JulianDay is 0 or negative, use JulianMonth variable to determine the actual day
    if JulianDay <= 0:
    
        #is JulianMonth in this list of 31-day months?
        if JulianMonth in [1,3,5,7,8,10,12]:
        
            #if so, add 31 to JulianDay and save that number in place of my original JulianDay            
            JulianDay = JulianDay + 31         
                     
        #if not, is it in this list of 30-day months?
        elif JulianMonth in [4,6,9,11]:     
                    
            #if so, add 30 to JulianDay and save that number in place of my original JulianDay
            JulianDay = JulianDay + 30   
               
        #I could have also used "else" here, but "elif" allows me to make clear this is for when JulianMonth is February              
        elif JulianMonth == 2:  
        
            #is year divisible by 4?                        
            if year % 4 == 0:     
            
                #if so, we are in a leap year and February has 29 days                      
                JulianDay = JulianDay + 29              
            else:
            
                #if not, February has 28 days
                JulianDay = JulianDay + 28              

    # send dates to a new csv file, reinserting them into mm/dd/yyyy format and putting one date on each line
    newDatesFile.write(str(JulianMonth) + "/" + str(JulianDay) + "/" + str(JulianYear)+"\r\n")

# close the files so we don't accidentally corrupt them or crash something
originalDatesFile.close()
newDatesFile.close()