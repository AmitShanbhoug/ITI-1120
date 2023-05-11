############################################################### 1.2 ###############################################################
# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 3





def two_length_run(list):
    ''''
        The function returns if the input has at least one run of length two

        (list) -> boolean
        
    '''

    if len(list) <= 1:
        
        return False
    return True

def main():

    list = [int(a) for a in input().split()]
    
    print(two_length_run(list))

q = input("Please input a list of numbers seperated by space: ")

main()
