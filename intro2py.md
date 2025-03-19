## Intro to Python Programming 

#### What is Python? Why Should You Learn It?
Python is a high-level programming language that’s easy to read and write. Created by Guido van Rossum in 1989, Python has become one of the most popular programming languages today!

#### Why Python?
1. Easy to learn (syntax is simple and readable).
2. Versatile (used for web development, data analysis, AI, game development, and more!).
3. Large community support (you’ll never be stuck alone!).

#### Getting Started: 
1. Install Python
2. Download Python from python.org.
3. Install it on your computer.
4. Open the Python IDLE or use a code editor like VS Code, PyCharm, or Jupyter Notebook.

Your First Program: 
“Hello World”!

`print("Hello World!")`

Run this program, and you’ll see “Hello World!” printed on your screen. Congrats, you’re now a Python programmer!

#### Variables and Data Types
Variables are like containers that hold values in Python. 
You can store numbers, text, lists, or even other objects in variables. Let’s explore some basic data types:

 
##### 1. Integers
Whole numbers (e.g., 5, -3).

```
age = 20
print(age)  # Output: 20
```

##### 2. Floats
Decimal numbers (e.g., 3.14, 2.5).

```
pi = 3.14`
print(pi)  # Output: 3.14
```

##### 3. Strings
Text enclosed in quotes (e.g., "Hello", 'World').

```
name = "Alice"
print(name)  # Output: Alice
```

##### 4. Booleans
Logical values (True or False).

```
is_python_fun = True
print(is_python_fun)  # Output: True
```

##### Tips & Tricks:
- Variable names should be descriptive (e.g., my_age, not just a).
- Avoid using reserved keywords like if, else, or while as variable names.


#### Operators and Expressions
Operators are symbols that perform operations on values or variables. Let’s explore some common ones!

##### Arithmetic Operators

```
# Addition
print(5 + 3)  # Output: 8

# Subtraction
print(10 - 2)  # Output: 8

# Multiplication
print(4 * 2)  # Output: 8

# Division
print(16 / 2)  # Output: 8.0

# Modulus (remainder)
print(7 % 3)  # Output: 1
```

Comparison Operators
```
a = 5
b = 3

print(a > b)   # True
print(a < b)   # False
print(a == b)  # False
print(a != b)  # True
```
Logical Operators
Combine conditions (like and, or, not).
```
x = 5
y = 3

print(x > y and x != y)  # True
print(x < y or x == y)   # False
print(not (x == y))       # True
```

Let’s Code: Simple Calculator!
```
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

#### Control Flow (if-elif-else)
Control flow determines the order in which your code runs. The most common structure is if, elif, and else.

```
if condition:
    # code block if condition is true
elif another_condition:
    # code block if previous conditions are false, but this one is true
else:
    # code block if all conditions are false
```
Example:
```
age = int(input("Enter your age: "))

if age < 18:
    print("You're a minor!")
elif age >= 18 and age <= 65:
    print("You're an adult!")
else:
    print("You're a senior citizen!")
```

##### Tips & Tricks:
- Indentation matters in Python! Use 4 spaces or a tab for each level of indentation.
- Simplify complex conditions using logical operators (and, or).

  
