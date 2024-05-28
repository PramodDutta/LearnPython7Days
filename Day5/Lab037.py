# List, Set, Tuple and Dictionary in Python

# A list is an ordered collection of items which can be of any type

fruits = ["apple", "banana", "cherry","apple"]
print(fruits[0])
print(fruits[1])  # Output: banana

# Example 2: Adding elements to a list
fruits.append("date")
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]

fruits.remove("banana")
print(fruits)

print(fruits[1:3]) # 1 to 2
print(fruits[0:2]) # 1 to 2

fruits.reverse()
print(fruits)

