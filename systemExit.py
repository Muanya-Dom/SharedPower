import sys
import sqlite3

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()

def close():
    # boolean variable called 'confirmation' used to control the while loop (i.e. stops from looping indefinitly)
    conf = False

    # the controller variable lets you leave the while loop if it is True
    while conf == False:
        choice = input('Are you sure you want to exit? (y/n): ')

        if choice in ['y','Y','yes','YES','Yes']:
            print('\nSystem Exit')
            dbCursor.close()
            conn.close()
            # Exits the system
            sys.exit()
            conf = True
        elif choice in ['n','N','no','NO','No']:
            # back to the system options
            print()
            conf = True
