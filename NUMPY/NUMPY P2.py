# Q2. SENSOR DATA CLEANING (Boolean Indexing)
# You receive temperature sensor data as a NumPy array.
# Remove all invalid readings where values are less than -10 or greater than 50.


import numpy as np
data=np.array([10,20,30,40,80,90,-20,-13,-2])
clean_data=data[(data>-10) & (data<50)]
print(clean_data)

