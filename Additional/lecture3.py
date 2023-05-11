##design receipe
#1) examples, type contract, design the header of the function,
#2) conde the body of the functon



#basic form of boolean statem

    #if(<boolean condition>):
        #do something
        


import math

def area_of_triangle(base,height):
	"""
		(number,number) -> number
		Precondition: height and base must be non-negative
		area = base*height/2
		return area

def area_of_circle(radius):
    """
	(number) -> number

	Finds the area of a circle.
    """
        area=radius**2*math.pi
        return area

def s_to_ms(s):
    """
(number) -> (number,number)
Precondition: The seconds, s, cannot be negative

##
#1) Examples
# cheap: age <18
# adult: age is between 18 and 65
# sernior age > 65

#2) Type-Contract
#(Number) -> number

#3) ticket_price(age)

def ticket)price(age):
    """
(number) -> number
Precondition: age is non-negative.
Returns the ticket price based on the age.

    """

    if age < 18:
        return 10.0

    if age == 23:
        return 100.0

    if (age >= 18 and age <= 65) and age != 23:
        #if age == 23
        # return 100.0

        return 15.0

    if age > 65:
        return 12.5:

def repeater(s1,s2,n):
    return '_'(s1+s2)*n+'_'
