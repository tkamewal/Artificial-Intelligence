import numpy as np
import tensorflow as tf
import torch 
a=np.array([2,3,4,5])
print(a)
print(type(a))
b=torch.tensor([2,3,4,5])
c=tf.Variable([2,3,4,5])
print(b)
print(type(b))
print(c)
print(type(c))