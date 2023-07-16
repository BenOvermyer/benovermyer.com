+++
title = "Bash"
description = "Notes on writing Bash"
+++

[Official Documentation for Bash](https://www.gnu.org/software/bash/manual/)

## Loops

For loops:

```bash
# Syntax for iterating over a range of numbers:
for ((i = 0; i < 5; i++)); do
    # Code block executed for each iteration
done

# Syntax for iterating over elements in an array:
array=("apple" "banana" "cherry")
for item in "${array[@]}"; do
    # Code block executed for each element
done
```

While loops:

```bash
# Syntax for a while loop:
counter=0
while [ $counter -lt 5 ]; do
    # Code block executed as long as the condition is true
    ((counter++))
done
```

## Variable Assignment

```bash
# Syntax for variable assignment:
variableName=value
```

## Functions

```bash
# Syntax for defining a function:
functionName() {
    # Code block defining the function's behavior
    # $1, $2, etc. represent function arguments
    return $result
}
```

## String Interpolation

```bash
# Syntax for string interpolation:
variable="world"
message="Hello, $variable!"
echo "$message"  # Output: Hello, world!
```

## Multiline Strings

Using escape characters:

```bash
# Syntax for multiline strings using escape characters:
multilineString="This is a multiline string. \
It can span multiple lines."
```

Using heredoc:

```bash
# Syntax for multiline strings using a here document:
cat <<EOL
This is a multiline string.
It can span multiple lines.
EOL
```

## File I/O

```bash
# Reading from a file:
filename="filename.txt"
content=$(<"$filename")

# Writing to a file:
outputFilename="output.txt"
data="Hello, world!"
echo "$data" > "$outputFilename"
```

## HTTP Requests

```bash
# Syntax for making an HTTP GET request with curl:
url="https://api.example.com/data"
response=$(curl -s "$url")
# Process the response data
```

## Faking Arrays in Bash

```bash
# Creating an array-like list using a space-separated string:
myArray="1 2 3 4 5"

# Accessing elements:
echo "${myArray[0]}"  # Output: 1

# Slicing (requires splitting the string):
slicedArray=($myArray)
echo "${slicedArray[@]:1:3}"  # Output: 2 3 4

# Modifying elements (requires updating the string):
myArray="1 2 10 4 5"
echo "$myArray"  # Output: 1 2 10 4 5

# Appending elements (requires concatenating the string):
myArray+=" 6"
echo "$myArray"  # Output: 1 2 10 4 5 6
```

## Dictionaries

```bash
# Creating an associative array using space-separated key-value pairs:
myAssocArray="name=John age=30 city=New York"

# Accessing elements (requires parsing the key-value pairs):
for item in $myAssocArray; do
    key="${item%=*}"
    value="${item#*=}"
    if [[ "$key" == "name" ]]; then
        echo "$value"  # Output: John
    fi
done

# Modifying elements (requires updating the key-value pairs):
myAssocArray="name=John age=35 city=New York"
echo "$myAssocArray"  # Output: name=John age=35 city=New York

# Adding new key-value pairs (requires appending to the string):
myAssocArray+=" occupation=Engineer"
echo "$myAssocArray"  # Output: name=John age=35 city=New York occupation=Engineer
```
