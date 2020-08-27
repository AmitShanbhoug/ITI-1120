
import math

#Programming Exercise 1

def linear_search_v1(lst, value):

     i = len(lst)-1
    
     while i != 0 and lst[i] != value:

        i = i-1
    
     if i == 0:
          return -1
     else:
          return i


def linear_search_v2(lst, value):
     
     for i in range(len(lst)-1, 0, -1):
          
         if lst[i] == value:
              
             return i
          
     return -1


def linear_search_v3(lst, value):
          
     lst.append(value)

     i = len(lst)-1

     while lst[i] != value:
          
          i = i-1
     
     lst.pop()
     
     if i == 0:
          return -1
     else:
          return i


#Programming Exercise 2

def min_or_max_index(lst, b):
     
    if b == True:
         
        minValue = None
        
        for value in lst:
             
            if not minValue:
                 
                minValue = value
                
            elif value < minValue:
                 
                minValue = value
                
        return lst[minValue]
    
    elif b == False:
         
        maxValue = None
        
        for x in lst:
             
            if x > maxValue:
                 
                maxValue = x
                
        return lst[maxValue]




#Programming Exercise 3

def first_one(L): 
    numOfOnes = 0
    if len(L) <= 3:
        return 0
    elif len(L) > 3:
        index = binary_search(L, 1)
    return index



    =


def binary_search(L, v):
     
     

     b = 0
     e = len(L) - 1

     while b != e + 1:
          mid = (b + e) // 2
          if L[mid] < v:
               b=mid+1
          else:
               e=mid-1
          
     if 0 <= b < len(L) and L[b] == v:
          return b
     else:
          return -1




    
    

