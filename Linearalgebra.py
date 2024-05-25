#%%
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,40,1000)
dr=2.5 * t
ds=3*(t-5)

fig,ax = plt.subplots()
plt.title("A bank Robber Caught")
plt.xlabel('Time(In Minutes)')
plt.ylabel('Distance(In Km)')
ax.set_xlim([0,40])
ax.set_ylim([0,100])
ax.plot(t,dr,c='green')
ax.plot(t,ds,c='brown')
plt.axvline(x=30,color='purple',linestyle='--')
_=plt.axhline(y=75,color='purple',linestyle='--')
# %%

# %%
