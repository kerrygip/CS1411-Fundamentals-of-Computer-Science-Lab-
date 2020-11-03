import random

def main():

    print('I will flip a coin 1000 times.'
          '\nGuess how many times it will come up heads.'
          '\n(Press enter to begin)')
    input()
    flips = 0
    heads = 0
    tails = 0
    while True:
        flips = flips +1
        coinFlip= random.randint(0, 1)
        
        if flips >1000:
            print("Done")
            break
            
        if coinFlip == 1:
            heads = heads + 1
            print ('Number of heads', heads)
            
        if flips == 100:
            print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
        if flips == 500:
            print('Half way done, and heads has come up ' + str(heads) + ' times.')    
        if flips == 900:
            print('900 flips and there have been ' + str(heads) + ' heads.')
        #for fun    
        elif random.randint(0,1) ==0:
            tails = tails +1
    print()
    print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
    print("Tails came up", tails, "times") 
    print('Were you close?')
