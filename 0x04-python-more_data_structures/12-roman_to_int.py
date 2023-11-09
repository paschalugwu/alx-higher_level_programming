#!/usr/bin/python3
"""
Create a helper function  to_subtract  that takes in a
list of numbers  list_num and calculates the value to
subtract from the maximum number in the list
"""


def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)
    for n in list_num:
        if max_list > n:
            to_sub += n
    return (max_list - to_sub)


"""
Start by defining the function  roman_to_int
that takes in a single parameter,  roman_string .
"""


def roman_to_int(roman_string):
    """
    Inside the function, use an  if  statement to check if  roman_string
    is  None  or not a string. You can use the  isinstance()
    function to check if  roman_string  is an instance of the  str  class
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
        """
        Create a dictionary  rom_n  that maps each Roman numeral character
        to its corresponding integer value
        """
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())
    """
    Initialize a variable  num  to 0 to store the final integer value
    """
    num = 0
    """
    Initialize a variable  last_rom  to 0 to store the value of the
    last Roman numeral encountered
    """
    last_rom = 0
    """
    Initialize a list  list_num  with a single element 0
    to keep track of the values encountered during the iteration
    """
    list_num = [0]
    """
    Iterate over each character  ch  in  roman_string
    """
    for ch in roman_string:
        """
        Inside the loop, iterate over each key  r_num  in
        the list of keys of the  rom_n  dictionary
        """
        for r_num in list_keys:
            """
            Inside the inner loop, check if  r_num  is equal to  ch .
            If they are equal, compare the current Roman numeral
            value with the previous one
            """
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))
                last_rom = rom_n.get(ch)
                """
                After the loop, add the value to subtract from
                the last set of numbers in  list_num  to the final  num
                """
    num += to_subtract(list_num)
    """
    Finally, return the  num  as the converted integer value
    """
    return num
