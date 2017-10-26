
import math

def derivada(f):
    def df(x, h=0.1e-5):
        return ( f(x+h/2) - f(x-h/2) )/h
    return df

def g(x): return math.log(x)

primeraDerivada = derivada( g )
segundaDerivada = derivada( primeraDerivada )

print ("f''(1.8) = ")
print (segundaDerivada( 1.8 ))
