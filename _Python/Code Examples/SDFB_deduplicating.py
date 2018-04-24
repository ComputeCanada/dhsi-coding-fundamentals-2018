# This program will enable the user to identify duplicate entries in a .CSV of potential people to mass-add and the current SDFB_people.csv export.
# I really ought to rewrite it so that this exports to a .CSV for easy cross-reference, possibly with feedback on date type fields as well

def DuplicateFinder():
    # open and read necessary files
    with open('SDFB_people.csv') as OldPeopleFile, open('sdfb_fathers_forupload.csv') as NewPeopleFile:
        OldPeopleText = csv.DictReader(OldPeopleFile)
        NewPeopleText = csv.DictReader(NewPeopleFile)
            
        # for each potential new person
        for row in NewPeopleText:
            
            # create variables
            # odnb_id = row['odnb_id']
            last_name = row['last_name']
            first_name = row['first_name']
            birth_year = row['ext_birthdate']
            death_year = row['ext_deathdate']
                    
            # check if odnb_id unique # issue because matches blank ODNB IDs I think
            # for row in OldPeopleText:
                # if (row['ODNB ID']==odnb_id):
                    # print "ODNB ID " + odnb_id + " is already in the Six Degrees dataset."
                    # break
                
            # reset .csv file so can loop through again
            # OldPeopleFile.seek(0)
                        
            # check if first name / last name combo unique
            for row in OldPeopleText:
                if (row['Last Name']==last_name):
                    if (row['First Name']==first_name):
                        if (row['Extant Death Year']==death_year):
                            if (row['Extant Birth Year']==birth_year):
                                print first_name + " " + last_name + ", born in " + birth_year + ", dying in " + death_year + " is a duplicate. Confirm with SDFB ID " + row['SDFB Person ID']
                            #else:
                                #print first_name + " " + last_name + ", dying in " + death_year + " is probably a duplicate. Confirm with SDFB ID " + row['SDFB Person ID']
                        #else:
                             #print first_name + " " + last_name + " might be a duplicate. Confirm with SDFB ID " + row['SDFB Person ID']

            # reset .csv file so can loop through again
            OldPeopleFile.seek(0)
                
    print "Duplicate people checks are complete."
# end function      
            
if __name__ == "__main__":
    import csv
    
    DuplicateFinder()
    
    print "All error checks are complete."
    
# end program