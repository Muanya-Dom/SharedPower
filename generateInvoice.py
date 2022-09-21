import sys
import sqlite3

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()

def invoice(customerId, email, username):

    #This code creates a text file called invoice
    invoice = open('Invoice.txt','w')

    total = 0.0
    
    details = '''<--Shared Power-->

**Invoice**
    
Customer No: %s
Email: %s
Username: %s


Order No.\t| Serial No.\t| Tool Name\t\t| Amount\t| No. of Days\t| Hire Date\t| Insurance
___________________________________________________________________________________________________________________
''' % (customerId, email, username)
    
    invoice.write(details)


    # Gets the tools the customer has hired from database hired tools table
    dbCursor.execute('SELECT * FROM hiredTool WHERE customer_id = ?', (customerId,))
    
    for row in dbCursor.fetchall():
        total = total + row[4]
        invoice.write('%s\t\t| %s\t\t| %s\t| £%s0\t| %s\t\t| %s\t| %s\n' % (row[0],row[2],row[3],row[4],row[5],row[6],row[7]))


    invoice.write('\n\nTotal Amount: £%s0' % (total))

    invoice.write('\n\n\n\nThank you for using Shared Power')
    invoice.write('\n\n© Copyright Shared Power')


    invoice.close()

    print('Invoice Generated Successfully')
    input('\nPress <ENTER> to continue: ')
    print()
    
    
