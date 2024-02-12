# JavaScript Warm-up

This project covers fundamental concepts of JavaScript programming. You will explore scripting and web front-end development using JavaScript.

## Background Context

JavaScript is a versatile language used for both client-side and server-side development. In this project, you'll focus on scripting tasks to grasp essential concepts before applying them to web development projects.

## Learning Objectives

By completing this project, you will be able to:

- Understand the fundamentals of JavaScript programming.
- Run JavaScript scripts.
- Create and manipulate variables and constants.
- Differentiate between `var`, `const`, and `let`.
- Work with various data types in JavaScript.
- Utilize control flow statements such as `if`, `if...else`, `while`, and `for`.
- Define and use functions effectively.
- Learn about variable scope.
- Perform arithmetic operations and manipulate dictionaries.
- Import files in JavaScript.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- Files must end with a new line
- The first line of all files must be `#!/usr/bin/node`
- Mandatory README.md file at the root of the project folder
- Code should be semistandard compliant (version 16.x.x) with semicolons on top
- All files must be executable

## Installation

To install Node.js 14, run the following commands:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

To install semistandard, run:

```bash
$ sudo npm install semistandard --global
```

## Tasks

- Each task in the project folder `0x12-javascript-warm_up` contains a JavaScript file with a specific task number.
- Follow the instructions in each task to complete the required functionality.
- Detailed descriptions and examples are provided within each task.

## Getting Started

Clone the project repository from GitHub:

```bash
$ git clone <repository-url>
```

Navigate to the `0x12-javascript-warm_up` directory to find all task files.

## Task 0: First constant, first print

### Description
This script prints "JavaScript is amazing" to the console.

- It defines a constant variable called `myVar` with the value "JavaScript is amazing".
- Utilizes `console.log(...)` to print the output.
- Does not use `var`.

### Usage
```
$ ./0-javascript_is_amazing.js 
```

### File Location
[0-javascript_is_amazing.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/0-javascript_is_amazing.js)

---

## Task 1: 3 languages

### Description
This script prints three lines to the console:
1. "C is fun"
2. "Python is cool"
3. "JavaScript is amazing"

- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./1-multi_languages.js 
```

### File Location
[1-multi_languages.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/1-multi_languages.js)

---

## Task 2: Arguments

### Description
This script prints a message depending on the number of arguments passed:
- If no arguments are passed, it prints "No argument".
- If only one argument is passed, it prints "Argument found".
- Otherwise, it prints "Arguments found".

- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./2-arguments.js 
```

### File Location
[2-arguments.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/2-arguments.js)

---

## Task 3: Value of my argument

### Description
This script prints the first argument passed to it, or "No argument" if no arguments are passed.

- Uses `console.log(...)` to print all output.
- Does not use `var`.
- Does not use `length`.

### Usage
```
$ ./3-value_argument.js 
```

### File Location
[3-value_argument.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/3-value_argument.js)

---

## Task 4: Create a sentence

### Description
This script prints two arguments passed to it in the format: `<arg1> is <arg2>`.

- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./4-concat.js c cool
```

### File Location
[4-concat.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/4-concat.js)

---

## Task 5: An Integer

### Description
This script prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer, otherwise it prints "Not a number".

- Uses `console.log(...)` to print all output.
- Does not use `var`.
- Does not use `try/catch`.

### Usage
```
$ ./5-to_integer.js 
```

### File Location
[5-to_integer.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/5-to_integer.js)

---

## Task 6: Loop to languages

### Description
This script prints three lines using an array of strings and a loop:
1. "C is fun"
2. "Python is cool"
3. "JavaScript is amazing"

- Uses `console.log(...)` to print all output.
- Does not use `var`.
- Does not use any if/else statement.
- Uses only one `console.log`.
- Uses a loop (while, for, etc.).

### Usage
```
$ ./6-multi_languages_loop.js 
```

### File Location
[6-multi_languages_loop.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/6-multi_languages_loop.js)

---

## Task 7: I love C

### Description
This script prints "C is fun" x times, where x is the first argument of the script.

- If the first argument can't be converted to an integer, it prints "Missing number of occurrences".
- Uses `console.log(...)` to print all output.
- Uses only two `console.log`.
- Uses a loop (while, for, etc.).

### Usage
```
$ ./7-multi_c.js 2
```

### File Location
[7-multi_c.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/7-multi_c.js)

---

## Task 8: Square

### Description
This script prints a square of X's with a size determined by the first argument.

- If the first argument can't be converted to an integer, it prints "Missing size".
- Uses the character X to print the square.
- Uses `console.log(...)` to print all output.
- Uses a loop (while, for, etc.).

### Usage
```
$ ./8-square.js
```

### File Location
[8-square.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/8-square.js)

---

## Task 9: Add

### Description
This script prints the addition of two integers provided as arguments.

- Uses a function `add(a, b)` to perform the addition.
- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./9-add.js 
```

### File Location
[9-add.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/9-add.js)

---

## Task 10: Factorial

### Description
This script computes and prints the factorial of the integer provided as an argument.

- If no argument is provided, it computes the factorial of 1.
- Uses recursion to compute the factorial.
- Uses a function.
- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./10-factorial.js 
```

### File Location
[10-factorial.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/10-factorial.js)

---

## Task 11: Second biggest!

### Description
This script searches for the second biggest integer in the list of arguments.

- If no arguments are passed, it prints 0.
- If only one argument is passed, it prints 0.
- Uses `console.log(...)` to print all output.
- Does not use `var`.

### Usage
```
$ ./11-second_biggest.js 
```

### File Location
[11-second_biggest.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/11-second_biggest.js)

---

## Task 12: Object

### Description
This script replaces the value 12 with 89 in the `myObject` variable.

### File Location
[12-object.js](https://

github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/12-object.js)

---

## Task 13: Add file

### Description
This script defines a function `add` that returns the addition of two integers.

- The function must be visible from outside.
- The name of the function is `add`.

### File Location
[13-add.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/13-add.js)

---

## Task 14: Const or not const

### Description
This script modifies the value of `myVar` to 333.

### File Location
[100-let_me_const.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/100-let_me_const.js)

---

## Task 15: Call me Moby

### Description
This script executes a function `x` times.

- The function must be visible from outside.
- Prototype: `function (x, theFunction)`.

### File Location
[101-call_me_moby.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/101-call_me_moby.js)

---

## Task 16: Add me maybe

### Description
This script increments and calls a function.

- The function must be visible from outside.
- Prototype: `function (number, theFunction)`.

### File Location
[102-add_me_maybe.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/102-add_me_maybe.js)

---

## Task 17: Increment object

### Description
This script adds a new function `incr` that increments the integer value in `myObject`.

### File Location
[103-object_fct.js](https://github.com/alx-higher_level_programming/0x12-javascript-warm_up/blob/main/103-object_fct.js)

