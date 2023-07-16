+++
title = "Ruby"
description = "Notes on writing Ruby"
+++

[Official Documentation for Ruby](https://www.ruby-lang.org/en/documentation/)

## Loops

For loops:

```ruby
# Syntax for iterating over elements in an array:
for item in array do
    # Code block executed for each element
end

# You can also use the each method (preferred way in Ruby):
array.each do |item|
    # Code block executed for each element
end
```

While loops:

```ruby
# Syntax for a while loop:
while condition do
    # Code block executed as long as the condition is true
end
```

## Variable Assignment

```ruby
# Syntax for variable assignment:
variable_name = value
```

## Functions

```ruby
# Syntax for defining a method:
def method_name(parameter1, parameter2)
    # Code block defining the method's behavior
    return result
end
```

## String Interpolation

```ruby
# Syntax for string interpolation:
variable = 'world'
message = "Hello, #{variable}!"
puts message  # Output: Hello, world!
```

## Multiline Strings

```ruby
# Syntax for multiline strings:
multiline_string = <<~EOL
    This is a multiline string.
    It can span multiple lines.
EOL
```

## File I/O

```ruby
# Reading from a file:
File.open('filename.txt', 'r') do |file|
    content = file.read
    # Process the content
end

# Writing to a file:
File.open('output.txt', 'w') do |file|
    file.write('Hello, world!')
end
```

## HTTP Requests

```ruby
require 'net/http'

url = URI.parse('https://api.example.com/data')
http = Net::HTTP.new(url.host, url.port)

response = http.get(url)
data = response.body
# Process the data
```

Or, with HTTParty:

```ruby
require 'httparty'

response = HTTParty.get('https://api.example.com/data')
data = response.body
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

## Hashes (Dictionaries)

```ruby
# Creating a hash:
my_hash = { 'name' => 'John', 'age' => 30, 'city' => 'New York' }

# Accessing elements:
puts my_hash['name']  # Output: John

# Modifying elements:
my_hash['age'] = 35
puts my_hash  # Output: { 'name' => 'John', 'age' => 35, 'city' => 'New York' }

# Adding new key-value pairs:
my_hash['occupation'] = 'Engineer'
puts my_hash  # Output: { 'name' => 'John', 'age' => 35, 'city' => 'New York', 'occupation' => 'Engineer' }
```
