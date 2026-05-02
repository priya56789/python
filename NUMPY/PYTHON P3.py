# Q3. NORMALIZATION FOR ML MODEL (Vectorization)
# Given a dataset (NumPy array), normalize all values between 0 and 1
# using min-max normalization.
#
#  Formula: (x - min) / (max - min)



import numpy as np
data=np.array([10,20,30,40,50])
normalized_data=(data-np.min(data))/(np.max(data)-np.min(data))
print(normalized_data)












