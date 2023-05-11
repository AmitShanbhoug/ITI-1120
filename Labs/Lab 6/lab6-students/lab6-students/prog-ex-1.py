def sum_odd_while_v2(n):
    '''(int)->int Returns the sum of all odd integers between 5 and n'''
    odd_sum = 0
    i = 5
    while (5 <= i <= n):
        if i % 2 == 1:
            odd_sum = odd_sum + i
        i = i + 1
    return odd_sum
##############################################################################        
def sum_int():
 
    a = int(input("Please enter an integer: "))
    b = int(input("Please enter another integer: "))

    print (a + b)

    c = str(input("Would you like to do that again? "))

    while c == 'yes':
        answer = (a + b)
        if c == 'yes':
            a = int(input("Please enter an integer: "))
            b = int(input("Please enter another integer: "))

        print (a + b)

        c = str(input("Would you like to do that again? "))
##############################################################################
def first_neg(a):

     if len(a)==0: # if the list is empty, it returns none
          return None
     i=0
     while(i<len(a) and a[i]>=0):
          i=i+1

     if(i==len(a)):
          return None
     else:
          return i
 
