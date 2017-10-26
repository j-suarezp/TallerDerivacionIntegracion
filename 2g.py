import math
import matplotlib.pyplot as plt
import numpy as np

def trapecios( f, a, b, m):
    h = ( b - a ) / m
    s = 0
    for i in range( 1, m ):
        s = s + f( a + i * h)
    r = h / 2 * ( f( a ) + 2 * s + f( b ) )
    return r


def biseccion( f, a, b, e ):
    while b - a >= e:
        c = ( a + b ) / 2
        if f( c ) == 0:
            return c
        else:
            if f( a ) * f( c ) > 0:
                a = c
            else:
                b = c 
    return c
            

def f(x): 
    return 4 + math.cos( x + 1 )
def g(x):
    return math.exp(x) * math.sin(x)
def h(x):
    return g(x) - f(x)

a = biseccion( h, 1, 1.5, 0.0001 )
b = biseccion( h, 3, 3.2, 0.0001 )

m = 10
print("El area entre lafuncion f y la g es: ", trapecios(h, a, b, m))

#El area entre lafuncion f y la g es: 4.17381709035612
