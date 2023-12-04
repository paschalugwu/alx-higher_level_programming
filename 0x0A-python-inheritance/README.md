# alx-higher_level_programming - 0x0A-python-inheritance

## 0. Lookup
Write a function that returns the list of available attributes and methods of an object.

### Prototype
```python
def lookup(obj):
    """
    Returns a list object
    """
    pass
```

## 1. My list
Write a class `MyList` that inherits from `list`. The class includes a public instance method `print_sorted()` that prints the list in ascending order.

### Usage
```python
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)
my_list.print_sorted()
print(my_list)
```

## 2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

### Prototype
```python
def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.
    """
    pass
```

### Usage
```python
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
```

## 3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

### Prototype
```python
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    pass
```

### Usage
```python
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
```

## 4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

### Prototype
```python
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
    otherwise False.
    """
    pass
```

### Usage
```python
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
```

## 5. Geometry module
Write an empty class `BaseGeometry`.

### Usage
```python
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
```

## 6. Improve Geometry
Write a class `BaseGeometry` (based on 5-base_geometry.py) with a public instance method `area()` that raises an Exception with the message "area() is not implemented."

### Usage
```python
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

## 7. Integer validator
Write a class `BaseGeometry` (based on 6-base_geometry.py) with a public instance method `integer_validator(self, name, value)` that validates the value.

### Usage
```python
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

## 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py) with instantiation using width and height.

### Usage
```python
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

## 9. Full rectangle
Write a class `Rectangle` that inherits from

 `BaseGeometry` (7-base_geometry.py) with instantiation using width and height, and implementation of the `area()` method.

### Usage
```python
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
```

## 10. Square #1
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py) with instantiation using size.

### Usage
```python
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())
```

## 11. Square #2
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py) with instantiation using size and a modified `__str__` method.

### Usage
```python
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
```

## 12. My integer
Write a class `MyInt` that inherits from `int` with inverted `==` and `!=` operators.

### Usage
```python
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
```

## 13. Can I?
Write a function `add_attribute` that adds a new attribute to an object if it’s possible.

### Usage
```python
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```
