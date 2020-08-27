import math


############################### EXERCISE 1 ##########################################

def ah(l,x,y):

     counter = 0

     m = l[0]

     a = ""

     for i in l:

          if i >= x and i <= y:
               counter += 1
               a = a + str(i)

     for i in l:
          if (i >= x and i <= y):
               if i < m:
                    m = i     
     
     return counter,m
          
############################### EXERCISE 2 ##########################################

def is_perfect(n):

     s = 0

     for i in range(1,n):
          
          if n % i == 0:
               
              s += i

     return s == n

############################### EXERCISE 3a ##########################################

def arithmetic(l):
     
    d = l[1] - l[0]
    flag=0
    for i in range(len(l) - 1):
         
        if ((l[i + 1] - l[i]) != d):
             
             flag=-1

    if flag==0: return True
    else: return False


############################### EXERCISE 3b ##########################################

def is_sorted(l):

     if l == sorted(l):
          return True
     return False
