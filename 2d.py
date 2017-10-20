import numpy as np
from scipy.integrate import simps

h = (0.5 - 0.1)/2
eps = 0.1
#m, segunda derivada

#e = 

trap = np.trapz([1.8,2.6,3.0,2.8,1.9], x = [0.1,0.2,0.3,0.4,0.5])
sim = simps(np.array([1.8,2.6,3.0,2.8,1.9]), x = [0.1,0.2,0.3,0.4,0.5])


print "metodo de simpson"
print sim

print "metodo del trapecio"
print trap


