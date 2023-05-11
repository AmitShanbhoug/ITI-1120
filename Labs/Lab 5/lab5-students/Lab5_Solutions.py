# Amit Shanbhoug
# 0008677407
# 11 Oct 18

import math


def ah(l,x,y):
    
     '''(list, int,int)->(int,number/+inf)
     Returns two numbers such that the first is the number of elements of the list
     between x and y. The second number is the minimum element of that are between x and y.

     Precondition: x <= y and the list contains numbers
     '''

     counter=0
     min_in_range = None
     for item in l:
          if item>=x and item <=y:
               counter=counter+1
               if(min_in_range == None or item <= min_in_range): 
                    min_in_range=item

     return(counter,min_in_range)

def arithmetic(l):
     '''(list)->bool
       Returns True if list l contains an arithmetic sequence, and returns false otherwise.
       
       Precondition: Elements of l are numbers'''

     if(len(l)<2):
         return True
    
     diff = l[1] - l[0]
     for i in range(1, len(l)-1):
        if l[i+1] - l[i] != diff:
            return False
     return True

# purpose of the last part is to check for the difference between consecutive numbers and that is equal to the difference
# the first two numbers

def is_perfect(n):
     ''' (number)->bool
     Returns True if the given positive integer n is perfect

     Precondition: n>=1
     '''
     current_sum = 0
     for divisor in range(1, n):
          if n % divisor == 0:
               current_sum = current_sum + divisor

     if n == current_sum:
          return True
     else:
          return False

print("Printing perfect numbers smaller than 10,000:")
for number in range(6,10001):
     if is_perfect(number):
          print(number)        
