# Project Title: 0x08. Python - More Classes and Objects

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the PEP 8 style guide, checked using `pycodestyle` (version 2.8.*)
- All files must be executable
- File length will be tested using `wc`

## Project Structure
The project is organized into the following directories:

- **alx-higher_level_programming/0x08-python-more_classes:**
  - 0-rectangle.py
  - 1-rectangle.py
  - 2-rectangle.py
  - 3-rectangle.py
  - 4-rectangle.py
  - 5-rectangle.py
  - 6-rectangle.py
  - 7-rectangle.py
  - 8-rectangle.py
  - 9-rectangle.py
  - 101-nqueens.py

## Tasks

### Task 0: Simple Rectangle
- Create an empty class `Rectangle` that defines a rectangle.
- No import statements are allowed.

### Task 1: Real Definition of a Rectangle
- Expand on Task 0 by adding private instance attributes for width and height.
- Implement properties to retrieve and set the values for width and height.
- Implement instantiation with optional width and height parameters.

### Task 2: Area and Perimeter
- Extend Task 1 by adding public instance methods for calculating the area and perimeter of the rectangle.

### Task 3: String Representation
- Build on Task 2 by adding a `__str__` method for a more human-readable string representation of the rectangle.
- Implement a `__repr__` method to create a string representation that can be used to recreate the object using `eval()`.

### Task 4: Eval is Magic
- Enhance Task 3 by modifying the `__repr__` method to include the class name and object address.
- Implement a feature to recreate a new instance using `eval()`.

### Task 5: Detect Instance Deletion
- Further extend the Rectangle class to print a message when an instance is deleted.

### Task 6: How Many Instances
- Add a class attribute `number_of_instances` to keep track of the number of instances created.
- Increment the count during instantiation and decrement during deletion.

### Task 7: Change Representation
- Add a class attribute `print_symbol` to customize the character used for string representation.
- Modify the `__str__` method to use `print_symbol`.
- Demonstrate this customization in the main script.

### Task 8: Compare Rectangles
- Add a static method `bigger_or_equal` to compare two rectangles based on their area.
- Demonstrate the use of this method in the main script.

### Task 9: A Square is a Rectangle
- Implement a class method `square(cls, size=0)` that returns a new Rectangle instance with equal width and height.
- Demonstrate the use of this method in the main script.

### Task 10: N Queens
- Implement a program (`101-nqueens.py`) that solves the N Queens problem.
- The program should take an integer N as a command-line argument.
- Print every possible solution to the problem, one solution per line.
- The format should be specified as per the example in the task description.

## Usage
To run the N Queens solver, use the following command:

```bash
./101-nqueens.py N
```

Replace N with the desired integer value. If the input is invalid, the program will print an appropriate error message.

## Example
```bash
./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Author
This project was developed by Paschal Ugwu.
