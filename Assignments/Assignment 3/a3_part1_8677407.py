# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 3

import math
import random

################# Question 1 #################

def coprime(x,y):
    '''
    (int,int) -> Boolean
    
    Returns True if two input integers are coprimes and false otherwise. 
    '''
  
    a = []
    b = []
    
    samefactor = 0
    
    for i in range(1,x+1):
        
        if x%i == 0:
            a.append(i)
            
    for j in range(1,y+1):
        
        if y%j == 0:
            b.append(j)


    for c in range(len(a)):
        for d in range(len(b)):
            
            if a[c] == b[d]:
                samefactor += 1

    return (samefactor == 1)


################# Question 2 #################

def all_coprime_pairs(L):
    '''
    (list) -> list of tuples

    Takes a list of distinct integers and returns a list containing pairs
    of numbers are tuples.
    '''

    pairs = []
    
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            
            a,b = L[i],L[j]
            if coprime(a,b) == True:
                pairs.append((a,b))

    return pairs
      

################# Question 3 #################    

def zero_out(a1, a2):
    '''
    (list of integers, list of integers) -> None

    Takes two lists of integers a1 & a2 and replaces any occurrences
    of a2 in a1 with zeroes.
    '''

    b = (len(a1) - len(a2))


    
    for i in range(0, b):
        total = 0
        
        for j in range(0, len (a2)):
            if (a1[i + j] == a2[j]):

                total += 1

        if (total == len(a2)):
            for j in range(0, len(a2)):
                
                a1[i + j] = 0

    return a1
    
################# Question 4 #################

def coin_flip(file_name):
    '''
    (file) -> strs

    Takes a list of distinct integers and returns a list containing pairs
    of numbers are tuples.
    '''

    a = open(file_name).readlines()

    for line in a:
        upper_line = line.upper()
        heads = 0
        total - 0

        for flip in upper_line:
            total += 1
            if (flip == "H"):
                heads += 1

        percent = 100 * heads/total
        rounded = round(10*percent)/10
        print (str(heads) + "heads (" + str(rounded) + "%)")
        if (percent > 50):
            print("You win!")
        print ()
        
        
################# Question 5 #################

def Run():
    '''
    (None)-> None
    
    Prints out 20 random die tosses in a list and prints the die values.
    '''
    
    a = []

    for i in range(21):
        a.append(random.randint(1,6))

    j = 0

    while j< len(a) - 2:
        i = j + 1

        if a[i] == a[j]:
            
            a.insert((j), "(")
            i += 1

            while(a[i] == a[j + 1]):
                i += 1
            a.insert((i), ")")
        j = i

    for i in range(21):
        
        if (a[0] == "("):
            print(str(a.pop(0)) + str(a.pop(0)), end = " ")
            i += 1

        elif(i < 20 and a[1] == ")"):
                  print(str(a.pop(0)) + str(a.pop()), end = " ")
        else:
            print(str(a.pop(0)) + " ", end = " ")
        
        
        
    
################# Question 6a #################

def craps():
    '''
    (None) -> int
    
    Returns 1 if player won Craps game, 0 if player lost
    
    '''
    
    dice = (random.randrange(1,7) + random.randrange(1,7))
    
    if dice in (2,3,12):
               
        return 0

    if dice in (7,11):
        
        return 1

    b = (random.randrange(1,7) + random.randrange(1,7))
    
    while b not in (7,dice):
        
        b = random.randrange(1,7) + random.randrange(1,7)

    if b == dice:
        
        return 1

    else:
        
        return  0

################# Question 6b #################

def testCraps(n):
    '''
    (None) -> int
    
    Takes a positive integer n as input,
    simulates n games of craps, and returns the fraction of games the player won
    
    '''
    

    a = []

    for i in range(n):
        x = craps()
        a.append(x)
    
    wins = a.count(1)

    b = (wins/len(a))

    return round(b,4)


################# Question 7 #################
    
def is_all_even(lis):
    '''
    (list) -> bool
    
    Returns True if elements in sublists are even and False otherwise
    
    '''
    a = 0
    
    for b in lis:
        for i in b:
            if i%2 != 0:
                a += 1
    
    if a > 0:
        return False
    else:
        return True
    
################# Question 8 #################

def Range(lis):
    '''
    (list) -> int
    Returns range of values contained in sublists of list L, defined as 1 more than the difference of the largest and smallest element
    
    '''
    minimum = []
    maximum = []
    
    if lis == []:
        return 0

    for l in lis:
        
        maximum.append(max(l))
        minimum.append(min(l))

    d = (max(maximum) - min(minimum)) + 1

    return d
    
