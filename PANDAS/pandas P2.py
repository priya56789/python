# Q7. EMPLOYEE PERFORMANCE REPORT (GroupBy)
# Given a dataset:
# ["employee", "department", "salary"]
#
# Tasks:
# - Find average salary per department
# - Find department with highest average salary
#



import pandas as pd
data={"employee":["priyanka","anjali","bhavana"],"department":["analyst","developer","mapping"],"salary":[10000,20000,5000]}
df=pd.DataFrame(data)
average_salary=df.groupby("department")["salary"].mean().astype(int)
print(average_salary)
highest_salary=average_salary.idxmax()
print(highest_salary)