# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 4

import math

################# Question 1a #################

def largest_34(a):
    '''
    (list) -> int
    
    Returns the sum of the third and fourth largest values in the list.

    This will have running time of O(n) which is linear. The loop will run n times and the loop
    following that should run the same amount of time as n or less than because it is within the
    for loop.
    '''
  
    one = float("-1000000")
    two = float("-1000000")
    three = float("-1000000")
    four = float("-1000000")

    for n in a:
        
        if n >= one:
            four = three
            three = two
            one = n

        elif n >= two:
            four = three
            three = two
            two = n

        elif num >= three:
            four = three
            three = n

        elif num >= four:
            four = n

    return three + four

################# Question 1b #################

def largest_third(a):
    '''
    (list) -> int

    Computes the sum of the len(a)//3 of the largest values in the list a.

    The running time for this should be O(nlogn). The for loop should execute n times and the line following should execute n times. The lines assigning variable
    returning the total should have running time of 1.
    '''

    a.sort()
    b = len(a)//3
    c = a[len(a)-1]
    d = len(a)-1-n



################# Question 1c #################    

def third_at_least(a):
    '''
    (list) -> (Int or None)

    Returns a value in a that occurs at least len(a)//3 + 1
    times. If it doesn't exist, it returns none
    '''

    b = []

    for i in a:
        if a.count(i) >= len(a)//3) + 1:
            return i
    
    
################# Question 1d #################

def sum_tri(a,x):
    '''
    (list) -> bool

    Takes a list and returns True if there exists indices i,j, and k such that
    a[i] + a[j] + a[k] = x. If not, it will return False
    '''

    for i in a:
        for j in a:
            for k in a:
                if i + j + k == x:
                    return True
                else:
                    z = False
    return Z

        

    
