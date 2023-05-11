#Family name: Amit Shanbhoug 
# Student number:  0008677407   
# Course: IT1 1120 
# Lab Number 7

########################
# Question 5.16
########################

def indexes(word, character):
    occurrence = []
    i = -1
    for item in word:
        i += 1
        if item == character:
            occurrence.append(i)
    return occurrence

########################
# Question 5.17
########################

def doubles(integers):
    for i in range(1, len(integers)):
        if integers[i] == (integers[i-1] * 2):
            print(integers[i])


########################
# Question 5.18
########################

def four_letter(words):
    result = []
    for i in range(len(words)):
        if len(words[i]) == 4:
            result.append(words[i])
    return result

########################
# Question 5.19
########################

def inBoth(f, s):
    for i in range(len(f)):
        for j in range(len(s)):
            if f[i] == s[j]:
                return True
    return False

########################
# Question 5.20
########################

def intersect(first, second):
    result = []
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                result.append(first[i])
    return result

########################
# Question 5.21
########################

def pair(first, second, n):
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] + second[j] == n:
                print(first[i], second[j])


########################
# Question 5.22
########################

def pairSum(first, n):
    for i in range(len(first)):
        for j in range(i+1,len(first)):
            if first[i] + first[j] == n:
                print(i, j)


########################
# Question 5.29
########################

def lastfirst(names):
    fname = []
    lname = []
    for i in range(len(names)):
        ind = 2 + names[i].find(",")
        first = names[i][ind:]
        fname.append(first)
    for i in range(len(names)):
        ind = names[i].find(",")
        second = names[i][:ind]
        lname.append(second)
    return [fname] + [lname]


########################
# Question 5.31
########################

def subsetSum(first, n):
    for i in range(len(first)):
        for j in range(i+1, len(first)):
            for k in range(i+2, len(first)):
                if (first[i] + first[j] + first[k]) == n:
                    return True

    return False


########################
# Question 5.33
########################

def mystery(n):
    i = 0
    while n != 1:
        i += 1
        n = n // 2
    return i


########################
# Question 5.46
########################

def inversions(string):
    counter = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] > string[j]:
                counter += 1
    return counter


########################
# Question 5.48
########################

def sublist(first, second):
    temp = -1
    for item in first:
        for i in range(len(second)):
            if item == second[i]:
                place = second.index(item)
                if place > temp:
                    temp = place
                else:
                    return False
    return True


########################
# Question 5.37
########################

def mssl(l):
    m = n = 0
    for i in l:
        n = max(n + i, 0)
        m = max(m, n)
    return m
    
