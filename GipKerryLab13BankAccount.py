#Bank Account Class
#Kerry Gip
#Lab 13
#11/10/2020



class BankAccount:
    """Every bank account has a balance, deposit, withdraw and
    getBalance funciton"""

    def __init__(self):
        """Initialize balance to 0"""
        self.balance = 0
        self.reject = 0

    def deposit(self,amount):
        """Increase value of balance by deposit"""
        if amount >0:
            self.balance = self.balance + amount
            print("You deposited: ", format(amount,".2f"))
            return True
            
        else:
            print("Invalid deposit. Transaction Declined.")
            self.reject +=1
            return False
        
        
    def withdraw(self, amount):
        """Decrease value of balance by withdrawal"""
        if amount > self.balance:
            print("Insufficient balance. Transaction Declined")
            self.reject +=1
            return False
        
        else:
            self.balance = self.balance - amount
            print("You withdrew: ", format(amount,".2f"))
            return True
            
          
    
    def getBalance(self):
        """Return current account balance"""
        return self.balance
        
    def reject():
        return int(self.reject)
