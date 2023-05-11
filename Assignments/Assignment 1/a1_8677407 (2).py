#Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 1

import math
import turtle 


############################################################################### Question 1 ###########################################################################################

def pythagorean_pair(a,b):
    """
        Calculates if 2 integers provided by the user are part of a pythagorean pair. This is done by using the pythagorean theorem to calculate the c value,
        and checks if the c value is an integer by ensuring it's modulus is 0.

        [int,int] -> boolean

    """ 
    
    c = math.sqrt(a**2 + b**2)
    return c % 1 == 0 #takes the modulus of c. if it is an integer, there shouldnn't be a modulus as there is no decimal value.

############################################################################### Question 2 ###########################################################################################

def mh2kh(s):
    """
        Converts speed from miles per hour to kilometres per hour.

        [int] -> int

    """
        
    kh = s*1.60934 #the exact value is based on the example code 

    return kh

############################################################################### Question 3 ###########################################################################################

def in_out(xs,ys,side):
    """

        Given a coordinate (bottom left corner) and a side length of a square, the function calculates whether a user provided query coordinate is within the square.
        The function establishes the max and min points of the square and checks whether the user inputted query points fall within it

        [number, number, number] -> boolean

    """

    max_x = (xs + side)
    max_y = (ys + side)
    min_x = (xs)
    min_y = (ys)
    
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    
    return min_x <= x <= max_x and min_y <= y <= max_y

############################################################################### Question 4 ###########################################################################################
 
