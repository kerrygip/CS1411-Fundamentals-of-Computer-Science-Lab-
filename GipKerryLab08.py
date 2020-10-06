#Kerry Gip
#10/6/2020
#This program shows techniques of defining functions, parameter passing and
#function invocation

#Convert date from mm/dd/yyyy to month, date, year

#use split #page 152 in the book

def dateConvert(date):
    monthStr, dayStr,yearStr = date.split("/")

    wordMonth = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct",
                 "Nov","Dec"]
    monthStr = wordMonth[int(monthStr)-1]
    newDate = monthStr + ". " + dayStr + "," + yearStr
    return newDate


#will take the date and convert it into a string 
def main():
    
    date = (input("Enter a date in mm/dd/yyyy format: "))
    print("The converted date is: ", dateConvert(date))
    
main()    
