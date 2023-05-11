# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 2


import math

############################## 2.1 ############################################

def min_enclosing_rectangle(r,x,y):
    
    ''' The function has 3 parameters, r (radius of a circle ), x and y
        (coordinates of the center of the circle). This function will
        calculate the smallest axis aligned rectangle that contains the circle.

        (number,number,number) -> number,number

        Precondition: The radius must be positive.
    '''
       
    min_x = x - r
    min_y = y - r

    if r >= 0:
        return (min_x,min_y)

# if r < 0, the function won't go to the return line and instead will return nothing.

############################## 2.2 ############################################

def series_sum():

    ''' The function asks the user to input a non-negative integer. With this integer
        the function will calculate the sum of the series (1000 + (1/1^2 + 1/2^2 ... 1/n^2)).

         (None) -> Number

         Precondition: The input must be a positive integer.     
    '''

    q = int(input("Please enter a non-negative ineteger: "))
    ans = 1000 #1000 is the constant at the begining of the problem
    
    if q < 0:
        return None

    else:
        for i in range(q):
            ans += 1/((i+1)**2) 
        return ans

############################## 2.3 ############################################ 

def pell(n):

    ''' The function has an input 'n', from which the function calculates the pell number of it.

        (int) -> int

        Precondition: The input must be positive.
    '''

    if n < 0: 
        return None

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    if (n > 1):

        a = 0
        b = 1
    for x in range(0, n+1):
        atmp = a
        a = 2 * a + b
        b = atmp
    return b

############################## 2.4 ############################################

def countMembers(s):

    '''The function returns the number of characters in s, that are extraordinary(lower case e and j (inclusive), the upper case letters between F and X
       (inclusive), 2-6 (inclusive), and !,',', \.

        (str) -> int    
    '''

    c = 0
    for char in s:
        if char in ("efghijFGHIJKLMNOPQRSTUVWX23456!,\\"):
            c += 1
    return c

############################## 2.5 ############################################         

def casual_number(s):
    ''' The function returns an integer representing a number in s. If s does not look like a number the function will return none.

        Precondition: The string must be a number
    '''

    a = s.replace(",", "")
    b = a.replace("-", "", 1)

    if b.isnumeric():
            return int(a)
    else:
            return None

############################## 2.6 ############################################

def alienNumbers(s):
    ''' The function returns the numeric value of the number that s represents in the alien numbering system.

        (str) -> int

        Precondition: None
    '''

    i = 0
    for char in s:
        if ((s.count("T") or s.count("y") or s.count("!") or s.count("a") or s.count("N") or s.count("U")) >= 0):

            a = (s.count("T") * 1024)
            b = (s.count("y") * 598)
            c = (s.count("!") * 121)
            d = (s.count("a") * 42)
            e = (s.count("N") * 6)
            f = (s.count("U") * 1)
            i += (a+b+c+d+e+f)
        return i

    else:
        return 0

############################## 2.7 ############################################ 

def alienNumbersAgain(s):
    ''' The function returns the numeric value of the number that s represents in the alien numbering system.

        (str) -> int

        Precondition: Cannot use string method
    '''

    i = 0
    for char in s:

        if char == "T":
            i += 1024
        elif char == "y":
            i += 598
        elif char == "!":
            i += 121
        elif char == "a":
            i += 42
        elif char == "N":
            i += 6
        elif char == "U":
            i += 1
    return i

############################## 2.8 ###########################################

def encrypt(s):
    """
        Function that returns a string which is the encrypted version of s.

        (str) -> str
    """

    add = ""
    sol = ""
    
    add += s[((len(s) - 1) // 2)]

    s = s[::-1]
    
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            add += (s[i] + s[-1 - i])
    else:
        for i in range((len(s) // 2)):
            add += (s[i] + s[-1 - i])
        sol += add
        
    return sol

############################## 2.9 ###########################################

def o_pify(s):
    """
        This function considers every pair of consecutive characters in s and follows the conventions.

        (str) -> str
    """
    a = 0
    s = list(s)
    output = ""

    for char in s:
        if len(s) == 1:
            for item in s:
                output += item
            return output
