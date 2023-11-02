#!/usr/bin/python3

# Import the  sys  module to access the command-line arguments
import sys

"""
Use the  if __name__ == "__main__":  condition to ensure
the code is only executed when the script is run directly,
not when imported as a module
"""
if __name__ == "__main__":

    # Get the number of arguments passed to the script using  len(sys.argv)
    num_args = len(sys.argv) - 1

    # Print the number of arguments in the specified format
    print("{} argument{}:".format(num_args, "s" if num_args != 1 else ""))

    """
    Check if there are any arguments and iterate over them using a
    for  loop
    """
    if num_args > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("No arguments.")
