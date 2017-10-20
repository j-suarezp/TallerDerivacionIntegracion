from math import *
import matplotlib.pyplot as plt
import numpy as np

def f(x):return x*exp(x)

r=5.436563656918091

x=np.linspace(0.0000000000001,0.1,1000)
y=[]

for h in x:
  d=(f(1+h)-f(1))/h
  e=abs(r-d)
  y.append(e)
  print('%18.15f %18.15f %18.15f %18.15f'%(h,r,d,e))
  

plt.plot(x,y)
plt.xlabel("h")
plt.ylabel("P")

plt.show()

