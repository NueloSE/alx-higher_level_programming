<<<<<<< HEAD
# ALX HIGHER LEVEL PROGRAMMING AND ALGORITHMS

![python photo](https://camo.githubusercontent.com/3939859066f892b0de3ca1282db48e2215f008daee504d63327216ad5aa0ad72/68747470733a2f2f7777772e706e67616c6c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f352f507974686f6e2d504e472d506963747572652e706e67)

#### This repository contains programs created with the intention of understanding Higher level programming and algorithms using PYTHON PROGRAMMING LANGUAGE to solve common programming task during my SOFTWARE ENGINEERING studies @ ALX_SE cohort 21

## Technologies
- Files are compiled using Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files are written according to the pycodestyle (version 2.8.*)
- Scripts are written in #!/usr/bin/python3
	- The first line of all your python scripts files should be exactly #!/usr/bin/python3
	- The first line of all your shell scripts files should be exactly #!/bin/bash
	- All scripts are executable

## Description

This repository encompasses code written for higher-level programming languages during the ALX Software Engineering course in collaboration with Holberton School of Computer Science. Through these projects, I have gained proficiency in the Python programming language, applying the acquired skills to address various tasks, all meticulously documented within this repository. Concurrently, I have furthered my expertise in the C programming language and shell scripting, concurrently advancing my comprehension of Data Structures and Algorithms. This repository can serve as a valuable learning resource for aspiring software engineers.

## Prerequisite

This is a continuation of [alx_low_level_programming by Nuelo](https://github.com/NueloSE/alx-low_level_programming)
=======
# 0x00. Python - Hello, World

![Monty python](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg)

## Resources

**Read or watch:**
- [The Python tutorial](https://intranet.alxswe.com/rltoken/JsFCs_NBzMAR7-XPAZ9BoA) (only the first three chapters below)
- [Whetting Your Appetite](https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg)
- [Using the Python Interpreter](https://intranet.alxswe.com/rltoken/RVpfAuagCo9SdfYeoHd6jg)
- [An Informal Introduction to Python](https://intranet.alxswe.com/rltoken/bVps0ZPWq7qVZ7vc-eJGTw)(Read up until “3.1.2. Strings” included)
- [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
- [Learn to Program](https://intranet.alxswe.com/rltoken/szBsJ-Qyig_RrImN7RGlOg)
- [Pycodestyle – Style Guide for Python Code](https://intranet.alxswe.com/rltoken/tgYt-0zVy1T4sDlE9ohxnA)

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Shell Scripts
- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable


## Task 0
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```

## Task 1
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```
## Task 2
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
## Task 3

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code here
- The output of the script should be:
	- the number, followed by Battery street,
	- followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips

## Task 4

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code here
- The output of the program should be:
	- Float:, followed by the float with only 2 digits
	- followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

## Task 5

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code here
- The output of the program should be:
	- 3 times the value of str
	- followed by a new line
	- followed by the 9 first characters of str
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```

## Task 6
Complete this source code to print Welcome to Holberton School!

- You can find the source code here
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
```

## Task 7. Copy - Cut - Paste

Complete this source code

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

## Task 8. Create a new sentence
Complete this source code to print object-oriented programming with Python, followed by a new line.

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

## Task 9
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

