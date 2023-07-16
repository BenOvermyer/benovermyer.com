+++
title = "Crystal"
description = "Notes on writing Crystal"
+++

[Official Documentation for Crystal](https://crystal-lang.org/docs/)

## Loops

For loops:

```ruby
# Syntax for iterating over a range of numbers:
for i in 0..4
  # Code block executed for each iteration
end

# Syntax for iterating over elements in an array or range:
array = [1, 2, 3, 4, 5]
for item in array
  # Code block executed for each element
end
```

While loops:

```ruby
# Syntax for a while loop:
i = 0
while i < 5
  # Code block executed as long as the condition is true
  i += 1
end
```

## Variable Assignment

```ruby
# Syntax for variable assignment (explicit type):
variable_name: DataType = value

# Syntax for variable assignment (type inference):
variable_name = value
```

## Functions

```ruby
# Syntax for defining a function:
def function_name(parameter1 : DataType, parameter2 : DataType) : ReturnType
  # Code block defining the function's behavior
end
```

## String Interpolation

```ruby
# Syntax for string interpolation:
variable = "world"
message = "Hello, #{variable}!"
puts message  # Output: Hello, world!
```

## Multiline Strings

```ruby
# Syntax for multiline strings:
multiline_string = """
This is a multiline string.
It can span multiple lines.
"""
```

## File I/O

```ruby
# Reading from a file:
filename = "filename.txt"
content = File.read(filename)

# Writing to a file:
output_filename = "output.txt"
data = "Hello, world!"
File.write(output_filename, data)
```

## HTTP Requests

```ruby
require "http/client"

url = "https://api.example.com/data"
response = HTTP::Client.get(url)
data = response.body.to_s
# Process the data
```

## Arrays

```ruby
# Creating an array:
my_array = [1, 2, 3, 4, 5]

# Accessing elements:
puts my_array[0]  # Output: 1

# Slicing:
puts my_array[1..3]  # Output: [2, 3, 4]

# Modifying elements:
my_array[2] = 10
puts my_array  # Output: [1, 2, 10, 4, 5]

# Appending elements:
my_array << 6
puts my_array  # Output: [1, 2, 10, 4, 5, 6]
```

## Dictionaries (Hashes)

```ruby
# Creating a hash:
my_hash = {"name" => "John", "age" => 30, "city" => "New York"}

# Accessing elements:
puts my_hash["name"]  # Output: John

# Modifying elements:
my_hash["age"] = 35
puts my_hash  # Output: {"name" => "John", "age" => 35, "city" => "New York"}

# Adding new key-value pairs:
my_hash["occupation"] = "Engineer"
puts my_hash  # Output: {"name" => "John", "age" => 35, "city" => "New York", "occupation" => "Engineer"}
```
