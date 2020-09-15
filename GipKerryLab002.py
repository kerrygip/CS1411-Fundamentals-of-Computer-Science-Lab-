#
# Name: Kerry Gip and Senai Ghide
# Class 1400-004
# Due Date: 9/1/2020
# Description: This is lab 2. It takes a temperature in Fahrenheit and converts it to Celsius:
# It also queries the user for their name 


def main():
    
    #ask user for first and last names 
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    #now ask for temperature they want to convert
    fahrenheit = (int(input("What is the temperature in Fahrenheit that you want to convert to Celsius?: ")))
    
    
    #make a loop to repeat 10 times
    i = 1
    for i in range(10):
        celsius = (fahrenheit - 32) * (5/9)
        fahrenheit = fahrenheit + 1
        print(firstName, "", lastName, " The temperature is ", celsius, " C")
    
main()