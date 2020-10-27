###########################################################################
# Name: Kerry Gip 
# Date: 10/27/2020
# This program will perform the following tasks:
#    1) It will ask user for a text file and a word within that text file
#    2) It will count the number of times that the word has
#       appeared in the file
###########################################################################



###########################################################################
# Function Name: main
# Description:
#    1. Ask the user for the name of the text file
#    2. Ask the user for a word to search the text file
#    3. It will display an error message if the text file is the filename
#       does not exist
# Parameter: none
#
###########################################################################


def main():
 
    count = 0
    error = True
    
    while error:
        try:
            infileName = input("Enter the file name: ")
            infile= open(infileName, "r")
            keyword = input("What is the keyword that you want to "
                            "search for?: ")
            error = False
        except FileNotFoundError:
            print("Invalid file name, try again")

    for line in infile:
        words = line.split()
        for duplicate in words:
            if duplicate == keyword:
                count = count+1
            
    
    print("The word:","'", keyword,"'", "has shown up ", count, "times")
main()            


#got me with the punctuation
#for line in infile:
    #found = line.find(keyword)
    #if found != -1 and found !=0:
        #count = count +1











            
            
