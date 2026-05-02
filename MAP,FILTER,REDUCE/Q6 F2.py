# 2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.


d={"apple":100,"banana":40,"cherry":150}
result=list(filter(lambda key:d[key]>50,d))
print(result)