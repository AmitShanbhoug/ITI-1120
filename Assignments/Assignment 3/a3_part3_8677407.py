# Name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 


import math
import random

def hangman():

    words = ["write", "program", "that", "receive", "positive","change", "study", "excellent", "nice"]

    a = random.choice(words)

    b = a.maketrans("abcdefghijklmnopqrstuvwxyz","**************************")
    
    Bingo = a.translate(b)
    
    incorrect_guess = 0
    
    while(Bingo != a):
        
        user_guess = input("(Guess) Enter a letter in word "+ Bingo + " > ")

        if user_guess in Bingo:

            print(user_guess,"is already in the word")

        if user_guess in a:

            for i in range(len(a)):
                
                if a[i] == user_guess:
                    
                    Bingo = Bingo[:i] + user_guess + Bingo[i+1:]
           
        else:
            
            print(user_guess,"is not in the word")

            incorrect_guess += 1

            
    print()
    print("The word is", a,'.', "You missed", incorrect_guess, "times.")
    print()


    continue_playing = input("Do you want to guess another word? Enter y or n ")

    if continue_playing == "y":

        hangman()
    
    
hangman()
