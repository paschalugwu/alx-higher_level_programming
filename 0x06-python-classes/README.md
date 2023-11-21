## Project Overview

This project involves developing a series of Python scripts that implement a `Square` class with various functionalities, including creating and manipulating square instances, defining attributes, validating inputs, and implementing methods for calculating area and printing squares. The project also includes advanced tasks involving linked lists, comparisons between square instances, and a class that replicates a given Python bytecode.

## Project Structure

The project is organized into a GitHub repository named `alx-higher_level_programming` with the following directory structure:

```
Directory: 0x06-python-classes
```

The repository contains the following files:

* `0-square.py`: Defines an empty class `Square` that represents a square.

* `1-square.py`: Extends the `Square` class to include a private instance attribute `size`. Provides instantiation with `size` and prevents external access to the `size` attribute.

* `2-square.py`: Adds size validation to the `Square` class. Raises `TypeError` for non-integer sizes and `ValueError` for sizes less than 0.

* `3-square.py`: Introduces a public instance method `area` to calculate the square area.

* `4-square.py`: Implements getter and setter methods for the `size` attribute. Centralizes type and value validation logic.

* `5-square.py`: Adds a public instance method `my_print` to print the square using the '#' character. Handles cases where `size` is equal to 0.

* `6-square.py`: Extends the `Square` class to include a private instance attribute `position`. Modifies the `my_print` method to use space for positioning.

* `100-singly_linked_list.py`: Defines a singly linked list with a class `Node` for individual nodes and `SinglyLinkedList` for the list itself. Implements a method to insert nodes into the list in sorted order.

* `101-square.py`: Enhances the `Square` class to have a string representation matching the output of the `my_print` method.

* `102-square.py`: Allows square instances to be compared using standard comparators based on their area.

* `103-magic_class.py`: Implements a class `MagicClass` replicating a given Python bytecode.

## Running the Scripts

To run any of the scripts, execute them from the command line using Python. For example:

```bash
python3 0-main.py
```

Replace `0-main.py` with the desired script filename.

## Task-specific Notes

* **Task 0:** Defines a basic empty class `Square`.

* **Task 1:** Extends the `Square` class to include a private size attribute.

* **Task 2:** Adds size validation to the `Square` class.

* **Task 3:** Introduces a public method `area` to calculate the square area.

* **Task 4:** Implements getter and setter methods for the `size` attribute.

* **Task 5:** Adds a public method `my_print` to print the square using the '#' character.

* **Task 6:** Extends the `Square` class to include a private position attribute.

* **Task 7:** Defines a singly linked list with insertion in sorted order.

* **Task 8:** Enhances the `Square` class to have a string representation matching the output of the `my_print` method.

* **Task 9:** Allows square instances to be compared using standard comparators based on their area.

* **Task 10:** Implements a class `MagicClass` replicating a given Python bytecode.

## Important Information

* All scripts are written in Python 3.

* No external modules are imported in the scripts, as specified in the tasks.

* Verify your Python version is 3.x before running the scripts.
