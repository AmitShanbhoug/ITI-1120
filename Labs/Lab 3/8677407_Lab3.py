import math

#Programming Exercise 1

def pay(wage_hourly,hours_total):
    
    if 40 < hours_total <=60:
      return (((hours_total-40)*1.5)*wage_hourly) + (40*wage_hourly)

    elif hours_total > 60:
      return (40*wage_hourly) + ((20*(1.5*wage_hourly)) + ((hours_total-60)*2)*wage_hourly)

    else:
      return wage_hourly*hours_total

#Programming Exercise 2

def rps(p1,p2):

    if p1 == 'r' and p2 == 's' or p1 == 'p' and p2 == 'r' or p1 == 's' and p2 == 'p' or  p1 == 's' and p2 == 'p':
        return -1

    elif p1 == 's' and p2 == 'r' or p1 == 'r' and p2 == 'p' or p1 == 'p' and p2 == 's':
        return 1

    else:
        return 0

#Programming Exercise 3a
    
def is_divisible(n,m):

    return n%m==0

n = int(input("Enter 1st integer:"))
m = int(input("Enter 2nd integer:"))
o = is_divisible(n,m)

if o==True:
    print (str(n) + ' is divisible by ' + str(m))

else:
    print (str(n) + ' is not divisible by ' + str(m))

    
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
