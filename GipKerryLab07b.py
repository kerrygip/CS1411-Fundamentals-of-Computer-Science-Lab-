#Kerry Gip
#9/29/2020
#Description: This program shows techniques of reading and writing text files in
#Python

def main():
        print("This program creates a file of emails and usernames from a file of names")

        infile = open("score.txt", "r")
        infileRead = infile.readlines()
        outfileName = input("What file should the usernames go in? ")

        outfile = open(outfileName, "w")
        

        #read usernames and read the next 5 scores from them and then
        #calcualte average
        total = 0
        #read the line until the first " " and output
        #then read the following scores and calculate average 
        for line in infileRead:
            #this is to just find the first name
            name = line.split(" ")#turns it into a string
            
            
            for i in range(1,6):
               total = int(name[i]) + total
               score = total/5
                #isdigit wont print since its a string 
                #to see if there is any numbers in it and divide by the size of
                #the entire thing, so can be more than 5 scores
                
            total =0    
            
            print(name[0] + " " , score)
            print(name[0] + " " , score, file = outfile)

        infile.close()
        outfile.close()
        print("Players and average score has been output to: ", outfileName)

main()        
    
