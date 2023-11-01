#!/usr/bin/python3
"""
To print all the lowercase letters of the
ASCII alphabet, excluding the letters 'q'
and 'e', without any newline characters.
"""
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
