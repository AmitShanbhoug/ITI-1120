import math

def f1(x):
    res=x**2+10
    return res

def f2(x):
    res=x**2+10
    print (res)
    return None  

def area_of_triangle(base, height):
    area=base*height/2
    return area

def area_of_circle(radius):
    pi=3.14
    area=radius**2*pi
    return area

def s_to_m(s):
    m=s//60
    #s=s-m*60
    s=s%60
    return (m,s)

def s_to_hms(s):
    h=s//3600
    #s=s-h*3600
    s=s&3600
    m=s//60
    s=s%60
    return (h,m,s)

f1(1)


