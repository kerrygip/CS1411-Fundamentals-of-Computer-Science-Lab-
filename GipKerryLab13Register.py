#Kerry Gip
#11/10/2020
#Lab 13

from BankAccount import *

def main():
    #empty bank account object
    account = BankAccount()

    #Ask user for number of transactions
    transactions = int(input("How many transactions will you be making today?: "))                      
    

    for i in range(transactions):
        transactionType = input("\nWhat kind of transaction will you be making?"
                            "\n 1 for Deposit"
                            "\n 2 for Withdrawals or"
                            "\n 3 for Get Balance "
                                "\n")

        #deposit
        if (transactionType == "1"):
            depositAmount = float(input("\nHow much do you want to deposit?: "))
            account.deposit(depositAmount)
            
            print("\nYour new balanace is $", format(account.getBalance(),".2f")) 
                
        #withdraw
        elif (transactionType == "2"):
            withdrawAmount = float(input("\nHow much do you want to withdraw?: "))
            account.withdraw(withdrawAmount)
            
            print("\nYour new balanace is $", format(account.getBalance(),".2f"))
                
        #getBalance
        elif (transactionType == "3"):
            print("\nBalance is: $", format(account.getBalance(),".2f"))

        else:
            print("Invalid entry, try again")

       
            
    print("\nNet amount = $" ,format(account.getBalance(),".2f"))
    print("Total transactions completed is ", (transactions - account.reject))
    
                
main()
