#%%
import torch
import matplotlib.pyplot as plt

x=torch.tensor([0,1,2,3,4,5,6,7.])

# y=-0.5 * x + 2 + torch.normal(mean=torch.zeros(8), std=0.2)


y=torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])

fig, ax=plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug Dosage (ml)")
plt.ylabel("Forgetfulness")
_=ax.scatter(x, y)


# %%
