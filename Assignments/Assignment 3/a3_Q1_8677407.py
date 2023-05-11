############################################################### 1.1 ##############################################################
# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 3

def count_pos(n):

    '''
    The function prints how many numbers in a list are positive.

    (list) -> Interger
    
    '''

    q = 0

    for i in range(0,len(n)):

        if (float(n[i]) > 0):
            q = q + 1

        else:
            None

    print ('There are', q ,'positive numbers in your list.')
          
q = input("Please input a list of numbers separated by space: ").split()
n = [float(i) for i in q]
count_pos(q)


