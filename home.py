import sys
import time
import hireTools
import viewTools
import returnTools
import addTool
import generateInvoice
import systemExit


def menu(customerId, email, username):

    while True:
        # This code gives users the option to choose among the following options below.
        print('1)  View tools for hire')
        print('2)  Hire Tools')
        print('3)  Return Tools')
        print('4)  Generate Invoice')
        print('5)  Create tool')
        print('6)  Exit')

        # The input() code gets user input from the console
        # print code means new line
        print()
        userInput = input('Enter a number (1, 2, 3, 4, 5, or 6): ')

        print('Checking please wait...')
        time.sleep(1) #waits for 1 second
    
        try:
            # confirms if user input is an integer ()
            userInput = int(userInput)

            # gets to this code if the user input is integer
            # checks if user input is 1,2,3,4 or 5
            if userInput not in [1,2,3,4,5,6]:
                print('\nInvalid input. Please select from the options below:')
            elif userInput == 1:
                print('Completed\n')
                viewTools.toolsForHire()
            elif userInput == 2:
                print('Completed\n')
                hireTools.tools(customerId)
            elif userInput == 3:
                print('Completed\n')
                returnTools.tools(customerId)
            elif userInput == 4:
                print('Completed\n')
                generateInvoice.invoice(customerId, email, username)
            elif userInput == 5:
                print('Complete\n')
                addTool.addtools()
            elif userInput == 6:
                print('Completed\n')
                systemExit.close()
        except ValueError:
            # Gets to this code if the user input is not an integer
            print('\nInvalid input. Please select from the options below:')



