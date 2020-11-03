def main():

    count = 0
    sum1 = 0
    infile = open ('data2.txt', 'r')

    line = infile.readline() 
    
    while line != "":
        my_list = line.split(', ')

        for num in my_list:
            
            sum1 = sum1 + float(num)
            count = count + 1
        line = infile.readline()
        average = sum1 / count

    print ('Number of data:', count)
    print ('Sum of numbers is:', sum1)
    print ('Average is: {0:.2f}'.format(average))
    
    infile.close()
