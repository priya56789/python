# Q4. MULTIPLE STORE SALES ANALYSIS (Axis operations)
# You have sales data of 3 stores for 7 days stored in a 2D NumPy array.
# Find:
# - Total sales per store
# - Average sales per day



import numpy as np
sales=np.array([[100,200,300],[400,200,800]])
total_sales=np.sum(sales,axis=1)#Axis 1 means row wise adding and Axis 0 means column wise adding
average_sales=np.mean(sales,axis=0)
print(total_sales)
print()
print(average_sales)