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
print(not (x == y))      # True
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


#### Loops (while and for)
Loops allow you to repeat code multiple times without rewriting it. There are two types: while loops and for loops.

##### While Loop
Runs as long as a condition is true.

```
count = 0

while count < 5:
    print(count)
    count += 1
```
##### For Loop
Iterates over a sequence (like a list, tuple, or string).

```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
Let’s Code: Sum of Numbers!

```
sum = 0

for i in range(1, 6):
    sum += i

print("Sum =", sum)  # Output: Sum = 15
```

#### Functions and Libraries
Functions are reusable blocks of code that perform a specific task. Libraries are collections of functions that extend Python’s capabilities.

##### Defining a Function:
```
def greet(name):
    print("Hello", name, "!")

greet("Alice")  # Output: Hello Alice!
```

##### Built-in Functions:
Python has many built-in functions like len(), type(), and input().

```
text = "Hello World!"
print(len(text))  # Output: 12
```

##### Importing Libraries:
Libraries like math, random, or pandas add new functionality to Python.

```
import math

radius = 5
area = math.pi * radius ** 2
print(area)  # Output: ~78.54
```

Check these programs from the repo
Program to generate random numbers using random library
 
![randomnum.py](https://github.com/santakd/py-starter/blob/main/randomnum.py)

Remember the Magic 8 ball, here is a fun program implementing that

![Magic 8 Ball](https://github.com/santakd/py-starter/blob/main/magic8ball.py)

##### Tips & Tricks:
- Use functions to avoid repeating code.
- Libraries save time by providing ready-made solutions for common problems.


#### Final Words
You’ve covered the basics of Python programming! Keep practicing, and soon you’ll be creating cool projects like games, websites, or even AI models. 

Remember:

- Practice regularly (even 15 minutes a day makes a difference!).
- Experiment with code (don’t be afraid to make mistakes).
- Join coding communities for support and inspiration (e.g., Reddit’s r/learnpython or Stack Overflow).
- Enjoy and share your learning.
  
Happy coding! 🚀
