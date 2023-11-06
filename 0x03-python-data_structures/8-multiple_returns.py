#!/usr/bin/python3
"""
Let's start by defining the function `multiple_returns`
with one parameter: `sentence`
"""


def multiple_returns(sentence):
    """
    Inside the function, let's calculate the length of the sentence using
    len() function and store it in a variable called sentence_length
    """
    sentence_length = len(sentence)
    """
    Inside the function, we check if the length of the sentence is
    equal to 0. If it is, create a new tuple with the sentence length
    and None as the first character
    """
    if sentence == 0:
        new_tuple = (sentence_length, None)
        """
        If the length of the sentence is not 0, create a new tuple with the
        sentence length and the first character of the sentence.
        """
    else:
        new_tuple = (sentence_length, sentence[0])
    return new_tuple
