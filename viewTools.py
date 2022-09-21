import sys
import sqlite3


# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()


def toolsForHire():

    print('SR. No \t | Tool Name \t\t | Category \t | PerDay Rate \t | HalfDay Rate')
    
    # Get tools information from database tool table
    dbCursor.execute('SELECT * FROM tool')
    
    for row in dbCursor.fetchall():
        print('%s \t | %s \t | %s \t | £%s0 \t | £%s0' % (row[0],row[1],row[2],row[3],row[4]))


    input('\nPress <ENTER> to continue: ')
    print()
