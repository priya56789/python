# Q9. LOG FILE ANALYSIS (String + DateTime)
# You have a dataset with columns:
# ["timestamp", "log_message"]
#
# Tasks:
# - Extract year from timestamp
# - Find logs containing "ERROR"
# - Count number of errors per year




import pandas as pd
data={"timestamp":["2026-12-8 10:00:00","2021-01-12 12:00:00"],"log_message":["Info end","Error Crashed"]}
df=pd.DataFrame(data)
df["year"]=pd.to_datetime(df["timestamp"]).dt.year
print(df)
print()
error_logs=df[df["log_message"].str.contains("ERROR")]
print(error_logs)
print()
error_count=error_logs.groupby("year").size()
print(error_count)