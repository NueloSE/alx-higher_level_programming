# 0x06. Python - Classes and Objects

`Python` `OOP`

## Resources

**Read or watch**
- [Object Oriented Programming](https://intranet.alxswe.com/rltoken/i49z6HxrBGRNnixo7ZWbEQ)
- [Object-Oriented Programming](https://intranet.alxswe.com/rltoken/qz3KSn154ia4H2DPaabOzg)
- [Properties vs. Getters and Setters](https://intranet.alxswe.com/rltoken/Wy2djWXK5b4rnnYlAq_wlA)
- [Learn to Program 9: Object Oriented Programming](https://intranet.alxswe.com/rltoken/MxIOanLf5vG5QeCWek2nqQ)
- [Python Classes and Objects](https://intranet.alxswe.com/rltoken/AoLH4xp5StrQST-Cu0Fg8w)
- [Object Oriented Programming](https://intranet.alxswe.com/rltoken/-vVnWzwR3a3X0H8Oia78Ug)
- [Example Google Style Python Docstrings](https://intranet.alxswe.com/rltoken/dOO785g5EQYkRU2E1wri0g)

## General Objectives
- Why Python programming is awesome
- What is OOP
- "first-class everything"
- What is a class
- What is an object and instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation and information Hiding
- What is a property
- What is the difference between an attribute and a property in python
- What is Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for exisiting instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## TASKS
### 0. My first Square
Write an empty class Square that defines a square:
- You are not allowed to import any module

### 1.
Write a class Square that defines a square by: (based on 0-square.py)

- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module

### 2.
Write a class Square that defines a square by: (based on 1-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- You are not allowed to import any module

### 3.
Write a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module