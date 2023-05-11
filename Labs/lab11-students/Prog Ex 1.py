def m(i):
     ''' (int)->number
         The function returns the sum 1/3+2/5+3/7+...+i/(2i+1)
         Precondition: i>=1
     '''
     if i == 1:
          return 1 / 3
     else:
          return m(i - 1) + ((i * 1) / (2 * i + 1))


for i in range(1, 11):
     print('m('+ str(i)+')=', m (i) )

def count_digits(n):
     ''' (int)->int
         The function returns the number of digits in n
         Precondition: n a positive integer
     '''
     count=0
     rest_of_digits = n // 10
     
     if rest_of_digits == 0:
          count= 1
     else:
          count = 1 + count_digits(rest_of_digits)
        
     return count

def is_palindrome(s):
     ''' (str)->bool
         Returns True if string s forms a palindrom and False otherwise
     '''
     if len(s) <= 1: # base case
          return True
     elif (s[0].lower()  != s[len(s)-1].lower() ):
          return False
     else:
          return is_palindrome(s[1:len(s)-1])  


def is_palindrome_v2(s):
     ''' (str)->bool
         Returns True if string s forms a palindrom and False otherwise
         (while ignoring all special characters)
     '''
     if len(s) <= 1: 
          return True
     else:
          first=s[0].lower()
          last=s[len(s)-1].lower()

          if first.isalpha() and last.isalpha():
               if first==last:
                    return is_palindrome_v2(s[1:len(s)-1])
               else:
                    return False
          elif not last.isalpha(): 
               return is_palindrome_v2(s[0:len(s)-1])
          else : 
               return is_palindrome_v2(s[1:len(s)]) 

def gcd(a, b):
    ''' (int,int)->int
        Returns the greatest common divisor of a and b
        Precondition: a and b are both positive integers
    '''  
    if a % b == 0:
         return b
    else:
      return gcd(b, a % b)
