# Q6. E-COMMERCE ORDER ANALYSIS (Filtering + Aggregation)
# You are given a DataFrame with columns:
# ["order_id", "customer", "amount", "status"]
#
# Tasks:
# - Filter only completed orders
# - Calculate total revenue
# - Find top 3 highest orders


import pandas as pd
data={"order_id":[1,2,3,4],"customer":["priya","anjali","Sasi","vasundhara"],"amount":[1000,2000,3000,4000],"status":["completed","pending","completed","completed"]}
df=pd.DataFrame(data)
completed_orders=df[df["status"]=="completed"]
print(completed_orders)
total_revenue=completed_orders["amount"].sum()
print(total_revenue)
highest_orders=completed_orders.sort_values(by="amount").head(3)
print(highest_orders)