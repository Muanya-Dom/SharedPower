import sys
import time
import random
from datetime import date
import sqlite3
import dbInsert

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()

def tools(customerId):
    numberCount = 0
    orderNo = 0
    listOfSerialNo = []
    listOfToolName = []
    listOfPerDayRate = []
    listOfHalfDayRate = []
    serialNo = 0
    toolName = ''
    cost = 0.0
    noOfDays = 0.0
    dateOfHire = ''
    insurance = ''
    
    print('options\t| Tool Name \t\t | PerDay Rate \t | HalfDay Rate')
    
    # Get tools information from database tool table
    dbCursor.execute('SELECT * FROM tool')
    
    for row in dbCursor.fetchall():
        numberCount = numberCount + 1
        print('%s)\t| %s \t | £%s0 \t | £%s0' % (numberCount,row[1],row[3],row[4]))
        listOfSerialNo.append(row[0])
        listOfToolName.append(row[1])
        listOfPerDayRate.append(row[3])
        listOfHalfDayRate.append(row[4])

    # print code means new line
    print()

    # Validation
    conf = False
    while conf == False:
        
        # The input() code gets user input from the console
        userInput = input('Enter your choice of tool from the options above: ')

        try:
            # confirms if user input is an integer ()
            userInput = int(userInput)

            # gets to this code if the user input is integer
            # checks if user input is not in the options
            if userInput < 1 or userInput > numberCount:
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
                userInput = userInput - 1

                cost, insurance, noOfDays = toolsOptions(userInput,listOfPerDayRate,listOfHalfDayRate)
                serialNo = listOfSerialNo[userInput]
                toolName = listOfToolName[userInput]
                
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

    dateOfHire = date.today()
    noOfDays = int(noOfDays)
    
    # Gets the maximum value from the hired tool table and adds 999 to make a new order no
    dbCursor.execute('SELECT MAX(order_no) from hiredTool')
    
    for row in dbCursor.fetchall():
        orderNo = int(row[0] + 999)

    # Inserts users details into the database
    dbInsert.toHiredToolTable(orderNo, customerId, serialNo, toolName, cost, noOfDays, dateOfHire, insurance)

    print('The tool (',toolName,') has successfully been hired.');
    print('Total Cost: £',cost,)
    print('Payment successfully made')
    input('\nPress <ENTER> to continue: ')
    print()
    
    




# Function that returns three return values
def toolsOptions(number, perDayRate, halfDayRate):

    cost = 0.0
    insurance = ''
    
    rate = int(input('\nFor per day rate enter \"1\". For half day rate enter \"2\": '))
    if rate == 1:
        cost = perDayRate[number]
    elif rate == 2:
        cost = halfDayRate[number]


    noOfDays = float(input('\nEnter the number of days you would like to hire this tool: '))
    cost = cost * noOfDays


    postage = int(input('''\nDo you want to arrange a dispatch rider? An extra cost of £1 will be added.
    For yes enter \"1\".
    For No enter \"2\".
    Enter your choice: '''))
    if postage == 1:
        cost = cost + 1.0
        print('\nDispatch rider has been confirmed.')
    elif postage == 2:
        print('\nYou will have to pick the item up yourself.')


    insure = int(input('''\nWould you like to insure this tool? An extra cost of £5 will be added.
    For yes enter \"1\".
    For No enter \"2\".
    Enter your choice: '''))

    if insure == 1:
        cost = cost + 5.0
        insurance = 'yes'
        print('\nInsurance has been added.')
    elif insure == 2:
        insurance = 'no'
        print('\nYou have no insurance cover.')

    return cost, insurance, noOfDays



