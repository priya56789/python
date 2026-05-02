#  Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.


s="Hello"
ascii_list=list(map(ord,s))
print(ascii_list)