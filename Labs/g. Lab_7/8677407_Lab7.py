import math




################################## Exercise 5.16 ####################################

def indexes(s,c):

    a = []
    #for index, i in enumerate(s):
    for i in range(0,len(s)-1):
        if s[i] == c:
            a.append(i)
    return a

################################## Exercise 5.17 ####################################

def doubles(l):
      
    if len(l) > 1:
        
        for i in range(1, len(l)):
            if(l[i] == 2*l[i-1]):
                print(l[i])
     
    
################################## Exercise 5.18 ####################################

def four_letter(l):

    a = []
    for i in l:
        if len(i) == 4:
            a.append(i)
            
    return a

################################## Exercise 5.19 ####################################

def inBoth(l1,l2):

    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                return True
    return False

################################## Exercise 5.20 ####################################

def intersect(l1,l2):

    a = []
    for i1 in l1:
        for i2 in l2:
            if i1 == i2:
                a.append(i1)
    return a
    
################################## Exercise 5.21 ####################################

def pair(l1,l2,n):

    for i1 in l1:
        for i2 in l2:
            if (i1 + i2 == n):
                print (i1, i2)

################################## Exercise 5.22 ####################################

def pairSum(lst,n):

    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == n:
                print(i,j)

################################## Exercise 5.29 ####################################

def lastfirst(names):

    l,f = [],[]

    for n in names:
        t_l, t_f = n.split(" , ")
        l.append(t_l)
        f.append(t_f)

    final = [f,l]
    return final

################################## Exercise 5.31 ####################################

def susbsetSum(l,n):

    for i in range(0, len(l)):
        for j in range(i, len(l)):
            for k in range(j, len(l)):
                if l[i] + l[j] + l[k] == n:
                    return True
    return False

################################## Exercise 5.33 ####################################

def mystery(n):

    a = 0

    while n > 1:
        a += 1
        n = (n//2)

    return a

################################## Exercise 5.46 ####################################

def inversions(s):

    inversions = 0

    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if s[i] > s[j]:
                inversions += 1
                
    return inversions

################################## Exercise 5.48 ####################################


def sublist(l1,l2):

    
    flag = True
    i = 0
    
    for n in l1:
        while i < len(l2):
            if l2[i] == n:
                i += 1
                flag = True
                break
            else:
                i += 1
                flag = False

        if flag == False:
            return False

    return True

################################## Exercise 5.37 ####################################

def mssl(l):

    m = 0

    for i in range(0, len(l)):
        for j in range(i + 1, (len(l) + 1)):
            if sum(l[i:j]) > m:
                m = sum(l[i:j])

    if m < 0:
        m = 0
    return m
    
