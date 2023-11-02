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
    Find the length of the  sys.argv  list to determine the
    number of arguments:
    """
    length = len(sys.argv)
    """
    Use a loop to iterate over the command-line arguments and
    add them to the  total variable. Start the loop from index
    1 to exclude the script name itself:
    """
    for i in range(1, length):
        total += int(sys.argv[i])
        """
        Print the  total  value followed by a new
        line using string formatting:
        """
        print("{}".format(total))
