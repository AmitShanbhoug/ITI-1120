# Name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 



import math
import random

def CouponCollector():
    
    
    allranks = ["Ace","1","2","3","4","6","7","8","9","10","Jack","Queen","King"]
    allsuits = ["Diamonds","Spades","Clubs","Hearts"]

    rank = []
    suit = []
    
    a = False

    while not(a):
        
        rank.append(random.choice(allranks))
        
        suit.append(random.choice(allsuits))
        
        if (suit.count("Diamonds") >= 1) and (suit.count("Spades") >= 1) and (suit.count("Clubs") >= 1) and (suit.count("Hearts") >= 1):

            a = True
            
        else:
            
            rank.append(random.choice(allranks))
            
            suit.append(random.choice(allsuits))


    Diamonds = suit.index("Diamonds")

    Spades = suit.index("Spades")

    Clubs = suit.index("Clubs")
    
    Hearts = suit.index("Hearts")

    
    print(rank[Diamonds], "of" ,suit[Diamonds])

    print(rank[Spades], "of" ,suit[Spades])

    print(rank[Clubs], "of" ,suit[Clubs])
    
    print(rank[Hearts], "of" ,suit[Hearts])
    
    print("Number of picks:",len(rank))

    
CouponCollector()

