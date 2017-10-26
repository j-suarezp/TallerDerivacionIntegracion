from math import *
from sympy import *

M = [10.0, 100.0, 1000.0]
l = 0.0
h = 2.0
x = Symbol('x')

def trapecios(f,a,b,m):
    h = (b-a)/m
    s=0.0
    for i in range(1,int(m)):
        s=s+f(a+i*h)
    r=h/2.0*(f(a)+2.0*s+f(b))
    return r

for i in M:
    experimental = trapecios(sin, l, h, i)
    real = integrate(sin(x),(x,l,h))
    error = (abs(real - experimental) / real) * 100
    print ("El error es del: ", round(error,4),"%")
    
#El error es del:  0.3336 %
#El error es del:  0.0033 %
#El error es del:  0.0 %
#Entre mayor sea el m, menor es el error
