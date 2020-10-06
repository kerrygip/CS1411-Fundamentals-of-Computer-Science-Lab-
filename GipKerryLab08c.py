#Kerry Gip
#10/6/2020
#This program shows techniques of defining functions, parameter passing and
#function invocation

#double the values in a list

def doubleValue(value):
    
   #return (i*2 for i in value)
    for i in range(len(value)):
        value[i] = value[i] * 2
    return value   
    

def main():
    numberList = []
    for i in range(5):
        
        numbers = int(input("Please enter 5 numbers: "))
        numberList.append(numbers)

    print("The doubled numbers list is: ", doubleValue(numberList))
    
main()    
