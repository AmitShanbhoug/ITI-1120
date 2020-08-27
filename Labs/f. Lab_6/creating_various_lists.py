n=int(input("Enter a positive even integer for the size of the list?" ))

#######################################
list_a = []

for i in range(n):
    
    list_a += [0]
    
print("list_a =", list_a)

#######################################

print("list_a = ",[0] * n)

#######################################

list_b = []

for i in range(n):
    
    x = random.randint(1,100)

    list_b += [x]
    
print("list_b = ", list_b)

b = [None] * n

for i in range(n):
    
    b[i]=random.randint(1,100)
    
print("list_b = ", b)

x = 0
list_c = list_b

while x < (len(list_c) // 2):
    
    list_c[x] = 0
    x += 1
    
print("list_c = ", list_c)
print("list_b = ", list_b)

#######################################

list_d = []
r = 0

while r < len(list_b):
    
    list_d += [list_b[r]]
    r += 1
print("list_d = ", list_d)

#######################################
list_d = list_b * 1

print("list_d = ", list_d)

m = 1
list_e = []

while m < len(list_d):
    
    list_e += [list_b[m]]
    m += 2
print("list_e = ", list_e)
