# Transaction.py
# Author: Kerry Gip
# Date: 11/18/2020

class Transaction:
    """Transaction class which keep track of a bank transaction"""
       

    def __init__(self, date, transaction_type, amount):
        """Initialize instance variables date, type, and amount"""
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount

    def get_date (self):
        """Returns transaction date"""
        return self.date

    def get_transaction_type (self):
        """Returns transaction type"""
        return self.transaction_type

    def get_amount (self):
        """Returns transaction amount"""
        return self.amount

    #added format
    def __repr__(self):
        return '{}{}{}\n'.format(self.date,self.transaction_type, self.amount)
    
