#  Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].


from functools import reduce
chars=['p','y','t','h','o','n']
result=reduce(lambda a,b:a+b,chars)
print(result)
