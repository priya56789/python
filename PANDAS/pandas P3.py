# Q8. DATA CLEANING PIPELINE (Missing Values)
# You are given a dataset with missing values.
#
# Tasks:
# - Identify missing values
# - Fill missing values using mean
#


import pandas as pd
import numpy as np
data={"a":[10,20,np.nan],"b":[40,np.nan,60],"c":[40,80,np.nan]}
df=pd.DataFrame(data)
print(df.isnull())
df_filled=df.fillna(df.mean(numeric_only=True))
print(df_filled)
