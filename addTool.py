import sys
import dbInsert
import sqlite3


def addtools():

    conf = False
    while conf == False:
        # the code gets users input and adds the tool to the database
        try:
            tool_name = input('Enter Tool Name: ') 
            tool_category = input('Enter Tool Category: ')
            serial_no = int(input('Enter Tool Serial Number: '))
            half_day_rate = int(input('Enter the price for half a day: '))
            per_day_rate = half_day_rate * 2

            # if statement that displays an error if the required details are empty
            if tool_name == '' or tool_category == '':
                print('\nError!!! All fields are required!')

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
                dbInsert.insertToToolTable(serial_no , tool_name, tool_category, half_day_rate, per_day_rate)

                print('\nTool Created Successfully!');
                input('\nPress <ENTER> to continue: ')
                print()
                
                # exits the loop
                conf = True
        
        except ValueError:
            # Gets to this code if the user input is not an integer
            print('\nInvalid input. This field requires a number.')

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
        
