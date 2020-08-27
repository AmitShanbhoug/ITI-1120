import math


############################### EXERCISE 1 ##########################################

def is_eligible(age, citizenship, prison):

     if age >=18 and prison == "no" and citizenship == "Canada" or "Canadian":

          return True
        
     else:
         
          return False

     
name=input("What is your name? ")
age= int(input("How old are you? "))
prison = input("Are you currently in prison convicted for a criminal offense? ")
citizenship = input("What citizenship do you hold? ")

prison = prison.lower()
prison = prison.strip()
citizenship = citizenship.lower()
citizenship = citizenship.strip()



if is_eligible(age, citizenship, prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 


############################### EXERCISE 2 ##########################################

def mess(phrase):
    
    phrase = phrase.replace(" ","-")
    for char in phrase:
        if char in "rstvwxyz":
            new = char.capitalize()
            phrase = phrase.replace(char,new)
            
    return phrase

############################### EXERCISE 4 ##########################################

char = input("Enter a character: ")
amount = int(input("Enter amount: "))


for i in range(amount+1):
    print(char * i)


############################### EXERCISE 5 ##########################################

def prime(number):
    if number >= 2:
        for i in range(2,number):
            if (number % i) == 0:
                return False
        return True


number = int(input("Enter a positive integer: "))

for i in range(number):
    if number % (i+1) == 0:
        print(i+1,end=",")

print("")

print("This number is prime:" ,prime(number))
