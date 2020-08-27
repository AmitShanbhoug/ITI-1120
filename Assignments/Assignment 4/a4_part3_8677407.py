# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 4

import math

################# Question 1 #################

def overlap(a):
    '''
    (set of integers, list) -> set of integers
    
    Takes a set of integers and a list of integers and returns a new set containing values that appear in both. 
    '''
    
   

################# Question 2 #################

def digit_sum(n):
    '''
    (int) -> int
    
    Returns the sum of all digits in a integer n.
    
    '''
    
    if n <= 9:
        return n
    else:
        
        b = n % 10
        c = n//10
        
        return b + digit_sum(c)



################# Question 3 #################    

def digital_root(n):
    '''
    (int) -> int
    
    Returns the digital root of the number, n
    
    '''
    
    if n <= 9:
        return n
    else:
        return digital_root(digit_sum(n))
    


        

    
