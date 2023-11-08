#!/usr/bin/python3
# Let's start by importing the module
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements
# Let's also create the input sets set_1 and set_2
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
"""
Next, we call the only_diff_elements function with set_1 and set_2
as arguments and store the result in od_set.
"""
od_set = only_diff_elements(set_1, set_2)
# Convert od_set to sorted list using the list() function
od_list = list(od_set)
# Sort od_list using the sorted() function
sorted_list = sorted(od_list)
"""
Finally, we print the sorted_list to display the elements
that are present in only one of the input sets 
"""
print(od_list)
