# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 3



import random

# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
      
    deck = []
    suit = 100
    rank = 1
    
    while len(deck) < (4*num):

        while rank <= num:

            deck.append(suit+rank)

            rank += 1

        rank = 1
        suit += 100

    return deck


def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    deck = random.shuffle(deck)
    return deck


def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''

     hand = []
     
     while len(hand) <= 7:

         hand.append(deck[0])

         del deck[0]

     return hand


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    count = 0
    
    if len(deck) < num:

        num = len(deck)
        
    while count<num:
        
        player.append(deck[0])
        del deck[0]

        count+= 1
    return deck


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    
    suit = sorted(hand[:])
    
    for i in suit:
        print(i, end=' ')
     
    rank = []
    Rankcard = 1
    
    while len(rank)<len(suit):

        count = 0
        
        while count < len(suit):
            
            if suit[count] % 100 == Rankcard:
                rank.append(suit[count])
                
            count += 1
            
        Rankcard += 1
        
    for i in range(len(rank)):
        
        print(rank[i], end =' ')

    return
        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''

    
    boolean = True
    
    count = 0
    
    while count < len(cards) and boolean == True:
        if cards[count] not in player:
            print(str(cards[count]) + ' is not in your hand. Invalid input')
            boolean = False
        count += 1 
    return boolean



def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''

    
    count = 0
    
    boolean = True
    
    if len(cards)<2:
        
        boolean = False 
        print('Invalid input. Discardable set needs to have at least 2 cards')

    else:
        
        while count<(len(cards)-1) and boolean == True:
            
            if (((cards[count+1]-cards[count+1]))//(100)) != (((cards[count]-cards[count]))//(100)):

                boolean = False
                
            count += 1
            
    return boolean
    


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    
    boolean = True

    count = 0

    if len(cards)<3 :

        boolean = False

        print('Invalid sequence. Discardable sequence needs to have at least 3 cards.')

    else:  

        while count < (len(cards)-1) and boolean == True:

            if  ((cards[count + 1])//100) != (cards[count]//100) :
                boolean = False

                print('Invalid sequence. Cards are not of same suit')

            elif (((cards[count + 1])-(cards[count + 1]%100))) != ((cards[count]-cards[count]%100 + 1)):

                boolean = False

                print('Invalid sequence. While the cards are of the same suit the ranks are not consecutive intergers.')

            count += 1

    return boolean  

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    flag = True
    
    while flag:
        card = int(input('Discard any card of your choosing.\nWhich card would you like to discard? ').strip())
        if card not in player:
            print(card)
            print('No such card in your hand. Try again')
        else: 
            player.remove(card)
            print('Here is you new hand printed in two ways:')
            print_deck_twice(player)
            flag = False
    return

def rolled_nonone_round(player):
    
     '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
     flag = True
     
     while flag:
         
        question = input('Yes or no, do you have a sequence of three or more cards of the same suit or two or more of a kind? ').strip()
   
        if question == 'yes':
            
            cards = input('Which 3+ sequece or 2+ of a kind would you like to discard? Type in cards separated by space: ').strip().split()

            cards = cards.strip()
            cards = cards.split()
            
            for n in range(len(cards)):
                
                cards[n] = int(cards[n])
                
                if is_valid(cards,player) == True:
                    
                    if is_discardable_kind(cards) or is_discardable_seq(cards) == True:
                        
                        for i in cards:
                            
                            player.remove(i)
                            
                        print('Here is your new hand printed in two ways: ')
                        
                        print_deck_twice(player)
                    elif question == 'no':
                        flag = False 
     return 

# main

print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

num = 13
if size_change == 'yes':
    
    num = int(input('Enter a number between 3 and 99 for the number of ranks : ')).strip()
deck = make_deck(num)
              
print('You are playing with a deck of ' + str(len(deck)) + ' cards')
              
shuffle_deck(deck)
player = deal_cards_start(deck)
              
print('Here is your starting hand in two ways: ')
              
print_deck_twice(player)

round = 0
while len(player)>0:
              
    round += 1
    print('Welcome to round ' + str(round))
    print('Please roll the dice')
    if len(deck) > 0:
              
        dice =  random.randint(1,6)
        print('You rolled the dice and it shows: ' + str(dice))
              
    else:
              
        dice = 1 
        print('The deck is out of cards. You will play as though you have rolled a one.') 
    
    if dice == 1:
              
        rolled_one_round(player)
              
   
