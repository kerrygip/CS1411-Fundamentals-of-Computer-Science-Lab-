#Kerry Gip
#9/22/2020
#Lab 06 - Part 2, Find the Caesar Cipher. We will be writing a program
#that can encode and decode Caesar Cipher
#ord converts charaver to number

#do not encode space - use strip
#upper and lower case matters so either if/else or force it all into lower

def main():
    #taking input data
    print("This is a sample Caesar Cipher code")
    string= input("Please enter a string: ")
    string = string.strip().replace(" ", "")
    print("Your string that will be encoded without spaces is ", string)
    key = eval(input("Please enter a key(number) to shift by: "))
    negativeKey = -key

    
    #encode,decode and normal empty lists to store the new data
    #encryption is c = (x + n) % 26(# of letters in alphabet)
    #where c is place value(encode) x is value of actual letter, n is key
    #97 is for lowercase
    #65 is for uppercase
    #decode is c = (x – n) % 26
    encode = " "
    decode = " "
    normal = " "

    
    for i in range(len(string)):
        char = string[i]

        if (char.isupper()): #for uppercase
            encode += chr((ord(char) + key - 65) % 26 + 65)
            decode += chr((ord(char) - key - 65) % 26 + 65)

        else:
            encode += chr((ord(char) + key - 97) % 26 + 97)
            decode += chr((ord(char) - key - 97) % 26 + 97)

    #to re-encode it back to normal    
    for i in range(len(encode)):
        char = encode[i]

        if (char.isupper()): #for uppercase
            normal += chr((ord(char) + negativeKey - 65) % 26 + 65)
        else:    
            normal += chr((ord(char) + negativeKey - 97) % 26 + 97)
        
    
    #print results
    print("The encoded message is: ", encode)
    print("The decoded message of ", string, " is: ", decode)
    print("The decoded message of what we encoded is: ", normal)
    
main()    


