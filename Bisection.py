# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:51:27 2019

@author: Dell
"""

import math
fx = lambda x : x**2 - math.sin(x)


a = 0.5
b = 1
n,i = 1,1
print ("Iteration  a and b")
while (n != 'True'):
    x1=fx(a)
    x2=fx(b)
    print ("{} \t\t {}\t{}".format(i,a,b))
    i = i + 1
    if (x1*x2 < 0):
        mid = (a + b) / 2
        x3 = fx(mid)
        if (x3 == 0):
            print("{} is the root.".format(mid))
            break
        elif (x1 * x3 < 0):
            b = mid
        elif (x2 * x3 < 0):
            a = mid
    
    elif(x1*x2>0):
        print(" Value of a and b  has not been choosed properly")
    else:
        print("here  a or b are root")
        
    if (b-a<0.001):
        print("{} is the root.".format(mid))
        break