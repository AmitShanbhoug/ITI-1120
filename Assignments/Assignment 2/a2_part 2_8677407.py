# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 2

import math

def main():
    '''
        (int) -> (str)

        This program will read a student's grades (exams and homework) and computes
        the student's course grade.

    '''

    print()
    intro()
    grades()

def intro():
    
    print("This program reads exam/homework scores and reports your overall course grade.")
    
def midterm_1():

    print()
    print("Midterm 1:")
    w = int(input("Weight (0-100)? "))

    se = int(input("Score earned? "))
    if (se > 100):
        se = 100
   
    ss = int(input("Were scores shifted (1=yes, 2=no)? "))

    if (ss == 1):
        a = int(input("Shift amount? "))

        if se + a < 100:
            t_p = se + a

        else:
            t_p = 100

    else:
        t_p = se         
    
    w_s = round((t_p * (w/100)),1) 

    print ("Total Points = " + str(t_p) + " / 100")
    print ("Weighted Score = " + str(w_s) + " / " + str(w))
    print()
    return w_s


def midterm_2():

    print("Midterm 2:")
    cw = ("Midterm 2: ")
    w = int(input("Weight (0-100)? "))

    se = int(input("Score earned? "))
    if (se > 100):
        se = 100
   
    ss = int(input("Were scores shifted (1=yes, 2=no)? "))

    if (ss == 1):
        a = int(input("Shift amount? "))

        if se + a < 100:
            t_p = se + a

        else:
            t_p = 100

    else:
        t_p = se         
    
    w_s = round((t_p * (w/100)),1) 

    print ("Total Points = " + str(t_p) + " / 100")
    print ("Weighted Score = " + str(w_s) + " / " + str(w))
    print()
    return w_s

def final():

    print("Final:")
    cw = ("Final: ")
    w = int(input("Weight (0-100)? "))

    se = int(input("Score earned? "))
    if (se > 100):
        se = 100
   
    
    ss = int(input("Were scores shifted (1=yes, 2=no)? "))

    if (ss == 1):
        a = int(input("Shift amount? "))

        if se + a < 100:
            t_p = se + a

        else:
            t_p = 100

    else:
        t_p = se         
    
    w_s = round((t_p * (w/100)),1) 

    print ("Total Points = " + str(t_p) + " / 100")
    print ("Weighted Score = " + str(w_s) + " / " + str(w))
    print()
    return w_s

def homework():

    print("Homework: ")
    cw = ("Homework: ")
    w = int(input("Weight (0-100)? "))
    assignments = int(input("Number of assignments? "))

    mp = 0.0
    sp = 0.0
    
    for num in range(1, assignments + 1):
        
        p = float(input("Assignment " + str(num) + " score? "))
        
        mpts = float(input("Assignment " + str(num) + " max? "))
        
        sp += p
        
        mp += mpts

    sec = int(input("How many sections did you attend? "))

    if sec <= 11:

        secpts = sec*3

    elif sec > 11:

        secpts = 34

    secpts = sec*3

    if sp > mp:
        sp = mp

    t_p = ((secpts + sp) / (mp + 34))
    w_s = t_p * w

    g = round(sp + secpts)
    h = round(mp + 34)
    k = round(w_s,1)

    print ("Section points = " + str(sec*3) + " / 34")
    print ("Total points = " + str(g) + " / " + str(h))
    print("Weighted score = " + str(k) + " / " + str(w))
    print()
    return w_s

def grades():

    OP = (midterm_1() + midterm_2() + final() + homework())

    print ("Overall Percentage = " + str(round((OP),1)))
    
    if (OP >= 90.0):
        print("Your grade will be at least: A")
        print("Excellent, keep it up!")
    
    if (89.99 >= OP >= 80):
        print("Your grade will be at least: B")
        print("Great Job!")

    elif (79.99 >= OP >= 70):
        print("Your grade will be at least: C")
        print("Satisfactory")

    elif (69.99 >= OP >= 60):
        print("Your grade will be at least: D")
        print("Put in more effort next time")

    elif (OP < 60):
        print("Your grade will be at least: F")
        print("Please see your TA")
               
    
main()

   
    
