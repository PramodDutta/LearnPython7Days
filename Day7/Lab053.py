# Exceptions
# Exceptions are errors detected during execution.
# Python provides various ways to handle exceptions.

try:
    result = 10/0
except ZeroDivisionError as e:
    print(e)
    
try:
    result = 10/0
except ZeroDivisionError as e:
    print(e)
finally:
    print("Always executed!")