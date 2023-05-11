import math

def is_divisible(n,m):

    return n%m==0


#Programming Exercise 3b

def is_divisible23n8(n):
  
    if is_divisible(n,2) or is_divisible(n,3) and not is_divisible(n,8):
        return True

    else:
        return True

n = int(input("Enter 1st integer:"))
z = is_divisible23n8(n)

if z==True:
    print (str(n) + ' is divisible by 2 or 3 but not 8')

else:
    print ('It is not true that ' + (str(n) + ' is divisible by 2 or 3 but not 8'))
