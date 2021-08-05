#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)


# In[ ]:


#Question 2
import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)


# In[ ]:


#Question 3
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))


# In[ ]:


#Question 4
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))


# In[ ]:


#Question 5
import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

