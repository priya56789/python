# Q10. MERGING MULTIPLE DATA SOURCES (Join/Merge)
# You are given:
# - Customers DataFrame
# - Orders DataFrame
#
# Tasks:
# - Merge both datasets on customer_id
# - Find total purchase amount per customer
#



import pandas as pd
customers=pd.DataFrame({"customer_id":[1,2,3,4],"name":["priya","Anjali","Sasi","chikki"]})
orders=pd.DataFrame({"customer_id":[1,2,3,4],"amount":[100,200,300,400]})
merged=pd.merge(customers,orders,on="customer_id")
print(merged)
total_purchase=merged.groupby("name")["amount"].sum()
print(total_purchase)