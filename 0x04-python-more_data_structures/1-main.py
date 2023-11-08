#!/usr/bin/python3
# We start by importing our module
search_replace = __import__('1-search_replace').search_replace
# Next, we create the input list my_list
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
"""
Let's call the search_replace function with my_list, the
element to search for (2), and the replacement element (89).
Store the result in new_list.
"""
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
