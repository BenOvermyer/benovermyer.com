+++
title = "Python"
description = "Notes on the Python programming language"
+++

[Official Documentation for Python](https://docs.python.org/3/)

## Loops

A for loop:

```python
# Syntax for iterating over elements in a collection (e.g., list, tuple, string):
for item in collection:
    # Code block executed for each item

# Syntax for iterating over a range of numbers:
for i in range(start, stop, step):
    # Code block executed for each value in the range
```

A while loop:

```python
# Syntax for a while loop:
while condition:
    # Code block executed as long as the condition is true
```

## Variable assignment

```python
# Syntax for variable assignment:
variable_name = value
```

## Functions

```python
# Syntax for defining a function:
def function_name(parameter1, parameter2, ...):
    # Code block defining the function's behavior
    return result
```

## String interpolation

```python
# Syntax for f-string interpolation:
variable = 'world'
message = f'Hello, {variable}!'
print(message)  # Output: Hello, world!
```

## Multiline strings

```python
# Syntax for multiline strings:
multiline_string = '''
This is a multiline string.
It can span multiple lines.
'''
```

## File I/O

```python
# Syntax for reading from a file:
with open('filename.txt', 'r') as file:
    content = file.read()

# Syntax for writing to a file:
with open('output.txt', 'w') as file:
    file.write('Hello, world!')
```

## HTTP requests

```python
# Syntax for making an HTTP GET request:
import requests

response = requests.get('https://api.example.com/data')
data = response.json()  # Assuming the response contains JSON data
```

## Arrays (Lists)

```python
# Creating a list:
my_list = [1, 2, 3, 4, 5]

# Accessing elements:
print(my_list[0])  # Output: 1

# Slicing:
print(my_list[1:4])  # Output: [2, 3, 4]

# Modifying elements:
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Appending elements:
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]
```

## Dictionaries (Maps)

```python
# Creating a dictionary:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements:
print(my_dict['name'])  # Output: John

# Modifying elements:
my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Adding new key-value pairs:
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'occupation': 'Engineer'}
```
