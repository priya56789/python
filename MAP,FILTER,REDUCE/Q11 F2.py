# Given a list of integers, use map() with id() to print the memory address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.


nums=[10,20,30,350,20]
addresses=list(map(id,nums))
print(addresses)
