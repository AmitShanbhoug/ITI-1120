




################################## Exercise 1 ####################################

def sum_odd_while_v2(n):

    i = 5
    s = 0
    
    while i < n:
        
        total += i
        i += 2
        
    return S     




################################## Exercise 2 ####################################

def add():

    main()

def main():
    
    a = int(input("Please enter integer 1: " ))
    b = int(input("Please enter integer 2: " ))
    c = input("Do you wish to perform this operation again? " ).strip().lower()
    print (a + b)
    print()

    while c == 'yes':
        main()
    
################################## Exercise 3 ####################################

def first_neg(l):

    i = 0

    while i < len(l):

        if l[i] < 0:
            return i
        
        else:
            i += 1

################################## Exercise 4 ####################################

def sum_5_consecutive(l):

    i = 0

    while i <= (len(l) - 5):
        
        if (l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4]) == 0:
            
            return True

        else:
            
            i += 1
            
    return False

################################## Exercise 6 ####################################

def fib(n):
    
    a = [1, 1]

    for i in range(2, n):
        
        a += ([a[i-1] + a[i-2]])
        i += 1
        
    print(a)
    
################################## Exercise 7 ####################################

def inner_product(x,y):
    
    s = 0
    
    for i in range(len(x)):
        s += (x[i] * y[i])
        
    return s
