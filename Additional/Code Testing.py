import math

import turtle


#import decimal

#def cad_cashier(price,payment):

 #   a = round(price,2)
  #  c = payment - price
   # d = format(c,'.2f')
    #return Decimal('c')

def cad_cashier(price,payment):
    return round((payment-round((round(price/0.05)*0.05),2)),2)


###############################################################################################################################################



def draw_car():

    turtle.speed(0)
screen = turtle.Screen()
turtle.tracer(0, 0)


t=turtle.Turtle()

t.color("black","yellow")
t.begin_fill()
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
t.goto(-186,-108)#starting point of the line between the two wheels
t.pendown()
t.goto(20,-105)#to account for the slight curve between the two wheels (from the sample pic in the assignment)
t.goto(180,-108)#ending point of the line between the two wheels
t.penup()
t.goto(230,-85)
t.pendown()
#Right Wheel
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
