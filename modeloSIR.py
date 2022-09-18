#!/usr/bin/env python
# coding: utf-8



import matplotlib.pyplot as plt
import numpy as np
import sdeint

m=0.016
b=0.089
d=0.1
g=0.02
e=0.03
a=1
sig1=0.07
sig2=0.08
sig3=0.05

r=(b*m)/((m+sig1**2/2)*(m+g+e+sig2**2/2))

print(r)

tspan = np.linspace(0,200,5001)
y0 = np.array([25, 12, 8])


def f(y, t):
    Si = y[0]
    Ii = y[1]
    Ri = y[2]
    
    f0 = a - m*y[0] - (b*(y[0]*y[1]))/sum(y) + d*y[2]
    
    f1 = (b*y[0]*y[1])/sum(y) - (m+g+e)*y[1]
    
    f2 = g*y[1]-(m+d)*y[2]
    
    
    return np.array([f0, f1, f2])


def GG(y,t):
    return np.array([[sig1*y[0]],[sig2*y[1]],[sig3*y[2]]])

result = sdeint.itoint(f, GG, y0, tspan)


plt.plot(tspan,result,label=["S","I","R"])
plt.legend()
plt.show()




