# Python Object Oriented Programming
## 4 Pillars of OOP
### Methods/functions
#### Modules
##### Libraries- Packages

# Packages/Modules:
# Lucky draw
- key word called import allows you to import from the libraries available within the operator
- . allows you to access methods
```python
import random

print(random.random()) 
# each time it is run it generates a random number
```
# Or you can use this way below-
```python
from random import * # allows you to import all functions
print(random()) # prints the random function
```
# importing using math
```python
import math
number = 23.66
# any numbers - to round the figure up-
# number .50 above round up 2
# number 1.49 or less round down to 1
print(math.ceil(number)) # ceil will round the figure up
print(math.floor(number)) # floor will help you round the figure to bottom
```

# Defining a Function

```python
def greeting():
    # greet the user
    print("Hello Dear ")

    #pass
    # keyword called pass
# unless the function is called it does nothing
greeting()
```

```python
def greet_user(name):
    print("Hello Dear " + name) # adding 2 strings with user input()
    #pass
greet_user("Sparta")

```

# Creating a Function using Int
```python
def add(value1, value2): # take user input as int then add them together, display the outcome
    print(value1 + value2)

add(2, 2)
```

