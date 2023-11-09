#!/usr/bin/python3
"""
Start by defining the function  weight_average
that takes in a single parameter,  my_list .
"""


def weight_average(my_list=[]):
    """
    Inside the function, use an  if  statement to check if
    my_list  is empty. You can use the  not  keyword to
    check if the list is empty
    """
    if not my_list:
        """
        If  my_list  is empty, return 0
        """
        return 0
        """
        Initialize two variables,  num  and  den , to 0. These variables
        will be used to calculate the numerator and denominator of the
        weighted average
        """
    num = 0
    den = 0
    """
    Iterate over each tuple  tup  in  my_list
    """
    for tup in my_list:
        """
        Inside the loop, update the  num  variable by adding the product
        of the score ( tup[0] ) and its weight ( tup[1] )
        """
        num += tup[0] * tup[1]
        """
        Inside the loop, update the  den  variable by
        adding the weight ( tup[1] )
        """
        den += tup[1]
        """
        After the loop, calculate the weighted average
        by dividing  num  by  den
        """
    return (num / den)
