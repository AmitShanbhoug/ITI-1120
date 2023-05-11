def minimum_for_v1(a):
    ''' (list) -> num '''
    minimum = a[0]
    for element in a:
        if element < minimum:
            minimum = element
        return minimum
