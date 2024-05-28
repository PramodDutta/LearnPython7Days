# Arguments

# Functions can accept information through arguments.

def greet(name):
    print("Hello ",name)
    
greet("Pramod")
greet("Amit")
greet("Lucky")

def greet_full_name(firstname,lastname):
    print("Your Full name is ,",firstname,lastname)
    
greet_full_name("pramod","dutta")


#Arbitrary Arguments, *args
print("amit","pramod","lucky")


def show_children(*children):
    print("Your children",children[0])
    print("Your children",children[1])
    print("Your children",children[2])
    #print("Your children",children[3])
    
show_children("Sumit","Duta","KUKO")


# Keyword Arguments


print(" ------ Keyword Arguments -------")


def display_children(child1, child2, child3):
    print("The youngest child is " + child3)
    
    
display_children(child1="John", child2="Jane", child3="Alice")




# Arbitrary Keyword Arguments, **kwargs



def show_details(**details):
    print("His first name is " + details["first_name"])
    print("His last name is " + details["last_name"])


show_details(first_name="John", last_name="Doe")


# Default Parameter Value


def my_function(country = "Norway"):
    print("I am from " + country)
    
    
my_function("Sweden")
my_function("India")
my_function()
my_function()

# Return

def sum_two_number(a,b):
    return a+b

result = sum_two_number(4,5)
print(result)