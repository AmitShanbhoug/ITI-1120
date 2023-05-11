# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 2

def split_tester(N, d):
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    pass

# you can add more function definitions here if you like       


            
# main
# Your code for the welcome message goes here, instead of name="Vida"

def user_message():

    str = (name)
    b = len(str)
    
    print (((b)*('*')) + ('*'*10)) 

    print ((('*') + (8*' ') + ((b)*(' ')) + ('*')))
    
    print ((('*  ') + ('__') + ("Welcome to my increasing splits-tester") + ('__') + ('  *'))) 
    
    print (((((('*') + (8*' ') + (b)*(' '))) + ('*'))))
    
    print (((((b)*('*')) + ('*'*10))))
    
    qq = (input("What is your name: "))

    return qq

flag=True
while flag:
    question=input('Amit'+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
   
