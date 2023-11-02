#!/usr/bin/python3
"""
Check if the script is being executed directly by adding the following code:
"""
if __name__ == "__main__":
    # Import the  sys  module to work with command-line arguments:
    import sys
    # Initialize a variable  total  to store the sum of the arguments:
    total = 0
    """
    Use a  for  loop to iterate over the command-line arguments
    and add them to the  total  variable:
    """
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
        """
        Print the  total  value followed by a new
        line using string formatting:
        """
        print("{}".format(total))
