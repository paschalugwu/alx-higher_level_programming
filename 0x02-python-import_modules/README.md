# Project Title: Python Import and Modules

This project consists of several Python scripts that demonstrate various aspects of importing functions and modules in Python. Each script has a specific task and set of requirements. Below, you'll find a brief overview of each script and its functionality.

## Table of Contents
1. Import a Simple Function
2. My First Toolbox
3. How to Make a Script Dynamic
4. Infinite Addition
5. Who Are You?
6. Everything Can Be Imported
7. Build My Own Calculator
8. Easy Print
9. ByteCode to Python
10. Fast Alphabet

## 1. Import a Simple Function
**Description:** This script imports a simple function,  `add(a, b)` , from the file  `add_0.py`  and prints the result of adding 1 + 2 = 3.

**Requirements:**
- Use the print function with string formatting to display integers.
- Assign the value 1 to a variable called  `a`  and 2 to a variable called  `b` .
- Use these variables as arguments when calling the  `add`  function and printing the result.
-  `a`  and  `b`  must be defined in two different lines:  `a = 1`  and  `b = 2` .
- Your program should print:  `<a value> + <b value> = <add(a, b) value>`  followed by a new line.
- Use the word  `add_0`  only once in your code.
- Do not use  `*`  for importing or  `__import__` .
- The code should not be executed when imported.

## 2. My First Toolbox
**Description:** This script imports functions from the file  `calculator_1.py` , performs mathematical operations, and prints the results.

**Requirements:**
- Do not use the print function more than 4 times.
- Assign the value 10 to a variable  `a`  and 5 to a variable  `b` .
- Use these variables only as arguments when calling functions (including print).
-  `a`  and  `b`  must be defined in two different lines:  `a = 10`  and  `b = 5` .
- Your program should call each of the imported functions and print the results in the specified format.
- The word  `calculator_1`  should be used only once in your file.
- Do not use  `*`  for importing or  `__import__` .
- The code should not be executed when imported.

## 3. How to Make a Script Dynamic
**Description:** This script prints the number of and the list of its arguments.

**Requirements:**
- Output format: "Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by : (or . if no arguments were passed) followed by a new line."
- For each argument (if at least one), print one line with the position of the argument, a colon, the argument value, and a new line.
- The code should not be executed when imported.
- Use  `len(argv)`  to determine the number of arguments.

## 4. Infinite Addition
**Description:** This script prints the result of adding all arguments.

**Requirements:**
- The output is the result of the addition of all arguments followed by a new line.
- Arguments can be cast into integers using  `int()` .
- The code should not be executed when imported.

## 5. Who Are You?
**Description:** This script prints all the names defined by the compiled module  `hidden_4.pyc` .

**Requirements:**
- Print one name per line, in alphabetical order.
- Print only names that do not start with  `__` .
- The code should not be executed when imported.
- Run the code in Python 3.8.x as  `hidden_4.pyc`  has been compiled with this version.

## 6. Everything Can Be Imported
**Description:** This script imports the variable  `a`  from the file  `variable_load_5.py`  and prints its value.

**Requirements:**
- Do not use  `*`  for importing or  `__import__` .
- The code should not be executed when imported.

## 7. Build My Own Calculator
**Description:** This script imports functions from the file  `calculator_1.py`  and performs basic operations based on user input.

**Requirements:**
- Usage:  `./100-my_calculator.py a operator b` .
- If the number of arguments is not 3, print usage and exit with value 1.
- Supported operators:  `+`  for addition,  `-`  for subtraction,  `*`  for multiplication,  `/`  for division.
- If the operator is not one of the above, print an error message and exit with value 1.
- Cast  `a`  and  `b`  into integers using  `int()` .
- Print the result in the specified format.
- Do not use  `*`  for importing or  `__import__` .
- The code should not be executed when imported.

## 8. Easy Print
**Description:** This script prints "#pythoniscool" in the standard output.

**Requirements:**
- The code should be a maximum of 2 lines long.
- Do not use  `print` ,  `eval` ,  `open` , or  `import sys` .

## 9. ByteCode to Python
**Description:** This script defines a Python function,  `magic_calculation(a, b)` , that emulates the behavior of a given Python bytecode.

**Requirements:**
- You need to define the function according to the specified bytecode.

## 10. Fast Alphabet
**Description:** This script prints the alphabet in uppercase, followed by a new line, using a specific constraint.

**Requirements:**
- The code should be a maximum of 3 lines long.
- Do not use loops, conditional statements,  `str.join()` , string literals, or system calls.
