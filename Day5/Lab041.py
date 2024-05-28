# Recursion

# Recursion is a method of solving problems where the function calls itself.
# Each recursive call should move closer to a base case that stops the recursion.


def rec_count(number):
    print(number)
    if (number == 0):
        return 0
    else:
        rec_count(number - 1)


rec_count(5)

# 5*4*3*2*1
def factorial(n):
    if n==1:
        return 1;
    else:
        return n*factorial(n-1)

print(factorial(5))


