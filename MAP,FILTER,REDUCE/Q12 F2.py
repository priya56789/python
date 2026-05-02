# 10. Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers


nums=[5,10,15,20,25,30]
result=list(map(lambda x:x**2,nums))
print(result)
result1=list(filter(lambda x:x%5==0,nums))
print(result1)
from functools import reduce
result2=reduce(lambda a,b:a+b,nums)
print(result2)
