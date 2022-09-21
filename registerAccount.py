import sys
import time
import random
import sqlite3
import dbInsert

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()

def createNewAccount():

    #Empty string variables
    username = ''
    email = ''
    password = ''
    re_enterPassword = ''

    confirm = False

    while confirm == False:

        isUserPresent = True
        
        email = input('Enter Your Email: ')
        username = input('Enter New Username: ')
        password = input('Enter New Password: ')
        re_enterPassword = input('Re-enter New Password: ')

        print('Processing details... \n')
        time.sleep(1) #waits for 1 second

        # if statement that displays an error if the email, passord and re_enterPassword is empty
        if username == '' or email == '' or password == '' or re_enterPassword == '':
            print('\nError!!! All fields are required!')

            # Validation
            doYouWantToResult = False
            while doYouWantToResult == False:
                choice = input('Do you want to try again? (y/n): ')
                if choice in ['y','Y','yes','YES','Yes']:
                    # user enters the information again
                    print()
                    doYouWantToResult = True
                elif choice in ['n','N','no','NO','No']:
                    # back to the system options
                    print()
                    doYouWantToResult = True
                    # returns to the main function i.e. starts all over again
                    return
        else:
            # if statement that displays an error if the password is not equal to the re_enterPassword
            if password != re_enterPassword:
                print('\nError!!! Password does not match.')
                
                # Validation
                doYouWantToResult = False
                while doYouWantToResult == False:
                    choice = input('Do you want to try again? (y/n): ')
                    if choice in ['y','Y','yes','YES','Yes']:
                        # user enters the information again
                        print()
                        doYouWantToResult = True
                    elif choice in ['n','N','no','NO','No']:
                        # back to the system options
                        print()
                        doYouWantToResult = True
                        # returns to the main function i.e. starts all over again
                        return
                    
            else:
                # cheking if email already exist in the database
                dbCursor.execute('SELECT email from customer')
                for row in dbCursor.fetchall():
                    if row[0] == email:
                        print('Error!!! Email already exist. Try again.')
                        isUserPresent = False

                        # Validation
                        doYouWantToResult = False
                        while doYouWantToResult == False:
                            choice = input('Do you want to try again? (y/n): ')
                            if choice in ['y','Y','yes','YES','Yes']:
                                # user enters the information again
                                print()
                                doYouWantToResult = True
                            elif choice in ['n','N','no','NO','No']:
                                # back to the system options
                                print()
                                doYouWantToResult = True
                                # returns to the main function i.e. starts all over again
                                return
                    
                        break


                if isUserPresent != False:
                    confirm = True

            
    customerId = 0

    # Gets the maximum value from the customer table and adds 99 to it in order to make a new customer id
    dbCursor.execute('SELECT MAX(customer_id) as customer_id from customer ')
    for row in dbCursor.fetchall():
        customerId = int(row[0] + 99)

    # Inserts users details into the database
    dbInsert.toCustomerTable(customerId, email, username, password)

    print('Account created successfully! \n');    
  
