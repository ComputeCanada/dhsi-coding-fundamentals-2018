# This program will enable the user to identify entries in the SDFB export .csv's that reference invalid Foreign Keys, which is generally a sign that something was unapproved/made inactive and all its dependent data was not edited accordingly.
# NOTE1: user will need to uncomment out the function name (at the bottom of this file) that they wish to run.
# NOTE2: user may need to save automatically downloaded CSV's as "Windows CSV" for function to work, I should write an error message saying this or figure out how to use csv library to read the csvs as downloaded...

# This function lists all the Admin Users, for manual inspection

def Users():
    # open and read necessary files
    with open('SDFB_Users.csv') as UserFile:
        UserText = csv.DictReader(UserFile)
        
        # for each row, check to see if users have Admin status
        for row in UserText:
            if (row['User Type']=='Admin'):
                print row['First Name'] + " " + row['Last Name'] + ", User ID " + row['SDFB User ID'] + " is an Admin"

    print "Error checks involving Users with Admin status are complete."
# end function

# This function checks the validity of Relationship Category Assignments with respect to Relationship Categories and Relationship Types

def RelCategoryAssignments():
    # open and read necessary files
    with open('SDFB_RelCategoryAssignments.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
        
        with open('SDFB_RelationshipCategories.csv') as RelCatFile, open('SDFB_RelationshipTypes.csv') as RelTypeFile:
            RelCatText = csv.DictReader(RelCatFile)
            RelTypeText = csv.DictReader(RelTypeFile)
            
            # for each Relationship Category Assignment
            for row in AssignText:
                
                # create variables
                assignmentID = row['SDFB Assignment ID']
                rel_cat = row['Relationship Category ID']
                rel_type = row['Relationship Type ID']
                validRelCat = 'FALSE'
                validRelType = 'FALSE'
                
                # check if Relationship Category ID is a valid Foreign Key
                for row in RelCatText:
                    if (row['SDFB Relationship Category ID']==rel_cat):
                        validRelCat = 'TRUE'
                        break
                        
                # print error message if encounter invalid Relationship Category
                if (validRelCat == 'FALSE'):
                    print rel_cat + " is not a valid Relationship Category ID. Manually fix SDFB RelCatAssignment ID " + assignmentID
                    
                # reset .csv file so can loop through again
                RelCatFile.seek(0)
                
                # check if Relationship Type ID is a valid Foreign Key
                for row in RelTypeText:
                    if (row['SDFB Relationship Type ID']==rel_type):
                        validRelType = 'TRUE'
                        # break
                        
                # print error message if encounter invalid Relationship Type
                if (validRelType == 'FALSE'):
                    print rel_type + " is not a valid Relationship Type ID. Manually fix SDFB RelCatAssignment ID " + assignmentID
               
                # reset .csv file so can loop through again
                RelTypeFile.seek(0)
                
    print "Error checks involving Relationship Category Assignments are complete."
# end function      

# This function checks the validity of Inverse Relationship Type Assignments within the Relationship Types

def InverseRelTypes():
    # open and read necessary files
    with open('SDFB_Relationshiptypes.csv') as RelTypeFile:
        RelTypeText = csv.DictReader(RelTypeFile)
        
        # create a list of relationship types
        rel_types = []
        for row in RelTypeText:
            rel_types.append(row['SDFB Relationship Type ID'])
        
        # reset .csv file so can loop through again
        RelTypeFile.seek(0)
        
        # for each Relationship Type/Inverse
        for row in RelTypeText:
            # create variables
            original = row['SDFB Relationship Type ID']
            inverse = row['Relationship Type Inverse']
            validInverse = 'FALSE'
            
            # skip header row
            if (inverse == "Relationship Type Inverse"):
                break
            
            # check if Inverse Relationship Type ID is valid
            for relType in rel_types:
                if (relType == inverse):
                    validInverse = 'TRUE'
            
            # print error message if encounter invalid Relationship Type ID
            if (validInverse == 'FALSE'):
                print inverse + " is not a valid Relationship Type ID. Manually fix SDFB Relationship Type ID " + original

    print "Error checks involving Inverse Relationship Types are complete."      
# end function

# This function checks the validity of Relationships with respect to People

def Relationships():
    print "WARNING: The Relationships function will take a long time to run. Go get yourself a cup of coffee. Drink it. Maybe get another."
    # open and read necessary files
    with open('SDFB_people.csv') as PersonFile:
        PersonText = csv.DictReader(PersonFile)
        with open('SDFB_relationships_greater_than_100180000.csv') as AssignFile:
            AssignText = csv.DictReader(AssignFile)
            # for each Relationship
            for row in AssignText:
                # create variables
                assignmentID = row['SDFB Relationship ID']
                person1 = row['Person 1 ID']
                person2 = row['Person 2 ID']
                validPerson1 = 'FALSE'
                validPerson2 = 'FALSE'
                
                # check if Person 1 and Person 2 ID are valid Foreign Keys
                for row in PersonText:
                    if (row['SDFB Person ID']==person1):
                        validPerson1 = 'TRUE'
                    elif (row['SDFB Person ID']==person2):
                        validPerson2 = 'TRUE'

                # print error message if encounter invalid Relationship Category
                if (validPerson1 == 'FALSE'):
                    print person1 + " is not a valid Person ID. Manually fix SDFB Relationship ID " + assignmentID
                if (validPerson2 == 'FALSE'):
                    print person2 + " is not a valid Person ID. Manually fix SDFB Relationship ID " + assignmentID

                # print status message every 1000 relationships to keep the user from panicking
                if ((int(assignmentID) % 1000) == 0):
                    print "Checked through " + assignmentID
                    
                # reset .csv file so can loop through again
                PersonFile.seek(0)

    print "Error checks involving the newest (crowdsourced) Relationships are complete. If you wish to check older Relationships, please manually alter the function and rerun."   
# end function

# This function checks the validity of Relationship Type Assignments with respect to Relationship Types and has been split from RelTypeAssignments() for speed reasons

def RelTypes():
    # open and read necessary files
    with open('SDFB_Relationshiptypes.csv') as RelTypeFile:
        RelTypeText = csv.DictReader(RelTypeFile)
        
        # create a list of relationship types
        rel_types = []
        for row in RelTypeText:
            rel_types.append(row['SDFB Relationship Type ID'])
    
    # create an array of Relationship Type Assignment files
    AllFiles = ['SDFB_RelTypeAssignments_00000_20000.csv', 'SDFB_RelTypeAssignments_20001_40000.csv', 'SDFB_RelTypeAssignments_40001_60000.csv', 'SDFB_RelTypeAssignments_60001_80000.csv', 'SDFB_RelTypeAssignments_80001_100000.csv', 'SDFB_RelTypeAssignments_100001_120000.csv', 'SDFB_RelTypeAssignments_120001_140000.csv', 'SDFB_RelTypeAssignments_140001_160000.csv', 'SDFB_RelTypeAssignments_160001_180000.csv', 'SDFB_RelTypeAssignments_greater_than_180000.csv']
    
    # for each Relationship Type Assignment file
    for file in AllFiles:
        with open(file) as AssignFile:
            AssignText = csv.DictReader(AssignFile)
         
            # for each Relationship Type Assignment
            for row in AssignText:
                # create variables
                assignmentID = row['SDFB Relationship Type Assignment ID']
                rel_type = row['SDFB Relationship Type ID']
                validRelType = 'FALSE'
            
                # check if Relationship Type ID is a valid Foreign Key
                for id in rel_types:
                    if (id==rel_type):
                        validRelType = 'TRUE'
                        #break # I don't know why this break statement is causing issues

                # print error message if encounter invalid Relationship Category
                if (validRelType == 'FALSE'):
                    print rel_type + " is not a valid Relationship Type ID. Manually fix SDFB Relationship Type Assignment ID " + assignmentID

    print "Error checks involving the Relationship Type Assignments and Relationship Types are complete."   
# end function


# This function checks the validity of Relationship Type Assignments with respect to Relationships and has been split from RelTypes() for speed reasons

def RelTypeAssignments():
    print "WARNING: The Relationships Type Assignments function will take a long time to run. Go take your lunch break."
    # open and read necessary files
    with open('SDFB_RelTypeAssignments_160001_180000.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
 
        # for each Relationship Type Assignment
        for row in AssignText:
            # create variables
            assignmentID = row['SDFB Relationship Type Assignment ID']
            rel = row['SDFB Relationship ID']
            validRel = 'FALSE'
            
            # search for rel in relationship files
            if (int(rel) < 100020001):
                file = 'SDFB_relationships_100000000_100020000.csv'
            elif (int(rel) < 100040001):
                file = 'SDFB_relationships_100020001_100040000.csv'
            elif (int(rel) < 100060001):
                file = 'SDFB_relationships_100040001_100060000.csv'
            elif (int(rel) < 100080001):
                file = 'SDFB_relationships_100060001_100080000.csv'
            elif (int(rel) < 100100001):
                file = 'SDFB_relationships_100080001_100100000.csv'
            elif (int(rel) < 100120001):
                file = 'SDFB_relationships_100100001_100120000.csv'
            elif (int(rel) < 100140001):
                file = 'SDFB_relationships_100120001_100140000.csv'  
            elif (int(rel) < 100160001):
                file = 'SDFB_relationships_100140001_100160000.csv'    
            elif (int(rel) < 100180001):
                file = 'SDFB_relationships_100160001_100180000.csv'
            else:
                file = 'SDFB_relationships_greater_than_100180000.csv'
                
            with open(file) as RelFile:
                RelText = csv.DictReader(RelFile)
            
                # check if Relationship ID is a valid Foreign Key
                for row in RelText:
                    if (row['SDFB Relationship ID']==rel):
                        validRel = 'TRUE'
                        #break # I don't know why this break statement is causing issues

                # print error message if encounter invalid Relationship Category
                if (validRel == 'FALSE'):
                    print rel + " is not a valid Relationship ID. Manually fix SDFB Relationship Type Assignment ID " + assignmentID

                # print status message every 500 relationships to keep the user from panicking
                if ((int(assignmentID) % 500) == 0):
                    print "Checked through " + assignmentID

                # reset .csv file so can loop through again
                RelFile.seek(0)

    print "Error checks involving the newest ~20,000 Relationship Type Assignments and Relationships are complete. If you wish to check older Relationship Type Assignments, please manually alter the function and rerun."   
# end function

# This function checks the validity of Group Category Assignments with respect to Group Categories and Groups

def GroupCategoryAssignments():
    # open and read necessary files
    with open('SDFB_GroupCategoryAssignments.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
        
        with open('SDFB_GroupCategories.csv') as GroupCatFile, open('SDFB_groups.csv') as GroupFile:
            GroupCatText = csv.DictReader(GroupCatFile)
            GroupText = csv.DictReader(GroupFile)
            
            # for each Group Category Assignment
            for row in AssignText:
                
                # create variables
                assignmentID = row['SDFB Assignment ID']
                group_cat = row['Group Category ID']
                group = row['Group ID']
                validGroupCat = 'FALSE'
                validGroup = 'FALSE'
                
                # check if Group Category ID is a valid Foreign Key
                for row in GroupCatText:
                    if (row['SDFB Group Category ID']==group_cat):
                        validGroupCat = 'TRUE'
                        break
                        
                # print error message if encounter invalid Relationship Category
                if (validGroupCat == 'FALSE'):
                    print group_cat + " is not a valid Group Category ID. Manually fix SDFB GroupCatAssignment ID " + assignmentID
                    
                # reset .csv file so can loop through again
                GroupCatFile.seek(0)
                
                # check if Group ID is a valid Foreign Key
                for row in GroupText:
                    if (row['SDFB Group ID']==group):
                        validGroup = 'TRUE'
                        break
                        
                # print error message if encounter invalid Group
                if (validGroup == 'FALSE'):
                    print group + " is not a valid Group ID. Manually fix SDFB GroupCatAssignment ID " + assignmentID
               
                # reset .csv file so can loop through again
                GroupFile.seek(0)
                
    print "Error checks involving Group Category Assignments are complete."
# end function
            
# This function checks the validity of Group Assignments with respect to Groups and People

def GroupAssignments():
    print "WARNING: The Group Assignments function will take a while to run. Time to procrastinate on Twitter!"
    # open and read necessary files
    with open('SDFB_GroupAssignments.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
        
        with open('SDFB_people.csv') as PersonFile, open('SDFB_groups.csv') as GroupFile:
            PersonText = csv.DictReader(PersonFile)
            GroupText = csv.DictReader(GroupFile)
            
            # for each Group Assignment
            for row in AssignText:
                
                # create variables
                assignmentID = row['SDFB Group Assignment ID']
                person = row['Person ID']
                group = row['Group ID']
                validPerson = 'FALSE'
                validGroup = 'FALSE'
                
                # check if Person ID is a valid Foreign Key
                for row in PersonText:
                    if (row['SDFB Person ID']==person):
                        validPerson = 'TRUE'
                        break
                        
                # print error message if encounter invalid Relationship Category
                if (validPerson == 'FALSE'):
                    print person + " is not a valid Person ID. Manually fix SDFB GroupAssignment ID " + assignmentID
                    
                # reset .csv file so can loop through again
                PersonFile.seek(0)
                
                # check if Group ID is a valid Foreign Key
                for row in GroupText:
                    if (row['SDFB Group ID']==group):
                        validGroup = 'TRUE'
                        break
                        
                # print error message if encounter invalid Group
                if (validGroup == 'FALSE'):
                    print group + " is not a valid Group ID. Manually fix SDFB GroupAssignment ID " + assignmentID
               
                # reset .csv file so can loop through again
                GroupFile.seek(0)
                
    print "Error checks involving Group Assignments are complete."
# end function

# This function checks the validity of Group Notes with respect to Groups

def GroupNotes():
    # open and read necessary files
    with open('SDFB_GroupNotes.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
        
        with open('SDFB_groups.csv') as GroupFile:
            GroupText = csv.DictReader(GroupFile)
            
            # for each Group Note
            for row in AssignText:
                
                # create variables
                assignmentID = row['SDFB Contribution ID']
                group = row['Group ID']
                validGroup = 'FALSE'
                
                # check if Group ID is a valid Foreign Key
                for row in GroupText:
                    if (row['SDFB Group ID']==group):
                        validGroup = 'TRUE'
                        break
                        
                # print error message if encounter invalid Group
                if (validGroup == 'FALSE'):
                    print group + " is not a valid Group ID. Manually fix SDFB GroupNote ID " + assignmentID
               
                # reset .csv file so can loop through again
                GroupFile.seek(0)
                
    print "Error checks involving Group Notes are complete. Note: these are often worth reading manually as a source of user-identified errors."
# end function

# This function checks the validity of Person Notes with respect to People

def PersonNotes():
    print "WARNING: The Person Notes function will take a while to run. Go check your email or something."
    # open and read necessary files
    with open('SDFB_PersonNotes.csv') as AssignFile:
        AssignText = csv.DictReader(AssignFile)
        
        with open('SDFB_people.csv') as PersonFile:
            PersonText = csv.DictReader(PersonFile)
            
            # for each Person Note
            for row in AssignText:
                
                # create variables
                assignmentID = row['SDFB Contribution ID']
                person = row['Person ID']
                validPerson = 'FALSE'
                
                # check if Person ID is a valid Foreign Key
                for row in PersonText:
                    if (row['SDFB Person ID']==person):
                        validPerson = 'TRUE'
                        break
                        
                # print error message if encounter invalid Relationship Category
                if (validPerson == 'FALSE'):
                    print person + " is not a valid Person ID. Manually fix SDFB Person Note ID " + assignmentID
                    
                # reset .csv file so can loop through again
                PersonFile.seek(0)
                
    print "Error checks involving People Notes are complete. Note: these are often worth reading manually as a source of user-identified errors."
# end function
            
if __name__ == "__main__":
    import csv
    
    #Users()
    #RelCategoryAssignments()
    #InverseRelTypes()
    #Relationships()
    RelTypes()
    #RelTypeAssignments()
    #GroupCategoryAssignments()
    #GroupAssignments()
    #GroupNotes()
    #PersonNotes()
    
    print "All error checks are complete."
    
# end program