# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 4



import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE

    idst= []

    for i in friends[1:]:
        g = i.index(" ") # searches for the space seperating the numbers

    a = (len(friends))
    
# looking for people that are not friends with one another
        
    person_1 = int(i[:g])
    person_2 = int(i[g:])

# if 2 users are not friends with one another, add them to a list

    if person_1 not in idst:
            idst.append(person_1)
    if person_2 not in idst:
            idst.append(person_2)

    plist = []
    
    for i in idst:
        profile = (i,[])
        plist.append(profile)
    
    for j in friends[1:]:
        gap = j.index(" ")
        person_1 = int(j[:g])
        person_2 = int(j[g:])
    
        m = idst.index(person_1) 
        n = idst.index(person_2) 
        
        plist[m][1].append(person_2)
        plist[n][1].append(person_1)
    
    network = plist
    
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    friends_in_common=[] 
    
    g = []
    for k in network:
        id_pos.append(k[1])
        
    user_1 = network[id_pos.index(user1)][1]
    user_2 = network[id_pos.index(user2)][1]
    
    for i in user_1:
        for j in user_2:
            friends_in_common.append(b)
                
    friends_in_common.sort()

    return friends_in_common
    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    
    a = len(network)
    
    for i in range(len(network)):
        r = getCommonFriends(user, network[i][0], network)
        t = len(r)
        if (t > current_longest) and (network[i][0] != user) and (user not in network[i][1]):
            current_longest = t
            s = network[i][0]
    if user != s:
        return s


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    pass

    a = 0
    for i in network:
        if len(i[1])>=k:
            a = a + 1
    return a

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    pass
    
    maximum = 0
    
    for i in network:

        if len(i[1])>maximum:

            maximum = len(i[1])

    return maximum

  

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE

    check = maximum_num_friends(network)
    
    for i in network:

        if len(i[1]) == check:

            max_friends.append(i[1])

    return max_friends   

def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    
    a = 0
    total = len(network)
    
    for i in network:
        a = a + len(i[1])
    avg = num//total
    return avg

    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE

    people = len(network)
    a = True
    while a != False:
        for i in network:
            if len(i[1]) == people-1:
                a = False
        break
    return a

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE

    b = []
    for i in network:
        uid = i[0]
        b.append(uid)
        
    check = 0
    
    while check == 0:
        a = input("Enter an integer for a user ID")

        if a.isdigit():
            if int(a) in b:
                check = check+1
                return int(a)
            else:
                print("That User ID does not exist. Try again.")
        else:
            int(a)
            print ("That User ID does not exist. Try again.")
            
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
