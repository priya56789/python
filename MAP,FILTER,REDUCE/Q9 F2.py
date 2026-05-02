# Use filter() to remove all vowels from a string and print the final string.

text="Hello world"
result="".join(filter(lambda ch:ch.lower() not in "aeiou",text))
print(result)
