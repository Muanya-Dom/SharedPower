# <----Shared Power System----->

import sys
import time
import authenticate
import viewTools
import registerAccount
import systemExit
import addTool


# System Introduction
# The \t (tab) code enables an indent in the introduction.
print('\t' *4 + 'WELCOME TO SHARED POWER')
print('\tThis program is an information system that helps you (tradesmen),')
print('\tshare expensive and specialist tools rather than buying them yourself. \n')

print('loading page...\n')
time.sleep(1) #waits for 1 second
    
              
#main function
def main():

    # indifinite while loop
    while True:
        # This code gives users the option to either login, view tools for hire, create new account or exist.
        print('1)  Login')
        print('2)  View tools for hire')
        print('3)  Create new account')
        print('4)  Exit')
        
        # The input() code gets user input from the console
        # \n code means new line
        print('\n')
        userInput = input('Enter a number (1, 2, 3 or 4): ')

        print('Checking please wait...')
        time.sleep(1) #waits for 1 second
    
        try:
            # confirms if user input is an integer ()
            userInput = int(userInput)

            # gets to this code if the user input is integer
            # checks if user input is 1,2,3 or 4
            if userInput not in [1,2,3,4]:
                print('\nInvalid input. Please select from the options below:')
            elif userInput == 1:
                print('Complete\n\tlogin to continue')
                authenticate.login()
            elif userInput == 2:
                print('Complete\n')
                viewTools.toolsForHire()
            elif userInput == 3:
                print('Complete\n')
                registerAccount.createNewAccount()
            elif userInput == 4:
                print('Complete\n')
                systemExit.close()
        except ValueError:
            # Gets to this code if the user input is not an integer
            print('\nInvalid input. Please select from the options below:')


# Program begins here
main()
