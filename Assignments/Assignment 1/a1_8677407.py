# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 1


import math

############
# Question 1
############

def repeat(string, n, delim):
    '''str -> str
    Returns the string repeated n times, separated by the string delim'''
    
    a = ((string + delim) * (n-1) + string)
    return a

############
# Question 2
############

def is_prime(n):
    '''int -> bool
     Returns a boolean value indicating whether an integer is prime or not.'''
    
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
            else:
                return True
    
############
# Question 3
############

def points(x1,y1,x2,y2):
    '''[int,int,int,int] -> str
      Takes as input four numbers x1, y1, x2, y2 that are the coordinates of
      two points (x1;y1) and (x2; y2) in the plane. Prints the slope of the line
      going through the two points and the distance between the points.'''

    v = y2 - y1
    h = x2 - x1
    
    if (h == 0):
        slope = str("infinity")
        
    else:
        slope = v/h

    distance = math.sqrt((h**2) + (v**2))
    slope = str(slope)
    distance = str(distance)

    print("The slope is " + slope + " and the distance is " + distance)
        
############
# Question 4
############        

def month_apart(m1,d1,m2,d2):
    '''[int,int,int,int] -> bool
     Returns whether two dates are at least a month apart.'''

    if ((m1 > m2 + 1 or m1 < m2 - 1) or (m1 == m2 - 1 and d1 <= d2) or (m1 == m2 + 1 and d1 >= d2)):
        return True
    else:
        return False
    

############
# Question 5
############

def reverse_int(n):
    '''int -> int
     Reverses a 3 digit integer.'''

    a = (n%10)*100
    b = ((n//10)%10)*10
    c = ((n//10)//10)

    return a+b+c

############
# Question 6
############

def vowelCount(string):
    '''str -> str
     Returns the number of vowels in a string respectively.'''

    s = string.lower()
    
    a = string.count('a')
    e = string.count('e')
    i = string.count('i')
    o = string.count('o')
    u = string.count('u')

    a = str(a)
    e = str(e)
    i = str(i)
    o = str(0)
    u = str(u)
    


    print (" a, e, i, o, and u appear, respectively," + a + ',' + e + ',' + i + ',' + o + ',' + u + " times.")


############
# Question 7
############

def allTheSame(x, y, z):
    '''[int/str,int/str,int/str] -> bool
     Returns true if all arguments are the same.'''

    return x == y == z

def allDifferent(x, y, z):
    '''[int/str,int/str,int/str] -> bool
     Returns true if all arguments are different.'''

    return x != y != z

def sorted(x, y, z):
    '''[int/str,int/str,int/str] -> bool
     Returns true if all arguments are sorted, starting with smallest.'''
    
    return x <= y <= z

############
# Question 8
############

def leap(year):
    '''int -> bool
     Returns true if it is a leap year.'''

    if (year % 400 == 0):
        return True

    if (year % 100 == 0):
        return False

    if (year % 4 == 0):
        return True

    else:
        return False

############
# Question 9
############


def letter2number(g):
    '''str -> floats
     Returns corresponding number grade to letter grade.'''

    if g == 'A':
        g = 4
    
    elif g == 'B':
        g = 3

    elif g == 'C':
        g = 2

    elif g == 'D':
        g = 1.0

    elif g == 'F':
        g = 0
    
    elif g == 'B+':
        g = 3.3

    elif g == 'C+':
        g = 2.3

    elif g == 'D+':
        g = 1.3

    elif g == 'F+':
        g = 0.3

    elif g == 'A-':
        g = 3.7
    
    elif g == 'B-':
        g = 2.7

    elif g == 'C-':
        g = 1.7

    elif g == 'D+':
        g = 0.7

    return g


############
# Question 10
############

def is_palindrome(s):
    '''str -> str
     Returns if input is a palindrome.'''
    
    a = (s == s[::-1])

    return a

############
# Question 11
############

def is_nneg_float(s):
    '''float -> bool
     checks if string s denotes a nonnegative floating point value
     (not in scientific notation). .'''

    nS = s.replace(".","")
    if (nS.isdigit() == True) and (0 <= s.count(".") <= 1):

        return True
    else:
        return False
    
############
# Question 12
############

def rps(p1,p2):
    '''str -> int
    Takes the choice ('R', 'P', or 'S') of player 1 and the
    choice of player 2, and returns -1 if player 1 wins, 1 if player 2 wins, or 0 if there is a
    tie'''

    if p1 == 'R' and p2 == 'S' or p1 == 'P' and p2 == 'R' or p1 == 'S' and p2 == 'P' or  p1 == 'S' and p2 == 'P':
        return -1

    elif p1 == 'S' and p2 == 'R' or p1 == 'R' and p2 == 'P' or p1 == 'P' and p2 == 'S':
        return 1

    else:
        return 0


############
# Question 13
############

def alogical(n):
    '''float -> int
    Takes the choice ('R', 'P', or 'S') of player 1 and the
    choice of player 2, and returns -1 if player 1 wins, 1 if player 2 wins, or 0 if there is a
    tie'''

    m = math.log(n,2)
    return math.ceil(m)

############
# Question 14
############

def count_even_digits(n, length):
    '''[int,int] -> int
    Takes  two integers as parameters and returns the number of even-valued digits in the first number'''

    total = 0
    for i in range(0,length):
        d = (n % 10)
        n = (n // 10)
        if (d % 2 == 0):
            total = total + 1
    return total
    
