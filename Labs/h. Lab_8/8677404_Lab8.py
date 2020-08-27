
import math
import random

# programming exercise 1
def make_matrix_random(a,b, x, y):
    
     matrix = []
     for i in range(a):
          row = []
          matrix.append(row)
          for i in range(b):
               row.append(random.randint(x, y))

     return matrix
          

# programming exercise  2
def sum_above_diagonal(m):
     
     theSum = 0
     row = 0
     column = 0
     
     for row in range(0, len(m)+1):
          for column in range(len(m[row])):
               if (row <= column):
                    theSum = theSum + m[row][column]

     return theSum
     
     

# programming exercise  3
def max_over_all_even_cols(m):
    
     maximum = m[0][0]
     for i in range(len(m)):
          for j in range(0, len(m[i]), 2):
               if m[i][j] > maximum:
                    maximum = m[i][j]
     return maximum
               
          

#programming exercise  4
def max_each_row(m):
     
     
     maxList = []
                   
     for x in range(len(m)):
          maxOfRow = m[x][0]    
          for y in range(len(m[x])):
               if (m[x][y] > maxOfRow):
                   maxOfRow = m[x][y]
                   
          maxList.append(maxOfRow)
          
     return maxList


# programming exercise  5
def index_of_max_sum_row(m):
    
     
     for i in range(len(m)):
          index = m[i][0]
