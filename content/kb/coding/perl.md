+++
title = "Perl"
description = "Notes on writing Perl"
+++

[Official Documentation for Perl](https://perldoc.perl.org/)

## Loops

For loops:

```perl
# Syntax for iterating over a range of numbers:
for (my $i = 0; $i < 5; $i++) {
    # Code block executed for each iteration
}

# Syntax for iterating over elements in an array or list:
my @array = (1, 2, 3, 4, 5);
foreach my $item (@array) {
    # Code block executed for each element
}
```

While loops:

```perl
# Syntax for a while loop:
while ($condition) {
    # Code block executed as long as the condition is true
}
```

## Variable Assignment

```perl
# Syntax for variable assignment:
my $variableName = $value;
```

## Functions

```perl
# Syntax for defining a subroutine:
sub subroutineName {
    # Code block defining the subroutine's behavior
    return $result;
}
```

## String Interpolation

```perl
# Syntax for string interpolation:
my $variable = 'world';
my $message = "Hello, $variable!";
print $message;  # Output: Hello, world!
```

## Multiline Strings

Heredoc:

```perl
# Syntax for heredoc multiline strings:
my $multilineString = <<EOL;
This is a multiline string.
It can span multiple lines.
EOL
```

Simple concatenation:

```perl
# Using simple concatenation for multiline strings:
my $multilineString = "This is a multiline string. " .
                      "It can span multiple lines.";
```

## File I/O

```perl
# Reading from a file:
my $filename = 'filename.txt';
open(my $file, '<', $filename) or die "Could not open file: $!";
my $content = do { local $/; <$file> };
close($file);

# Writing to a file:
my $outputFilename = 'output.txt';
my $data = 'Hello, world!';
open(my $outputFile, '>', $outputFilename) or die "Could not open file: $!";
print $outputFile $data;
close($outputFile);
```

## HTTP Requests

```perl
use LWP::UserAgent;

my $url = 'https://api.example.com/data';
my $ua = LWP::UserAgent->new;
my $response = $ua->get($url);

if ($response->is_success) {
    my $data = $response->decoded_content;
    # Process the data
} else {
    die "Error while making the request: " . $response->status_line;
}
```

## Arrays

```perl
# Creating an array:
my @myArray = (1, 2, 3, 4, 5);

# Accessing elements:
print $myArray[0];  # Output: 1

# Slicing:
print @myArray[1..3];  # Output: 234

# Modifying elements:
$myArray[2] = 10;
print @myArray;  # Output: 121045

# Appending elements:
push @myArray, 6;
print @myArray;  # Output: 1210456
```

## Hashes (Dictionaries)

```perl
# Creating a hash:
my %myHash = (
    'name' => 'John',
    'age' => 30,
    'city' => 'New York',
);

# Accessing elements:
print $myHash{'name'};  # Output: John

# Modifying elements:
$myHash{'age'} = 35;
print %myHash;  # Output: nameJohnage35cityNew York

# Adding new key-value pairs:
$myHash{'occupation'} = 'Engineer';
print %myHash;  # Output: nameJohnage35cityNew YorkoccupationEngineer
```
