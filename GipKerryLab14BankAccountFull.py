# BankAccount.py
# Author: Kerry Gip
# Date: 11/18/2020



#import Transaction class
from GipKerryLab14TransactionClass import *


def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data (list_of_transactions):
#bank_account_data.txt
    
    print ('Read Data Function')
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""

      # Ask user for name of the input file, read each line of the data,
    infileName = input("What is the name of the file you wish to enter?: ")

    #list_of_transactions = []
    #newList = []
    
    try:               
        infile = open(infileName, "r")
        for line in infile:
            # split line using colon (:) is delimiter,
            date, action, amount = line.split(":")
            date = int(date)
            amount = float(amount)

            # create transaction object
            transaction = Transaction(date,action,amount)
           
            # add to list of transaction
            list_of_transactions.append(transaction)
           

       #Display error message if the input file is not found.     
    except FileNotFoundError:
        print("File not found")
               
    infile.close()
    #return list_of_transactions
    
    


def display_list (list_of_transactions):
#bank_account_data.txt    
   """ Displays list of transactions """

   # Sort the list of transactions by date and display list of transactions
   # in form of a table
   # in ascending order 
   
   print('Display List Function')

   displayTransactions = Transaction("","",0)
   
   n = len(list_of_transactions)
        
   print("\nDate     Type    Amount($)")
   print("______________________________")

   #sort feature
   #list_of_transactions.sort(key = lambda list_of_transactions:(list_of_transactions.date))

   #Bubble Sort ascending 
   for i in range(n):
       swap = False
       
       for j in range(0,n-1):
           if list_of_transactions[j].date > list_of_transactions[j+1].date:
               displayTransactions.date = list_of_transactions[j].date
               displayTransactions.transaction_type = list_of_transactions[j].transaction_type
               displayTransactions.amount = list_of_transactions[j].amount
               
               list_of_transactions[j].date = list_of_transactions[j+1].date
               list_of_transactions[j].transaction_type = list_of_transactions[j+1].transaction_type
               list_of_transactions[j].amount = list_of_transactions[j+1].amount
               
               #displayTransactions.date = list_of_transactions[j].date
               #displayTransactions.transaction_type = list_of_transactions[j].transaction_type
               #displayTransactions.amount = list_of_transactions[j].amount
               
               list_of_transactions[j+1].date = displayTransactions.date
               list_of_transactions[j+1].transaction_type = displayTransactions.transaction_type
               list_of_transactions[j+1].amount = displayTransactions.amount

               swap = True
               
       if swap == False:
           break
        
   

   for i in range(n):       
       
       print(list_of_transactions[i].date,
             list_of_transactions[i].transaction_type,
             list_of_transactions[i].amount)
       
       
   print("______________________________")
   print("\nEnd of List")
   

def add_transaction (list_of_transactions):
    """Adds a new transaction to list of Transactions"""

    # Ask user for date, type, and amount of transaction, create a transaction
    # object and append it to the list of transactions.
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest
    #format to 2 decimal points
    print ('Add Transaction Function')

    newTransaction = Transaction("","",0)
    #newTransaction = read_data(list_of_transactions)
    balance = calculate_balance(list_of_transactions)


        
    date = int(input("Enter the date using format yyyymmdd: "))
        #if (len(date) != 8): cannort sort between > on int and str
            #print("invalid date entered")
        #else:
    newTransaction.date = date
    
        
           
    added = eval(input("What kind of transaction type do you want to add? "
                      "\n1). Deposit"
                      "\n2). Withdraw"
                      "\n3). Bank Charge"
                      "\n4). Interest"
                      "\n5). Exit"
                      "\nEnter a number: "))
        #deposit
    if (added == 1):
        depositAmount = eval(input("How much do you want to deposit?: "))
        if (depositAmount >0):
            balance = balance + depositAmount
            format(balance, ".2f")
            newTransaction.transaction_type = "deposit"
            newTransaction.amount = format(depositAmount, "0.2f")

                #added this one - need a way to call the previous list
        
                          
            
        else:
            print("Cannot deposit negative monies, that's impossible")

        #withdrawal                 
    elif (added ==2):
        withdrawAmount = eval(input("How much do you want to withdraw?: "))
        if (withdrawAmount > balance):
             print("You don't have that much money, try again next time")
        else:
                #allow withdrawal from balance
            balance = balance - withdrawAmount
            format(balance, ".2f")
            newTransaction.transaction_type = "withdraw"
            newTransaction.amount = format(withdrawAmount, ".2f")

            
                

        #Bank charge - what is bank charge? still have to ask for amount for bank charge
    elif (added == 3):
            
        bankCharge = eval(input("How much would you like to gift us?: "))
        balance = balance - bankCharge
        format(balance, ".2f")
        newTransaction.transaction_type = "Bank Charge"
        newTransaction.amount = format(bankCharge, ".2f")

       
            

        #interest        
    elif (added == 4):    
        interest = eval(input("How much would you like for us to pay you interest? In dollar amount: "))
        balance = balance + interest
        format(balance, "0.2f")
        newTransaction.transaction_type = "Interest"
        newTransaction.amount = format(interest, ".2f")

      
            
            

        #exit
    elif (added ==5):
        print("Goodbye")


        #otherwise
    else:
        print("Idk what you said, please try again")


        
    list_of_transactions.append(newTransaction)    
    #print(list_of_transactions)
    
def calculate_balance (list_of_transactions):
    
    

    """Calculates the current balance"""

    # Start with initializing balance to zero
    # For each transaction in the list of transactions you will
    # add the amount to balance if the transaction type is deposit or interest
    # subtract the amount if transaction type is withdraw or bank charge
    # Print the balance on the screen
    print ('Calculate Balance Function')
    balance = 0
    
    n = len(list_of_transactions)
    
    for i in range(n):
        balance = float(list_of_transactions[i].amount) + balance
    
    print("Your balance is: $"+str(format(balance,"0.2f")))
    return balance
    
        


def save_data (list_of_transactions):
    """ Saves list of transaction to a file"""
    
    # Ask user for name of the output file, sort the list of transactions by date
    # and save the data using the following format:
    # date:transaction_type:amount
    # Display a message that data was saved to the output file.
    print ('Save Data Function')
    outFileName = input("Please enter the name of output file: ")
    outFile = open(outFileName, "w")

    for i in list_of_transactions:
        outFile.write(str(i.date) + ":" + str(i.transaction_type) + ":" + format(i.amount, "0.2f" )+"\n")
    outFile.close()
    print("Your file has been saved to ", outFileName)

            
main()
