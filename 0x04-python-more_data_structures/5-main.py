#!/usr/bin/python3
# Let's import our module
number_keys = __import__('5-number_keys').number_keys
# Next, we create the input dictionary my_dictionary
my_dictionary = {'language': "C", 'number': "13", 'track': "Low level"}
"""
Let's now call the number_keys function with my_dictionary as an argument
and store the result in nb_keys
"""
nb_keys = number_keys(my_dictionary)
"""
Finally, we print the number of keys in the dictionary
using the format() method
"""
print("Number of keys: {:d}".format(nb_keys))
