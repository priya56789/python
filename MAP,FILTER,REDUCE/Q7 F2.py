
# 3. Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically.

from functools import reduce
nums=[12,45,7,89,34,2]
largest=reduce(lambda a,b: a if a>b else b,nums)
print("largest_number:",largest)
