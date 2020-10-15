#Kerry Gip
#10/13/2020
#Lab 9: This will read in a set of data from an input file and
#calculate sum, mean and std deviation then outputs the results


##############################################################
# Function Name: read_data
# Description: Reads a set of numbers from an input file.
# Parameter: file - name of the input file
# Returns list_of_numbers
##############################################################

def read_data(file):
    infile = open(file, "r")
    list_of_numbers = []
    for line in infile:
        number = int(line)
        list_of_numbers.append(number)
    return list_of_numbers


##############################################################
# Function Name: compute_sum
# Description: Calculates sum of numbers in list
# Parameter: file - list of numbers
# Returns total
##############################################################
     
def compute_sum(sumList):
    total = 0
    for i in sumList:
        total = total + i
    return total
    

##############################################################
# Function Name: compute_mean
# Description: Calculates average of numbers
# Parameter: numbers
# Returns average
##############################################################  
def compute_mean(meanList):
    length = len(meanList)
   
    average = compute_sum(meanList)/length

    return average

##############################################################
# Function Name: compute_std
# Description: Calculates standard deviation
# Parameter: numbers
# Returns std_dev
##############################################################

def compute_std(stdList):
    total = 0
    length = len(stdList)
    for num in stdList:
        deviation = compute_mean(stdList) - num
        sqDeviation = (deviation)**2
        total = total + sqDeviation
        
    result = total/(length-1)
    std_dev = (result)**0.5
    return std_dev


##############################################################
# Function Name: write_result
# Description: Writes result onto output file 
# Parameter: file
# Returns outfile 
##############################################################     
#write_result ("output1.txt", 55, 5.5, 3.0276503540974917)
def write_result(file, sumN, mean, std):
    outfile = open(file, "a")
  
    
    
    outfile.write("The sum is: " + format(sumN, ".2f")+ "\n")
    outfile.write("The mean is: " + format(mean, ".2f")+ "\n")
    outfile.write("The std deviation is: " + format(std, ".3f") + "\n")
          
    print("The outputs have been written to output file")
    outfile.close()

##############################################################
# Function Name: main
# Description: ask user for name of input and output files
#   use read_data, compute_sum, compute_mean, compute_sd and write_result
# Parameter: none
# Prints everything 
############################################################## 
def main():
    print("This program will read a set of numbers from an input file and \n"
          "calculate the sum, mean and standard deviation")
    
    infileName = input("What is the name of the file? ")
    outfileName = input("What is the name of the output file? ")

    my_list = []
    my_list = read_data(infileName)
    
    
    sume = compute_sum(my_list)
    mean = compute_mean(my_list)
    std = compute_std(my_list)
    write_result(outfileName, sume, mean, std)
    
    
          
    













    

    
    
