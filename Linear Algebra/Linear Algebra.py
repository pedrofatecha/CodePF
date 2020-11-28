import pandas as pd
import scipy as spy
import numpy as npy
import matplotlib.pyplot as plt

x=[i for i in range(-10,10)]
y=[4-i for i in x]
r=x
w=[((2*i)-4)/2 for i in r]

plt.plot([min(x),max(x)],[0,0], 'k--')
plt.plot([0,0],[min(min(y),min(w)),max(max(y), max(w))], 'k--')

plt.plot(x,y)
plt.plot(r,w)
plt.show()

A=npy.array([[1,2],[1,-2]])
b=npy.array([4,4])

x=npy.linalg.solve(A,b)
