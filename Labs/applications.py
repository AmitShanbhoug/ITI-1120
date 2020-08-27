

import math

# QUESTION 1

def element_uniqueness(L):
    
     
     check = True
     
     for item in lst:
          if lst.count(item) > 1:
               check = False
     return check

 
# QUESTION 2

def one_unique_at_least(L):
     
     unique_list = []
     numOfUniques = 0
     for x in L:
          if x not in unique_list:
               numOfUniques += 1
               unique_list.append(x)

          if numOfUniques == 1:
               return True
          elif numOfUniques != 1:
               return False
     

# QUESTION 3
     
#def all_unique(L):
     ''' (list,int)->list
     Return a list of elements of L that appear exactlly once in L. 
     Precondition: L is not empty
    
     >>> all_unique([2, 2,2, 2, 8])
     [8]
     >>> all_unique([1,-20,-1])
     [-20,-1,,1]
     >>> all_unique([3,2,2,3,3])
     []
     >>> all_unique([10])
     [10]
     >>> all_unique([10,10])
     []
     >>> all_unique([10,-1])
     [-1,10]
     '''
 

# QUESTION 1 again

#def element_uniqueness_v2(L):
     # make now a 2nd solution to element_uniqueness
     # by making a call to all_unique
 

# QUESTION 2 again

#def one_unique_at_least_v2(L):
     # make now a 2nd solution to one_unique_at_least_v2
     # by making a call to all_unique

# QUESTION 4

def count_unique(L):
     
     
     unique_list = []
     numOfUniques = 0
     for x in L:
          if x not in unique_list:
               numOfUniques += 1
     return numOfUniques
          
# QUESTION 5                               

#def duplicates(L):
     ''' (list)->int
     Returns True if the given list L has duplicates, in other,
     if it has at least one element that appears two or more times.
     Precondition: L is not empty

     >>> duplicates([2, 2,2, 2, 8])
     True
     >>> duplicates([1,-20,-1])
     False
     >>> duplicates([3,2,2,3,3])
     True
     >>> duplicates([10])
     False
     >>> duplicates([10,10])
     True
     >>> duplicates([10,-1])
     False
     '''

# QUESTION 6

#def majority(L):
     '''(list)->
     An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
     This function returns the majority element of L if such an element exsits, otherwise it returns None
     >>> majority([2,1,2])
     2
     >>> majority([10,5,1,5,5])
     5
     >>> majority([5,5,1,1])
     
     >>> majority([3])
     3
     >>> majority([8,8,2,8])
     8
     '''
 
