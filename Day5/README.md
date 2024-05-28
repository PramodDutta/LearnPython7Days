
### Strings and Functions

- Functions in Python are reusable code blocks designed to perform specific tasks.
- A function executes only when it is invoked.
- You can pass data, known as parameters, into a function.
- A function can return data as a result.

```python
def greet():
    print("Hello from a function")
```

```python
greet()
```

#### Arguments
- Functions can accept information through arguments.
- Arguments are specified after the function name, inside the parentheses.
- The terms parameter and argument can be used interchangeably.
- Arbitrary Arguments, *args
- Keyword Arguments
- Arbitrary Keyword Arguments, **kwargs

```python
def print_name(first_name):
    print(first_name + " Doe")

print_name("John")
print_name("Jane")
print_name("Alice")
```

```python
def show_children(*children):
    print("The youngest child is " + children[2])

show_children("John", "Jane", "Alice")
```

```python
def display_children(child1, child2, child3):
    print("The youngest child is " + child3)

display_children(child1="John", child2="Jane", child3="Alice")
```

```python
def show_details(**details):
    print("His last name is " + details["last_name"])

show_details(first_name="John", last_name="Doe")
```

- Default Parameter Value
``def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")``

- Return 
def my_function(x):
  return 5 * x

print(my_function(3))

-- 

#### Recursion

- Recursion is a common mathematical and programming concept. 
- It means that a function calls itself. 

