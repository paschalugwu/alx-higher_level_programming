# Python Input/Output Project

## Overview

This repository contains a set of Python scripts that cover various aspects of file handling, JSON serialization, and related tasks. Each script is designed to fulfill specific requirements and demonstrates practical use cases.

## Project Structure

- **0x0B-python-input_output/**
  - **0-read_file.py**: Read a text file and print its content to stdout.
  - **1-write_file.py**: Write a string to a text file and return the number of characters written.
  - **2-append_write.py**: Append a string to the end of a text file and return the number of characters added.
  - **3-to_json_string.py**: Return the JSON representation of an object (string).
  - **4-from_json_string.py**: Return an object (Python data structure) represented by a JSON string.
  - **5-save_to_json_file.py**: Write an object to a text file using a JSON representation.
  - **6-load_from_json_file.py**: Create an object from a JSON file.
  - **7-add_item.py**: Script to add items to a Python list, save them to a file, and load them back.
  - **8-class_to_json.py**: Function to return the dictionary description for JSON serialization of a class instance.
  - **9-student.py**: Class definition for a student with a `to_json` method.
  - **10-student.py**: Extended class with a `to_json` method that supports attribute filtering.
  - **11-student.py**: Class with `to_json` and `reload_from_json` methods for serialization and deserialization.
  - **12-pascal_triangle.py**: Function to generate Pascal's triangle up to a given level.
  - **100-append_after.py**: Function to insert a line of text into a file after each line containing a specific string.
  - **101-stats.py**: Script to compute metrics based on a log input format.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-higher_level_programming.git
   cd alx-higher_level_programming/0x0B-python-input_output
   ```

2. Execute the desired Python scripts based on the specific tasks you want to perform.

## Example Usage

### Task 1: Read a file (0-read_file.py)

```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
```

### Task 3: Write to a file (1-write_file.py)

```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
```

### Task 5: Append to a file (2-append_write.py)

```python
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
```

### Task 7: To JSON string (3-to_json_string.py)

```python
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
```

### Task 9: From JSON string to Object (4-from_json_string.py)

```python
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
```

### Task 11: Save Object to a file (5-save_to_json_file.py)

```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)
```

### Task 13: Create object from a JSON file (6-load_from_json_file.py)

```python
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
```

### Task 15: Load, add, save (7-add_item.py)

```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))


try:
    my_list = load_from_json_file(filename)
    print(my_list)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

### Task 17: JSON string representation of a class instance (8-class_to_json.py)

```python
#!/usr/bin/python3
class_to_json = __import__('8-class_to_json').class_to_json

class_to_json_obj = class_to_json()
print(class_to_json_obj)
```

### Task 19: Student to JSON with filter (10-student.py)

```python
#!/usr/bin/python3
Student = __import__('10-student').Student

student = Student()
student.first_name = "John"
student.last_name = "Doe"
student.age = 23

json_student = student.to_json(["first_name", "age"])
print(json_student)
```

### Task 21: Student to JSON with filter (11-student.py)

```python
#!/usr/bin/python3
Student = __import__('11-student').Student

student = Student()
student.first_name = "John"
student.last_name = "Doe"
student.age = 23

json_student = student.to_json(["first_name", "age"])
print(json_student)
```

### Task 23: Student to disk and reload (12-student.py)

```python
#!/usr/bin/python3
Student = __import__('12-student').Student

student = Student()
student.first_name = "John"
student.last_name = "Doe"
student.age = 23

filename = "student.json"
student.save_to_file(filename)

loaded_student = Student.load_from_file(filename)
print(loaded_student.__dict__)
```

### Task 25: Pascal's Triangle (12-pascal_triangle.py)

```python
#!/usr/bin/python3
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

triangle = pascal_triangle(5)
for row in triangle:
    print(row)
```

### Task 27: Insert at specific places (100-append_after.py)

```python
#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

filename = "append_after.txt"
string = "new"
word = "Python"
append_after(filename, word, string)
```

### Task 29: Log parsing (101-stats.py)

```python
#!/usr/bin/python3
log_parser = __import__('101-stats').log_parser

log_parser()
```
