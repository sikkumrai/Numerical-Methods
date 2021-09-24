# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:33:27 2019

@author: Sikkum
"""
import math
fx = lambda x : math.exp(x) - 4*x
deriv = lambda x : math.exp(x) -4
x0 = -3.0
i = 1

while True:
    i = i+1
    x1 = x0 - (fx(x0) / deriv(x0))
    print ("{}\t{}".format(i,x0))
    if (abs(x1 - x0) < 0.00001 ):
        print("The root is {}".format(x1))
        break
    else:
        x0 = x1