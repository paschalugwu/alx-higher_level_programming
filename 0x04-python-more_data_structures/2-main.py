#!/usr/bin/python3
# import the uniq_add module
uniq_add = __import__('2-uniq_add').uniq_add
# Create the input list my_list
my_list = [1, 2, 3, 1, 4, 2, 5]
"""
Let's call the uniq_add function with my_list as
an argument and store the result in `result`
"""
result = uniq_add(my_list)
"""
Finally, we print the result using the format() method
to display the sum of the unique integers
"""
print("Result: {:d}".format(result))
