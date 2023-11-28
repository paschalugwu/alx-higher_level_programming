# Python Test-Driven Development Project

## Introduction
Welcome to the Python Test-Driven Development project! This project focuses on enhancing your understanding of Python programming through the practice of Test-Driven Development (TDD). Test-Driven Development is a software development approach where tests are written before the actual code. This helps ensure the reliability and correctness of your code from the outset.

## Project Details

### Concepts
In this project, the key concept to focus on is:
- **Never forget a test**

### Background Context
This project introduces important considerations for Python projects on the intranet. Some key points to keep in mind include:
- Always write documentation and tests before coding.
- Intranet checks for Python projects won't be released before their first deadline to emphasize TDD.
- Collaboration on test cases is encouraged to cover all possible edge cases.
- Do not trust user input; always think about all possible edge cases.

### Resources
To successfully complete this project, make sure to read or watch the following resources:
- [doctest](https://docs.python.org/3/library/doctest.html) – Test interactive Python examples (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html)

### Learning Objectives
By the end of this project, you should be able to explain the following without external assistance:
- Why Python programming is awesome
- What an interactive test is
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- Basic option flags to create tests
- How to find edge cases

### Copyright - Plagiarism
Remember, you are responsible for creating solutions for the tasks outlined in this project to meet the specified learning objectives. Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files must end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All files should end with a new line
- All test files should be inside a folder named `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (length will be verified)
- Collaboration on test cases is strongly encouraged

## Project Structure
The project should be organized within the following GitHub repository and directory structure:

- **GitHub repository:** alx-higher_level_programming
- **Directory:** 0x07-python-test_driven_development

### Files
1. **0-add_integer.py**
    - Write a function that adds two integers.
    - Prototype: `def add_integer(a, b=98):`
    - `a` and `b` must be integers or floats, otherwise, raise a `TypeError` exception.
    - `a` and `b` must be casted to integers if they are floats.
    - Returns an integer: the addition of `a` and `b`.
    - No importing of any module allowed.

    Example:
    ```python
    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))       # Output: 3
    print(add_integer(100, -2))    # Output: 98
    print(add_integer(2))          # Output: 100
    print(add_integer(100.3, -2))   # Output: 98
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 0-add_integer.py, tests/0-add_integer.txt

2. **2-matrix_divided.py**
    - Write a function that divides all elements of a matrix.
    - Prototype: `def matrix_divided(matrix, div):`
    - `matrix` must be a list of lists of integers or floats.
    - Raise `TypeError` if `matrix` is not valid.
    - Each row of the matrix must be of the same size.
    - `div` must be a number (integer or float).
    - Raise `TypeError` for invalid `div`.
    - `div` can't be equal to 0.
    - Divide all elements of the matrix by `div`, rounded to 2 decimal places.
    - Returns a new matrix.

    Example:
    ```python
    matrix_divided = __import__('2-matrix_divided').matrix_divided

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    ```

    Output:
    ```
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 2-matrix_divided.py, tests/2-matrix_divided.txt

3. **3-say_my_name.py**
    - Write a function that prints "My name is \<first name\> \<last name\>".
    - Prototype: `def say_my_name(first_name, last_name=""):`
    - `first_name` and `last_name` must be strings.
    - Raise `TypeError` for invalid inputs.

    Example:
    ```python
    say_my_name = __import__('3-say_my_name').say_my_name

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    ```

    Output:
    ```
    My name is John Smith
    My name is Walter White
    My name is Bob
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 3-say_my_name.py, tests/3-say_my_name.txt



4. **4-print_square.py**
    - Write a function that prints a square with the character `#`.
    - Prototype: `def print_square(size):`
    - `size` is the size length of the square.
    - Raise `TypeError` for invalid inputs.
    - Raise `ValueError` if `size` is less than 0.
    - Output a square using `#`.

    Example:
    ```python
    print_square = __import__('4-print_square').print_square

    print_square(4)
    ```

    Output:
    ```
    ####
    ####
    ####
    ####
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 4-print_square.py, tests/4-print_square.txt

5. **5-text_indentation.py**
    - Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.
    - Prototype: `def text_indentation(text):`
    - `text` must be a string.
    - Raise `TypeError` for invalid inputs.

    Example:
    ```python
    text_indentation = __import__('5-text_indentation').text_indentation

    text_indentation("Lorem ipsum dolor sit amet. Consectetur adipiscing elit.")
    ```

    Output:
    ```
    Lorem ipsum dolor sit amet.
    Consectetur adipiscing elit.
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 5-text_indentation.py, tests/5-text_indentation.txt

6. **6-max_integer.py**
    - Write a function `max_integer` that finds and returns the maximum integer in a list.
    - Prototype: `def max_integer(list=[]):`
    - Return `None` for an empty list.
    - Raise a `ValueError` if the list contains non-integer elements.

    Example:
    ```python
    max_integer = __import__('6-max_integer').max_integer

    print(max_integer([1, 2, 3, 4]))    # Output: 4
    print(max_integer([1, 3, 4, 2]))    # Output: 4
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 6-max_integer.py, tests/6-max_integer_test.py

7. **100-matrix_mul.py**
    - Write a function that multiplies two matrices.
    - Prototype: `def matrix_mul(m_a, m_b):`
    - Validate `m_a` and `m_b` according to specified requirements.
    - Raise `ValueError` if `m_a` and `m_b` cannot be multiplied.
    - Use standard Python, no importing of any module.
    - Returns a new matrix.

    Example:
    ```python
    matrix_mul = __import__('100-matrix_mul').matrix_mul

    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    ```

    Output:
    ```
    [[7, 10], [15, 22]]
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 100-matrix_mul.py, tests/100-matrix_mul.txt

8. **101-lazy_matrix_mul.py**
    - Write a function that multiplies two matrices using the NumPy module.
    - Prototype: `def lazy_matrix_mul(m_a, m_b):`
    - Test cases should be the same as in `100-matrix_mul`, but with new exception type/message.

    Example:
    ```python
    lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    ```

    Output:
    ```
    [[7, 10], [15, 22]]
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt

9. **102-python.c**
    - Create a function `print_python_string` that prints Python strings.
    - Prototype: `void print_python_string(PyObject *p);`
    - Format should follow the specified example.
    - If `p` is not a valid string, print an error message.
    - Use C standard library.

    Example:
    ```python
    import ctypes

    lib = ctypes.CDLL('./libPython.so')
    lib.print_python_string.argtypes = [ctypes.py_object]
    s = "The spoon does not exist"
    lib.print_python_string(s)
    ```

    Output:
    ```
    [.] string object info
      type: compact ascii
      length: 24
      value: The spoon does not exist
    ```

    - **Repo:**
        - GitHub repository: alx-higher_level_programming
        - Directory: 0x07-python-test_driven_development
        - File: 102-python.c

## Conclusion
This project is designed to reinforce your understanding of Python programming principles and Test-Driven Development. Remember to follow the specified requirements for each task, write meaningful documentation, and collaborate on test cases to cover all possible scenarios. Good luck, and have fun!
