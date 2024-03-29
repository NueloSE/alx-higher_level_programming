# 0x03. Python - Data Structures: Lists, Tuples

## Resources
**Read or watch**
- [3.1.3. Lists](https://intranet.alxswe.com/rltoken/VarQbHxfmbnpGnaGp3Nb_A)
- [Data structures](https://intranet.alxswe.com/rltoken/2aa8Mp-V2eSieGeX3OX8yQ)(until 5.3. Tuples and Sequences included)
- [Learn to Program 6 :Lists](https://intranet.alxswe.com/rltoken/BX2_CuHj1sq4eYGiXbCYSg)

## General Objectives
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

## Task

### 0. Print a list of integers
Write a function that prints all integers of a list.
- Prototype: def print_list_integer(my_list=[]):
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```

### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in c.
- Prototype: def element_at(my_list, idx):
- If idx is negative, the function should return None
- If idx is out of range (> of number of element in my_list), the function should return None
- You are not allowed to import any module
- You are not allowed to use try/except

### 2. Replace element

write a function that replaces an element of a list at a specific position(like in c).
- Prototype: def replace_in_list(my_list, idx, element):
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except
```
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```

## 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
- Prototype: def print_reversed_list_integer(my_list=[]):
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```

## 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

- Prototype: def new_in_list(my_list, idx, element):
- If idx is negative, the function should return a copy of the original list
- If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
- You are not allowed to import any module
- You are not allowed to use try/except
```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

## 5. Can you C me now?
Write a function that removes all characters c and C from a string.

- Prototype: def no_c(my_string):
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use str.replace()

## 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

- Prototype: def print_matrix_integer(matrix=[[]]):
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers
```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
## 7. Tuples addition

Write a function that adds 2 tuples.
- Prototype: def add_tuple(tuple_a=(), tuple_b=()):
- Returns a tuple with 2 integers:
    - The first element should be the addition of the first element of each argument
    - The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```