+++
title = "Go"
description = "Notes on the Go programming language"
+++

[Official Documentation for Go](https://golang.org/doc/)

## Loops

```go
// Syntax for a basic for loop:
for i := 0; i < 5; i++ {
    // Code block executed for each iteration
}

// Syntax for a for loop used like a while loop:
counter := 0
for counter < 5 {
    // Code block executed as long as the condition is true
    counter++
}
```

## Variable Assignment

```go
// Syntax for variable assignment (explicit declaration):
var variableName dataType
variableName = value

// Syntax for variable assignment (short variable declaration):
variableName := value
```

## Functions

```go
// Syntax for defining a function:
func functionName(parameter1 dataType, parameter2 dataType) returnType {
    // Code block defining the function's behavior
    return result
}
```

## String Interpolation

```go
import "fmt"

func main() {
    variable := "world"
    message := fmt.Sprintf("Hello, %s!", variable)
    fmt.Println(message)  // Output: Hello, world!
}
```

## Multiline Strings

```go
multilineString := `
This is a multiline string.
It can span multiple lines.
`
```

## File I/O

```go
import (
    "io/ioutil"
    "os"
)

// Reading from a file:
content, err := ioutil.ReadFile("filename.txt")
if err != nil {
    // Handle error
}

// Writing to a file:
data := []byte("Hello, world!")
err := ioutil.WriteFile("output.txt", data, 0644)
if err != nil {
    // Handle error
}
```

## HTTP Requests

```go
import (
    "net/http"
    "io/ioutil"
)

func main() {
    url := "https://api.example.com/data"
    response, err := http.Get(url)
    if err != nil {
        // Handle error
    }
    defer response.Body.Close()

    data, err := ioutil.ReadAll(response.Body)
    if err != nil {
        // Handle error
    }
    // Process the data
}
```

## Arrays (Slices)

```go
// Creating a slice:
my_slice := []int{1, 2, 3, 4, 5}

// Accessing elements:
fmt.Println(my_slice[0])  // Output: 1

// Slicing:
fmt.Println(my_slice[1:4])  // Output: [2 3 4]

// Modifying elements:
my_slice[2] = 10
fmt.Println(my_slice)  // Output: [1 2 10 4 5]

// Appending elements:
my_slice = append(my_slice, 6)
fmt.Println(my_slice)  // Output: [1 2 10 4 5 6]
```

## Maps

```go
// Creating a map:
my_map := map[string]interface{}{
    "name": "John",
    "age": 30,
    "city": "New York",
}

// Accessing elements:
fmt.Println(my_map["name"])  // Output: John

// Modifying elements:
my_map["age"] = 35
fmt.Println(my_map)  // Output: map[name:John age:35 city:New York]

// Adding new key-value pairs:
my_map["occupation"] = "Engineer"
fmt.Println(my_map)  // Output: map[name:John age:35 city:New York occupation:Engineer]
```
