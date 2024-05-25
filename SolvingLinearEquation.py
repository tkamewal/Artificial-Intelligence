import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,1000)

y1= 3*x
y2= 1+(5*x)/2

fig, ax= plt.subplots()
plt.xlabel('X')
plt.ylabel('Y')
ax.set_xlim([0,3])
ax.set_ylim([0,10])
ax.plot(x,y1,c='green')
ax.plot(x,y2,c='brown')
plt.axvline(x=2,color='purple',linestyle='--')
_=plt.axhline(y=6,color='purple',linestyle='--')