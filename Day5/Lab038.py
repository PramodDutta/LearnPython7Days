# Set
# A set is an unordered collection of unique items.
# Sets are mutable but do not allow duplicate elements.

fruits = {"apple", "banana", "cherry"}
fruits.add("date")
fruits.add("apple")
print(fruits)

fruits.remove("banana")
print(fruits)

print("apple" in fruits)


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)