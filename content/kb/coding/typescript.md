+++
title = "TypeScript"
description = "Notes on writing TypeScript"
+++

[Official Documentation for TypeScript](https://www.typescriptlang.org/docs/)

## Loops

For loop:

```typescript
// Syntax for iterating over elements in an array:
for (let i = 0; i < array.length; i++) {
  // Code block executed for each element
}

// Syntax for iterating over elements in an iterable object (e.g., array, string):
for (const item of iterable) {
  // Code block executed for each item
}
```

While loop:

```typescript
// Syntax for a while loop:
while (condition) {
  // Code block executed as long as the condition is true
}
```

## Variable Assignment

```typescript
// Syntax for variable assignment (explicit type):
let variableName: dataType = value;

// Syntax for variable assignment (type inference):
let variableName = value;
```

## Functions

```typescript
// Syntax for defining a function with parameters and return type:
function functionName(parameter1: dataType, parameter2: dataType): returnType {
  // Code block defining the function's behavior
  return result;
}

// Example:
function addNumbers(a: number, b: number): number {
  return a + b;
}
```

## String Interpolation

```typescript
const variable = "world";
const message = `Hello, ${variable}!`;
console.log(message); // Output: Hello, world!
```

## Multiline Strings

```typescript
const multilineString = `
This is a multiline string.
It can span multiple lines.
`;
```

## File I/O

```typescript
import fs from "fs";

// Reading from a file (asynchronous):
fs.readFile("filename.txt", "utf8", (err, data) => {
  if (err) {
    // Handle error
  } else {
    // Process the data
  }
});

// Writing to a file (asynchronous):
fs.writeFile("output.txt", "Hello, world!", "utf8", (err) => {
  if (err) {
    // Handle error
  } else {
    // File written successfully
  }
});
```

## HTTP Requests

```typescript
import axios from "axios";

async function fetchData() {
  const url = "https://api.example.com/data";
  try {
    const response = await axios.get(url);
    const data = response.data;
    // Process the data
  } catch (error) {
    // Handle error
  }
}
```

## Arrays

```typescript
// Creating an array:
const myArray: number[] = [1, 2, 3, 4, 5];

// Accessing elements:
console.log(myArray[0]); // Output: 1

// Slicing:
console.log(myArray.slice(1, 4)); // Output: [2, 3, 4]

// Modifying elements:
myArray[2] = 10;
console.log(myArray); // Output: [1, 2, 10, 4, 5]

// Appending elements:
myArray.push(6);
console.log(myArray); // Output: [1, 2, 10, 4, 5, 6]
```

## Objects

```typescript
// Creating an object:
const myObject: { [key: string]: any } = {
  name: "John",
  age: 30,
  city: "New York",
};

// Accessing elements:
console.log(myObject["name"]); // Output: John

// Modifying elements:
myObject["age"] = 35;
console.log(myObject); // Output: { name: 'John', age: 35, city: 'New York' }

// Adding new key-value pairs:
myObject["occupation"] = "Engineer";
console.log(myObject); // Output: { name: 'John', age: 35, city: 'New York', occupation: 'Engineer' }
```
