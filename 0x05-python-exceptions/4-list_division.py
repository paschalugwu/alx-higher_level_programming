#!/usr/bin/python3
"""The task requires you to write a function called list_division that
takes two lists, my_list_1 and my_list_2, and a list_length as input.
The function should divide the elements of the two lists element by
element and return a new list of length list_length with the division
results. If two elements cannot be divided, the division result should
be equal to 0. If an element is not an integer or float, it should
print "wrong type". If the division by 0 occurs, it should print
"division by 0". If my_list_1 or my_list_2 is too short, it should
print "out of range". You need to use try, except, and finally blocks
to handle exceptions, and you are not allowed to import any modules.
We stary by defining the function list_division with the my_list_1,
my_list_2, and list_length parameters"""


def list_division(my_list_1, my_list_2, list_length):
    # Initialize an empty list new_list to store the division results
    new_list = []
    # Use a for loop to iterate over the rage from 0 to list_length
    for i in range(list_length):
        """Inside the loop, use a try block to attempt to perform the
        division of the corresponding element from my_list_1 and my_list_2"""
        try:
            div = my_list_1[i] / my_list_2[i]
            """If the division is successful, assign the result to a variable
            div. If an exception (TypeError) occurs during the division, catch
            the exception using an except block, print "wrong type", and
            assign 0 to div"""
        except TypeError:
            print("wrong type")
            div = 0
            """If the exception (ZeroDivisionError) occurs during the divison,
            catch the exception using an except block, print "division by 0",
            and assign 0 to div"""
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            """If the exception (IndexError) occurs during the division, catch
            the exception using an except block, print "out of range",
            assign 0 to div"""
        except IndexError:
            print("out of range")
            div = 0
            """Use the finally block to always append the value of div
            to the new_list"""
        finally:
            new_list.append(div)
            # After the loop, return the new_list
    return new_list
