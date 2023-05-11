############################################################### 1.3 ###############################################################
# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 3





def longest_run(x):

    ''' The function returns the longest run of identical numbers in the input list.

        (list)-> int
    '''

    previous = x[0]
    a = 0
    for i in range(0, len(x)):
        if x[i] == previous:
            a = a + 1
        else:
            previous = x[i]
        return a

a = input(' Please input a list of numbers seperated by space: ')
a = a.split()
x = [int(i) for i in a]
longest_run(x)
