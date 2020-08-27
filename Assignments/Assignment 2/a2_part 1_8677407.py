# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 2

import math

################# Question 1 #################

def print_factors(n):
    ''' (int) -> (bool)
        Prints out all the factors of n,
        returning True if 2 is a factor of n and returning False otherwise. 
    '''

    lis = []
    
    for i in range (1,n+1):
        if n % i == 0:
            lis.append(i)
            
    print ('factors of', end = " ")
    print (n, end = " ")
    print ("=", end = " ")

    for item in lis:
        print(str(item),end = " ")

    print()
    
    return n % 2 == 0

################# Question 2 #################

def triangle(num):
    '''
    (int) -> None
    
    Prints a triangle of size*2-1 wide by size tall triangle of numbers

    Preconditions: num must be non-negative
    '''

    for i in range(1, num+1):
        
        print(" " * i, end = "")
        
        for j in range(i,((num * 2)-i)+1):
            if j > 9:

                print(j%10, end="")
                
            else:
                
                print(j, end="")
            
        print(" " * i)

################# Question 3 #################    

def approxPi(error):
     ''' (float) -> (float)

         Approximates the constant π within error
         until the difference between the current sum and the previous sum
         is no greater than error. 
    '''
     a = 4

     b = (4 - 4/3)

     sign = 1

     i = 5
    
     while error < abs(b-a):
        
        a, b = b, (b + ((sign*4)/i))

        i += 2

        sign *= -1
        
     return b

################# Question 4 #################

def is_fib_like(lst):
    ''' (list) -> (bool)

          Takes a list of integers as a parameter and that returns whether or
          not the sequence matches the pattern of the Fibonacci sequence 
    '''

    if (len(lst) <= 2):
        return True

    a = lst[0]
    b = lst[1]

    for item in lst[2:]:
        if(item != (a + b)):
            return False
        a = b
        b = item

    return True

################# Question 5 #################

def longest_name(n):
    ''' (int) -> (string)

         Reads names typed by the user and prints the longest name. 
    '''

    inputs = []

    for i in range(1, n+1):
        
        inputs.append(input('Name # ' + str(i) + '? '))

    length = 0
    longest = ''

    for item in inputs:

        if (len((item)) > length):

            length = len(item)
            longest = item

            a = longest.lower()
            a = longest.capitalize()
                       
         
    print (a + "'s" + ' name is longest')  
    
################# Question 6 #################

def encrypt(key,n):
    ''' (string,string) -> (string)

         Returns encryption of the clear text. 
    '''   

    
    a = str.maketrans("0123456789",key)
    return n.translate(a)
    
