import pandas as pd
s=pd.Series([10,20,30])
print(s)


df=pd.DataFrame({"A":[1,0,3,4],"B":[6,7,8,9]})
print(df)
print()

print(df.head(3))
print(df.tail(2))
print()

print(df.info())
print()


print(df.describe())
print()

print(df["A"])
print()


print(df.loc[2])
print(df.iloc[1])
print()


print(df[df["A"]>1])
print()


df["C"]=df["A"]+df["B"]
print(df)
print()


df=df.drop("C",axis=1)
print(df)
print()


print(df.sort_values("A"))
print()

df2=pd.DataFrame({"Name":["Priya","Anjali","Priya","Priya"],"Marks":[30,60,90,120]})
print(df2)
print()
print(df2.groupby("Name").sum())
print()


left=pd.DataFrame({"Name":["PRIYA","VASUNDHARA"],"Maths":[60,90]})
right=pd.DataFrame({"Name":["PRIYA","VASUNDHARA"],"English":[45,30]})
print(pd.merge(left,right,on="Name"))
print()


df=pd.DataFrame({"A":[1,None,3]})
print(df.isnull())
print(df.fillna(0))
print(df.dropna())
print()

df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].apply(lambda x:x*2))
print()


df=pd.DataFrame({"A":["a","b","D"]})
print(df["A"].str.upper())
print()


dates=pd.date_range("2024-01-01",periods=3)
df=pd.DataFrame({"date":dates})
print(df["date"].dt.month)


df=pd.DataFrame({"A":["foo","soo","bar","foo"],"B":["one","two","one","two"],"C":[1,2,3,4]})
print(pd.pivot_table(df,values="C",index="A",columns="B"))



