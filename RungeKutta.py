# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:56:22 2019

@author: sikkum
"""
#Runge Kutta 2nd order method
def func( x, y ): 
    return (x*x + x) 

def rk( x0, y, h, x ): 
    while x0 < x: 
        k1 = h*func(x0,y)
        k2=h*func(x0+h,y+k1)
        y=y+(k1+k2)/2
        print("Approximate solution at x = ","%.1f"% x0+" is ", "%.6f"% y)
        x0=x0+h
x0 = 0
y0 = 1
x = 2
h = (x-x0)/10  
rk(x0, y0, h, x)