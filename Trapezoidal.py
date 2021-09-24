# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:58:35 2019

@author: sikkum
"""

import numpy as np
f = lambda x: np.sqrt(1/(2*np.pi))*np.exp(-(x**2)/2)
x = np.linspace(-4,4,50)
y = f(x)
h=x[1]-x[0]
sum=0
for i in range(1,49,2):
    sum=sum+y[i]
sum_o=0
for i in range(2,48,2):
    sum_o=sum_o+y[i]

I=(h/3)*(y[0]+y[49]+4*sum+2*sum_o)
print("The approximation of the definite integral is","%.3f"% I)
