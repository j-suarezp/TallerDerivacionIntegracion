from math import *

def cuadraturaGauss(f, a, b):
    t1 = -( b - a ) / 2 * 1 / sqrt( 3 ) + ( b + a ) / 2
    t2 = ( b - a ) / 2 * 1 / sqrt( 3 ) + ( b + a ) / 2
    s = ( b - a) / 2 * ( f( t1 ) + f( t2 ) )
    return s

def cuadraturaGaussIntervalos( f, a, b, m ):
    h = ( b - a ) / m
    s = 0
    x = a
    for i in range( m ):
        a = x + i * h
        b = x + ( i + 1 ) * h
        s = s + cuadraturaGauss( f, a, b )
        
    return s
        
def f(x):
    return x * exp( x )

s = cuadraturaGaussIntervalos( f, 1, 2, 3 )
print( "El valor de la integral usando la cuadratura de Gauss es: ")
print(s)

