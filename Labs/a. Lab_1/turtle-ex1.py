import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

# Place your code after this line

numberOfSides=100

t.circle(13)#first circle
t.goto(0,300)#max
t.goto(0,-30)
t.circle(50)#second circle
t.goto(0,-70)
t.circle(90)#third circle
t.goto(0,-120)
t.circle(140) #fourth circle
t.goto(0,-250)
t.penup()
t.goto(300,10)
t.pendown()
t.goto(-300,10)
t.penup()
t.goto(-250,210)#left to right 
t.setheading(45)
t.pendown()
t.goto(250,-190)
t.setheading(45)
t.penup()
t.goto(230,210)
t.pendown()
t.goto(-250,-210)#right to left
