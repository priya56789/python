# Q5. MATRIX MULTIPLICATION IN RECOMMENDATION SYSTEM
# You are given:
# - User preference matrix
# - Product feature matrix
#
# Perform matrix multiplication to compute recommendation scores.
#



import numpy as np
arr1=np.array([[1,2],
              [3,4]])
arr2=np.array([[4,5],
              [6,7]])
arr3=np.dot(arr1,arr2)
print(arr3)