# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:15:24 2019

@author: sikkum
"""

#Eulers method
def func( x , y ): 
    return (x*x + y) 
def euler( x0, y, h, x ): 
    while x0 < x: 
        y=y+h*func(x0,y)
        print("Approximate solution at x = ","%.1f"% x0+" is ", "%.6f"% y)
        x0=x0+h
x0 = 0
y0 = 1
h = (y0-x0)/20
x = 2
  
euler(x0, y0, h, x)

