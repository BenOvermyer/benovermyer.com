+++
title = "PHP"
description = "Notes on writing PHP"
+++

[Official Documentation for PHP](https://www.php.net/docs.php)

## Loops

For loops:

```php
// Syntax for iterating over a range of numbers:
for ($i = 0; $i < 5; $i++) {
    // Code block executed for each iteration
}

// Syntax for iterating over elements in an array or iterable:
for ($i = 0; $i < count($array); $i++) {
    $item = $array[$i];
    // Code block executed for each element
}
```

While loops:

```php
// Syntax for a while loop:
while ($condition) {
    // Code block executed as long as the condition is true
}
```

Foreach loops:

```php
// Syntax for iterating over elements in an array with foreach:
foreach ($array as $item) {
    // Code block executed for each element
}
```

## Variable Assignment

```php
// Syntax for variable assignment:
$variableName = $value;
```

## Functions

```php
// Syntax for defining a function:
function functionName($parameter1, $parameter2) {
    // Code block defining the function's behavior
    return $result;
}
```

## String Interpolation

```php
// Syntax for string interpolation:
$variable = 'world';
$message = "Hello, $variable!";
echo $message;  // Output: Hello, world!
```

## Multiline Strings

Heredoc:

```php
// Syntax for heredoc multiline strings:
$multilineString = <<<EOL
This is a multiline string.
It can span multiple lines.
EOL;
```

Nowdoc, which doesn't interpolate variables:

```php
// Syntax for nowdoc multiline strings:
$nowdocString = <<<'EOL'
This is a nowdoc multiline string.
Variables are not interpolated here: $variable
EOL;
```

## File I/O

```php
// Reading from a file:
$filename = 'filename.txt';
$content = file_get_contents($filename);

// Writing to a file:
$outputFilename = 'output.txt';
$data = 'Hello, world!';
file_put_contents($outputFilename, $data);
```

### HTTP Requests

```php
// Syntax for making an HTTP GET request:
$url = 'https://api.example.com/data';
$response = file_get_contents($url);
// Process the response data
```

## Arrays

```php
// Creating an array:
$myArray = [1, 2, 3, 4, 5];

// Accessing elements:
echo $myArray[0];  // Output: 1

// Slicing:
print_r(array_slice($myArray, 1, 3));  // Output: Array ( [0] => 2 [1] => 3 [2] => 4 )

// Modifying elements:
$myArray[2] = 10;
print_r($myArray);  // Output: Array ( [0] => 1 [1] => 2 [2] => 10 [3] => 4 [4] => 5 )

// Appending elements:
$myArray[] = 6;
print_r($myArray);  // Output: Array ( [0] => 1 [1] => 2 [2] => 10 [3] => 4 [4] => 5 [5] => 6 )
```

## Associative Arrays (Dictionaries)

```php
// Creating an associative array:
$myAssocArray = array(
    'name' => 'John',
    'age' => 30,
    'city' => 'New York',
);

// Accessing elements:
echo $myAssocArray['name'];  // Output: John

// Modifying elements:
$myAssocArray['age'] = 35;
print_r($myAssocArray);  // Output: Array ( [name] => John [age] => 35 [city] => New York )

// Adding new key-value pairs:
$myAssocArray['occupation'] = 'Engineer';
print_r($myAssocArray);  // Output: Array ( [name] => John [age] => 35 [city] => New York [occupation] => Engineer )
```
