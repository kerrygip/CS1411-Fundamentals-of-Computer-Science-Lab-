#Kerry Gip
#Sept 15,2020
#Description: Lab 05 Part II. This lab shows various operations of String data type

def main():
    firstName = input("Please enter your first name ")
    lastName = input("Please enter your last name ")
    print(" ")
    
    userName = lastName + firstName[0].lower()
    print("Your username is: ", userName)
    print(" ")

    email = firstName.lower() + "." + lastName.lower() +"@ucdenver.edu"
    print(email)

main()    
          
