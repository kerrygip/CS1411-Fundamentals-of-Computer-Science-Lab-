###########################################################################
# Name: Kerry Gip
# Date: 10/20/2020
# This program will perform the following tasks:
#    1) It will ask user for the number of items purchased
#    2) It will calculate the discount percentage
#    3) It will then display the discount amount
#    4) It will calculate the total amount of the purchase after discount 
###########################################################################



##############################################################
# Function Name: discount_percentage
# Description: Calculate discount percentage after
#           recieving the total amount of packages purchased
#       Quantity            Discount
#       10-19               20%
#       20-49               30%
#       50-99               40%
#       100+                50%
#
# Parameter: quantity
# Returns percent
##############################################################

def discountPercentage(quantity):

    if quantity >0 and quantity <=9:
        percent = 0
        
    elif quantity >= 10 and quantity <= 19:
        percent = 20
    elif quantity >= 20 and quantity <= 49:
        percent = 30
    elif quantity >= 50 and quantity <= 99:
        percent = 40
    elif quantity >= 100:
        percent = 50
    else:
        percent = "None, you gave a bad number or non number"
        
    return percent



###########################################################################
# Function Name: main
# Description:  Ask the user for quantity
#               Display error if less than 0 or non number
#               Use discountPercentage to calculate discount percentage
#               Calculate amount(quantity *99)
#               Calculate discount amount(amount*discount percentage)/100))
#               Calculate total amount(amount-discount amount)
#               Display discount percent, amount of discount and total amount
# Use/try and except
#
# Parameter: None
# Returns None
###########################################################################

def main():
    try:
        quantity = int(input("What is the quantity of items you bought?: "))
        
        discount = discountPercentage(quantity)
        amount = quantity*99
        discountAmount = (amount*discount)/100
        total = amount-discountAmount

        print("Your discount is: ", discount, "%\n"
              "Your amount of discount is: $" + format(discountAmount, "0.2f"), "\n"
              "Your total amount is: $" + format(total,"0.2f"))

    except ValueError as err:
        print("The quantity entered is not a real quantity\n"
              "Please enter it again")
    except:
        print("Unknown error")
        

        

        