def safe(n):
    """
        Precondition: 'n' must be a non-negative integer and at most has 2 digits.

        Given a non-negative integer, the function checks whether the number doesn't contain 9 as a digit or is divisible by 9. By taking the modulus,
        the functions checks whether it is divisible.

        [int] -> boolean
    
    """

    divisibility = not ((n//10 == 9) or (n%10 == 9) or (n%9 == 0))
    
    return divisibility 

############################################################################### Question 5 ###########################################################################################
 
def quote_maker(quote,name,year):
    """
        The function returns a sentence stating a quote, it's author and when it was said. The format of the string is: In 'year',  person called 'name' said: "quote"

        [string, string, int] -> string


    """
    
    return 'In ' + str(year) + ',' + ' ' + 'a person called ' + (name) + ' ' + 'said:' + ' ' + '"' + (quote) + '"'

############################################################################### Question 6 ###########################################################################################

def quote_displayer():
    """
        The function prompts the user for a quote and makes a call to the previous function (quote_maker)to print a statement containing a quote, its author and when it was said.

        [None] -> String

    """
    
    x = input("Give me a quote: ")
    y = input("Who said that? ")
    z = input ("What year did she/he say that? ")
    
    print(quote_maker(x,y,z))
    
############################################################################### Question 7 ###########################################################################################

def rps_winner():
    """
        The function prompts the user for the choices of 2 players in a game of rock, papers, scissors and returns the result of player 1

        [None] -> None
        
    """

    p1 = input("What choice did player 1 make? \nType one of the following options: 'rock', 'paper', 'scissors': ")
   
    p2 = input("What choice did player 2 make? \nType one of the following options: 'rock', 'paper', 'scissors': ")

    a = (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock')#p1 wins
    b = (p1 == 'rock' and p2 == 'paper') or (p1 == 'scissors' and p2 == 'rock') or (p1 == 'paper' and p2 == 'scissors')#p2 wins
    c = (p1 == p2)#p3 wins

    print((('Player 1 wins.' + ' That is' + ' ' + str(a) + '.' + '\nIt is a tie. That is not' + ' ' + ('True')) or print ((('Player 1 wins .' + ' That is ' + ' ' + str(b) + '.' + '\nIt is a tie. That is not ' + ' ' + ('True'))))or print (('Player 1 wins .' + ' That is' + str(c) + '.' + '\nIt is a tie. That is not' + ('False')))))

        
############################################################################### Question 8 ###########################################################################################

def fun(x):
    """
        Precondition: 'x' must be a positive number
        
        The function calculates takes a positive input, plugs it into the formula as X and solves for y.

        [number] -> float

    """

    y = (math.log10(x+3)/4)#rearranged the original formula to solve for y by taking log of both sides, bringing the 4y down and isolating for y.
    return y

############################################################################### Question 9 ###########################################################################################

def ascii_name_plaque (name):
    """
        The function takes an indidivual's name as an input and prints a string in the ascii name plaque format.

        [String] -> None

    """

    str = (name)
    b = len(str)


    print (((b)*('*')) + ('*'*10)) 

    print ((('*') + (8*' ') + ((b)*(' ')) + ('*')))
    
    print ((('*  ') + ('__') + (str) + ('__') + ('  *'))) 
    
    print (((((('*') + (8*' ') + (b)*(' '))) + ('*'))))
    
    print (((((b)*('*')) + ('*'*10))))
    
############################################################################### Question 10 ###########################################################################################


s=turtle.Screen()
t=turtle.Turtle()

def draw_car():
    """
        This function draws a car using Python Turtle Graphics.

        [None] -> None
        
    """
    
    screen = turtle.Screen()
    turtle.tracer(0, 0)


    t=turtle.Turtle()

       
#Left Wheel
    t.penup()
    t.goto(-250,-100)
    t.pendown()
    t.circle(10)#smallest circle, left wheel
    t.penup()
    t.goto(-250,-125)
    t.pendown()
    t.circle(37)#second circle, left wheel
    t.penup()
    t.goto(-250,-152)
    t.pendown()
    t.circle(70)#main wheel, left side
    t.penup()

#Line between the two wheels
    t.color("red", "black")
    t.begin_fill()
    t.goto(-186,-108)#starting point of the line between the two wheels
    t.pendown()
    t.goto(20,-105)#to account for the slight curve between the two wheels (from the sample pic in the assignment)
    t.goto(180,-108)#ending point of the line between the two wheels
    t.penup()
    t.goto(230,-85)
    t.pendown()
#Right Wheel
    t.color("yellow")
    t.circle(5.5)#smallest circle, right wheel
    t.penup()
    t.goto(240,-118)
    t.pendown()
    t.circle(38)#second circle, right wheel
    t.penup()   
    t.goto(242,-152)
    t.pendown()
    t.circle(70)#main wheel right side
    t.penup()
#Right Wheel Spokes
    t.color("grey")
    t.goto(232,-77)#start of wheel spoke, RS
    t.pendown()
    t.setheading(90)
    t.goto(250,-42)#end of wheel spoke
    t.penup()
    t.goto(226,-79)#start of wheel spoke
    t.pendown()
    t.goto(214,-53)#end of wheel spoke
    t.penup()
    t.goto(226,-82)#start of wheel spoke
    t.pendown()
    t.goto(210,-106)#end of wheel spoke
    t.penup()
    t.goto(232,-85)#start of wheel spoke
    t.pendown()
    t.goto(235,-117)#end of wheel spoke
    t.penup()
    t.goto(233,-80)#start of wheel spoke
    t.pendown()
    t.goto(278, -84)#end of wheel spoke
    t.penup()
#Left Wheel Spokes
    t.goto(-250,-80)#start of wheel spoke
    t.pendown()
    t.goto(-250,-50)#end of wheel spoke
    t.penup()
    t.goto(-259,-86)#start of wheel spoke
    t.pendown()
    t.goto(-283,-70)#end of wheel spoke
    t.penup()
    t.goto(-258,-98)#start of wheel spoke
    t.pendown()
    t.goto(-272,-120)#end of wheel spoke
    t.penup()
    t.goto(-240,-93)#start of wheel spoke
    t.pendown() 
    t.goto(-225,-115)#end of wheel spoke
    t.penup()
    t.goto(-240,-85)#start of wheel spoke
    t.pendown()
    t.goto(-215,-75)#end of wheel spoke
    t.penup()

#Bumper of the car
    t.goto(-315,-108)#start of horizontal line from the wheel
    t.pendown()
    t.goto(-350,-108)#end of horizontal line
    t.penup()
    t.goto(-351,-106)   
    t.pendown()
    t.goto(-359,-75)#start of the bumper
    t.goto(-345,-72)#to account for the curve in the sample picture
    t.goto(-320,-74)#end of the bumper at the wheel
    t.penup()
#main car frame inlcuding the front bumper
    t.goto(-345,-72)
    t.pendown()
    t.goto(-345,30)#max
    t.goto(-345,5)
    t.goto(-322,5)
    t.goto(-322,17)
    t.goto(-345,17) 
    t.penup()
    t.goto(-345,30)#start of horizontal line
    t.pendown()
    t.goto(-330,33)#curve
    t.goto(350,28)#end of horizontal line
    t.goto(352,20)#curve
    t.goto(354,-80)
    t.goto(330,-80)
    t.goto(380,-80)
    t.goto(376,-110)
    t.penup()
    t.goto(375,-110)
    t.pendown()
    t.goto(302,-110)
    t.penup()
    t.goto(345,20)
    t.pendown()
#front light
    t.goto(340,21)
    t.goto(340,8)
    t.goto(345,8)
    t.goto(345,21)
    t.penup()
#windows and roof
    t.goto(-250,33)
    t.pendown()
    t.goto(-150,140)
    t.penup()
    t.goto(-148,142)
    t.pendown()
    t.goto(-82,142)
    t.goto(-82,-100)#door seperation
    t.goto(-82,142)
    t.goto(130,143)
    t.goto(180,29)
    t.goto(183,-47)
    t.penup()

#door handle
    t.goto(-60,5)
    t.pendown()
    t.goto(-57,-5)
    t.goto(-37,-5)
    t.goto(-37,3)
    t.goto(-60,5)
    t.penup()
    t.goto(400,-152)#right side of the road (front of the car)
    t.pendown()
    t.goto(-430,-152)#left side of the road (back of the car)


############################################################################### Question 11 ###########################################################################################

def alogical(n):
    """
        Precondition 'n' must be greater or equal to 1
        
        Takes an input as n and returns the number of times that 'n' needs to be halved until is less than or equal to 1

        [Number] -> Int

    """

    m = math.log(n,2)
    
    return math.ceil(m)

############################################################################### Question 12 ###########################################################################################

def time_format(h,m):
    """
        Precondition: 'h' must be an integer between 0 and 23 while 'm' must be an integer between 0 and 59.

        The function uses the input from a user, in hours and minutes. The minutes are then rounded to the nearest minutes. The time is returned in a string with
        the following format (e.g. 2 o'clock.)

        [int,int] -> string
        
    """

    a = ((round(m/5))*5)

    if a == 0:
        time = str(h) + " o'clock"

    if a == 5:
        time = str(a)+' minutes past '+ str(h) + " o'clock"

    if a == 10:
        time = str(a)+' minutes past '+ str(h) + " o'clock"

    if a == 15:
        time = str(a)+' minutes past '+ str(h) + " o'clock"

    if a == 20:
        time = str(a)+' minutes past '+ str(h) + " o'clock"

    if a == 25:
        time = str(a)+' minutes past '+ str(h) + " o'clock"
   
    if a == 30:
        time = str(a) + ' Half past ' + str(h) + " o'clock"

    if a == 35:
        time = str(60-a)+' minutes to '+ str(h+1) + " o'clock"

    if a == 40:
        time = str(60-a)+' minutes to '+ str(h+1) + " o'clock"

    if a == 45:
        time = str(60-a)+' minutes to '+ str(h+1) + " o'clock"

    if a == 50:
        time = str(60-a)+' minutes to '+ str(h+1) + " o'clock"
    
    if a == 55:
        time = str(60-a)+' minutes to '+ str(h+1) + " o'clock"

    if a == 60:
        time = str(h+1) + " o'clock"
    
    return time


############################################################################### Question 13 ###########################################################################################


def cad_cashier(price,payment):
    """
        Precondition: Price and payment must be positive numbers. Payment given by the customer must be greater than the price of the goods. Lastly,the second decimal
        in payment must either be a 0 or 5.

        This function calculates the change that a customer will receive with respect to his payment and the price of the good. Price is the price of the good while payment
        is the amount handed to the cashier for which they must return change.

        [number,number] -> float

    """    

    a=round(price*2,1)/2
    b=round(payment-a,2)

    return b


############################################################################### Question 14 ###########################################################################################


def min_CAD_coins(price,payment):
    """
        Precondition:  Price and payment must be positive numbers. Payment given by the customer must be greater than the price of the goods. Lastly,the second decimal
        in payment must either be a 0 or 5.

        This function determines the minimum number of coins that the cashier must return in terms of toonies, loonies, quarters, dimes and nickels. 

        [number,number]  -> tuple

    """

    price = cad_cashier(price, payment)


    t = price//2 #calculates number of toonies
    vt = (t*2)
    
    l = (price-(t*2))//1 #calculates number of loonies
    vl = (l*1)
    
    q = (price - (vt + vl))//0.25
    vq = (q*0.25)

    d = (price - (vt + vl + vq))//0.1
    vd = (d*0.1)

    n = (price - (vt + vl + vq + vd))//0.05
    vn = (n*0.05)

    return int(t),int(l),int(q),int(d),int(n)
    



    

    
