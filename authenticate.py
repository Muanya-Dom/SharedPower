import sys
import time
import sqlite3
import home

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()


def login():
    
    #Empty string variables
    email = ''
    username = ''
    password = ''
    customerId = 0
    
    confirm = False

    while confirm == False:

        isUserPresent = False
        
        email = input('Enter Your Email: ')
        password = input('Enter Your Password: ')

        print('Processing details... \n')
        time.sleep(1) #waits for 1 second

        if email == '' or password == '':
            print('\nError!!! All fields are required!')

            #Validation
            doYouWantToResult = False
                
            while doYouWantToResult == False:
                choice = input('Do you want to try again? (y/n): ')
                    
                if choice in ['y','Y','yes','YES','Yes']:
                    # user enters the email and password again
                    print('\n')
                    doYouWantToResult = True
                elif choice in ['n','N','no','NO','No']:
                    # back to the system options
                    print('\n')
                    doYouWantToResult = True
                    confirm = True
                    # returns to the main function i.e. starts all over again
                    return
        else:
            # Gets the customer_id, email ,username and password from the database customer table
            dbCursor.execute('SELECT * FROM customer')

            # checks if the user email and password is present in the database results
            for row in dbCursor.fetchall():
                if row[1] == email and row[3] == password:
                    # user has an account in the system
                    customerId = row[0]
                    username = row[2]
                    isUserPresent = True
                    break

            # confirms that the user does not have an account
            if isUserPresent == False:
                print('Incorrect Username or Password.')

                #Validation
                doYouWantToResult = False
                
                while doYouWantToResult == False:
                    choice = input('Do you want to try again? (y/n): ')
                    
                    if choice in ['y','Y','yes','YES','Yes']:
                        # user enters the email and password again
                        print('\n')
                        doYouWantToResult = True
                    elif choice in ['n','N','no','NO','No']:
                        # back to the system options
                        print('\n')
                        doYouWantToResult = True
                        confirm = True
                        # returns to the main function i.e. starts all over again
                        return
            else:
                # Login successful
                print('Hello ',username,' ◕‿◕')
                print()
                home.menu(customerId, email, username)
                confirm = True

