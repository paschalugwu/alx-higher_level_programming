#!/usr/bin/python3
"""
Let's provide the condition to ensure that
the code is only executed when the file is
run directly, not when it is imported as a module:
"""
if __name__ == "__main__":
    """
    Import the necessary functions from the  calculator_1.py  file:
    """
    from calculator_1 import add, sub, mul, div
    """
    Import the  sys  module to access command-line arguments:
    """
    import sys
    """
    Check if the number of command-line arguments is 3
    using  len(sys.argv) - 1 . If not, print the usage
    message and exit with a value of 1:
    """
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    """
    Create a dictionary  ops  to map the operator symbols to
    the corresponding functions:
    """
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    """
    Check if the operator provided as the second command-line
    argument is valid. If not, print the error message and exit
    with a value of 1:
    """
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    """
    Convert the first and third command-line arguments to integers:
    """
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    """
    Print the result in the specified format using string formatting,
    and execute the corresponding function based on the operator
    provided:
    """
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
