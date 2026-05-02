#  Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?





# Both
# map(str, [1, 2, 3]) and map(lambda x: str(x), [1, 2, 3])  produce the same result

# Faster:map(str, [1, 2, 3])
# str is a built-in function (optimized, no extra overhead)

# lambda x: str(x) adds an extra function call for every element
#map(str, ...) is  faster and more efficient
