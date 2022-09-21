import sys
import time
import random
from datetime import date
from datetime import datetime
import sqlite3
import dbInsert

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()


def tools(customerId):

    noOfToolsHired = 0
    orderNo = 0
    serialNo = 0
    toolName = ''
    noOfDays = 0
    dateOfHire = ''

    listOfOrderNo = []
    listOfSerialNo = []
    listOfToolName = []
    listOfNoOfDays = []
    listOfDateOfHire = []

    returnNo = 0
    dateOfReturn = ''
    daysUsed = 0
    daysOverdue = 0
    status = ''

    # Gets the tools the customer has hired from database hired tools table
    dbCursor.execute('SELECT * FROM hiredTool WHERE customer_id = ?', (customerId,))
        
    for row in dbCursor.fetchall():
        noOfToolsHired = noOfToolsHired + 1
        listOfOrderNo.append(row[0])
        listOfSerialNo.append(row[2])
        listOfToolName.append(row[3])
        listOfNoOfDays.append(row[5])
        listOfDateOfHire.append(row[6])

    if noOfToolsHired == 0:
        print('You have not yet hired any tools.')
        input('\nPress <ENTER> to continue: ')
        print()
    else:
        print('options\t| Order No.\t| Serial No.\t| Tool Name\t\t| Amount\t| No. of Days\t| Hire Date\t| Insurance')

        # Gets the tools the customer has hired from database hired tools table
        dbCursor.execute('SELECT * FROM hiredTool WHERE customer_id = ?', (customerId,))
        
        noOfToolsHired = 0
        for row in dbCursor.fetchall():
            noOfToolsHired = noOfToolsHired + 1
            print('%s)\t| %s\t\t| %s\t\t| %s\t| £%s0\t| %s\t\t| %s\t| %s\n' % (noOfToolsHired,row[0],row[2],row[3],row[4],row[5],row[6],row[7]))


        # Validation
        conf = False
        
        while conf == False:
            
            # The input() code gets user input from the console
            userInput = input('Enter your choice of tool to return from the options above: ')

            try:
                # confirms if user input is an integer ()
                userInput = int(userInput)

                # gets to this code if the user input is integer
                # checks if user input is not in the options
                if userInput < 1 or userInput > noOfToolsHired:
                    print('\nInvalid input. Please select from the options above')
                    
                    #Validation
                    doYouWantToResult = False
                    while doYouWantToResult == False:
                        choice = input('Do you want to continue? (y/n): ')
                        
                        if choice in ['y','Y','yes','YES','Yes']:
                            print('\n')
                            doYouWantToResult = True
                        elif choice in ['n','N','no','NO','No']:
                            print('\n')
                            doYouWantToResult = True
                            conf = True
                            # returns to the menu function i.e. starts all over again
                            return
                else:
                    # exits the loop
                    conf = True
                    
            except ValueError:
                # Gets to this code if the user input is not an integer
                print('\nInvalid input. Please select from the options above')

                #Validation
                doYouWantToResult = False
                while doYouWantToResult == False:
                    choice = input('Do you want to continue? (y/n): ')
                    
                    if choice in ['y','Y','yes','YES','Yes']:
                        print('\n')
                        doYouWantToResult = True
                    elif choice in ['n','N','no','NO','No']:
                        print('\n')
                        doYouWantToResult = True
                        conf = True
                        # returns to the menu function i.e. starts all over again
                        return


        # Cont.
        print('\nProcessing request...')
        time.sleep(2) #waits for 1 second
        
        userInput = userInput - 1

        orderNo = listOfOrderNo[userInput]
        serialNo = listOfSerialNo[userInput]
        toolName = listOfToolName[userInput]
        noOfDays = listOfNoOfDays[userInput]
        dateOfHire = listOfDateOfHire[userInput]

        # Gets the current date
        dateOfReturn = date.today()

        # Converts the string variable to a datatime
        dateOfHire = datetime.strptime(dateOfHire, '%Y-%m-%d')
        dateOfHire = dateOfHire.date()
                    
        delta = dateOfReturn - dateOfHire
        daysUsed = delta.days

        daysOverdue = daysUsed - noOfDays

        if daysOverdue > 0:
            status = 'Overdue'
        else:
            status = 'Ontime'

        # Gets the maximum value from the returned tool table and adds 999 to make a new return no
        dbCursor.execute('SELECT MAX(return_no) from returnedTool')
                    
        for row in dbCursor.fetchall():
            returnNo = int(row[0] + 999)

        
        # Inserts the tool to the returned tool table 
        dbInsert.toReturnedToolTable(returnNo, customerId, serialNo, toolName, dateOfReturn, daysUsed, status)
                
        # Delete the tool from the hired tool table
        dbCursor.execute('DELETE FROM hiredTool WHERE order_no = ?', (orderNo,))
        conn.commit()

        if daysOverdue > 0:
            print('\nOVERDUE - YOU HAVE BEEN FINED')
            print('Tools Returned Successfully')
        else:
            print('\nTools Returned Successfully')
                
        input('\nPress <ENTER> to continue: ')
        print()



