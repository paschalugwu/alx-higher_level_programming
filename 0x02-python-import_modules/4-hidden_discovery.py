#!/usr/bin/python3
"""Print all names defined by hidden_4 module."""
"""
 Check if the script is being run directly
 and not imported as a module:
"""
if __name__ == "__main__":
    import hidden_4
    """
    Use the  dir()  function to get a list
    of names defined in the module:
    """
    names = dir(hidden_4)
    # Use a  for  loop to iterate over the names and print them:
    for name in names:
        if name[:2] != "__":
            print(name)
