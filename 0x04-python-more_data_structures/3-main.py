#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements
# Let's create the input sets set_1 and set_2
set_1 = {"Python", "C", "Javascript"}
Set_2 = {"Bash", "C", "Ruby", "Perl"}
"""
Let's now call common_elements function with set_1
and set_2 as arguments and store the result in c_set
"""
c_set = common_elements(set_1, Set_2)
# Let's convert c_set to a sorted list using the list() function
c_list = list(c_set)
# Let's sort c_list using the sorted() function
sorted_list = sorted(c_list)
"""
Finally, we print to display the common elements
between the two sets
"""
print(sorted_list)
