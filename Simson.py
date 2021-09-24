# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:36:33 2019

@author: sikkum
"""

import numpy as np
#import scipy.integrate as sci
f = lambda x: np.sin(x)/np.exp(x)
x = np.linspace(0,np.pi,20)
y = f(x)
h=x[1]-x[0]

sum=0
for i in range(1,19):
    sum=sum+y[i]

I=(h/2)*(y[0]+y[19]+2*sum)
print("The approximation of the definite integral is","%.3f"% I)
