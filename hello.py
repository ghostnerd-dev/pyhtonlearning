print ("Hello world\n")
greeting = "Welcome to the new repo!"
print (greeting)
for i in range(5):
    print (greeting)

import sys
print("Python version")
print (sys.version)

if(5 > 5):
      for i in range(3):
        print("5 is greater than 2")
print("Five is greater than two!")

#this is a commet, and should not be executed
#this is another comment
#this is yet another comment
#this is the last comment
#this is the final comment
#this is the ultimate comment
#this is the penultimate comment
#this is the antepenultimate comment
#this is the preantepenultimate comment
#this is the superlative comment
#this is the definitive comment
#this is the conclusive comment
#this is the terminal comment
#this is the closing comment
#this is the ending comment
#this is the finishing comment
#this is the concluding comment
#this is the wrap-up comment
#this is the finalizing comment
#this is the last but not least comment
#this is the ultimate final comment
#this is the absolute final comment
#this is the conclusive final comment
#this is the definitive final comment

print("Just a test line to check git functionality") #print("Another test line to check nextline functionality")

#this is to test sameline different print statements using "End" parameter
print("This is the first part of the line ", end="" )
print("and this is the second part of the same line.")
print("This is to test the end parameter again ", end="*** ")
print("See if it works this time.")
print("End of the test lines.")

print(23+32)
print("I am", 35, "years old.")
#this is to play with varaibles
x = 4       # x is of type int
x = "Sally" # x is now of type 
x=12 # x is of type int again
print(x)

#this is casting example

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#this is ot check type of above casted variables
print("the type of x is", type(x))
print("the type of y is", type(y))
print("the type of z is", type(z))

#variable names case sensitivity checkup
a = 4
A = "Sally" # A is a different variable than a
print(a)
print(A)
    #variable names are case sensitive in python
    ########################################
    #########################################
#this is valid variable naming section
myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"

#this is a invalid variable naming section
#2myvar="John"  #invalid variable name there is a number at the beginning
#my-var="John"  #invalid variable name there is a hyphen
#my var="John"  #invalid variable name there is a space
#print(my var)

#this is cases to write multi word variable names
#this is one case
MyVariableName="John" #pascal case -- Every word starts with a capital letter
#this is second case
my_variable_name="John" #snake case -- Every word is in lowercase and separated by underscores
#this is third case
myVariableName="John" #camel case -- first letter of first word is in lowercase and rest of the words start with a capital letter

#this is to check assignment of multiple variables in one line

Name, Residence, Age ="Ammaar", "Kashmir", 23
print(Name)
print(Residence)
print(Age)

####################################################################################
####################################################################################

#this is to check the assignment of same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

####################################################################################
####################################################################################

# the conecpt of unpacking a collection [Unpacking: extracting values from a collection like lists
# and tuples and assigning them to variables]
print("\nUnpacking a collection example:")
fruits = ["apple", "banana", "cherry"] #this is a list of fruits
x, y, z = fruits #unpacking the list into three variables and printing them below
print(x)
print(y)
print(z)

####################################################################################
####################################################################################

#In the print() function, you output multiple variables, separated by a comma:

print("\nMultiple variable print example:")
x="I"
y="Love"
z="Python"

print(x,y,z)

#"+" can also be used to join multiple variables together as given below

x="I"
y="Like"
z="Java"

print(x+" "+y+" "+z)    #here spaces are added between the variables to separate them in the output

## For Numbers , the + character works as a mathematical operator:
#example:

x = 5
y = 10
print(x + y)    #output will be 15

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
##example:
x = 5
y = "John"
#print(x + y)    #this will give an error

# The best way to output multiple variables in the print() function is to separate them with commas, 
# which even support different data types:
x = 5
y = "John"
print(x, y)    #this will not give an error

#Global Variables
print("\nGlobal variable example:")
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

#example 2:
print("\nGlobal variable example 2:")
x = "fantastic"
def myfunc():
  x = "great"
  print("Python is " + x)
myfunc()
print("Python is " + x)

################################################################################
################################################################################

#DataTypes in Pyhton:
#1. Text DataType is represented by str class
x = "Hello World"    #this is string datatype
print(type(x))

#2. Numeric DataTypes: int, float, complex
x = 20    #this is int datatype
print(type(x))
x = 20.5    #this is float datatype
print(type(x))
x = 1j    #this is complex datatype
print(type(x))  
print(x)

#3. Sequence DataTypes: list, tuple, range
x = ["apple", "banana", "cherry"]    #this is list datatype
print(type(x))
x = ("apple", "banana", "cherry")    #this is tuple datatype
print(type(x))
x = range(10,15)          #this is range datatype
print(type(x))
print(x)

X=10
a=x
print(a)

#TypeConversion

print("\nType conversion examples:")
x=10  #this is int
y=10.5  #this is float
z=3j   #this is complex

#after conversion
a=float(x)
b=int(y)
c=complex(x)
print(a)
print(b)
print(c)

#Note: You cannot convert complex numbers into another number type.
#Example
x = 3j
#print(int(x))  #this will give an error
#print(float(x))  #this will give an error

####################################################################
####################################################################

#Random Number Generation
import random
print("\nRandom number generation examples:")
print(random.randrange(1,10))  #this will generate a random number between 1 and 10
print(random.randint(1,10))    #this will generate a random integer between 1 and 10
print(random.random())         #this will generate a random float number between 0.0 and 1.0
print(random.uniform(1,10))    #this will generate a random float number between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  #this will randomly select an item from the given list
print(random.sample(range(1, 100), 5))  #this will generate a list of 5 unique random numbers between 1 and 100
print(random.shuffle(['apple', 'banana', 'cherry']))  #this will shuffle the given list randomly  
mylist = ['apple', 'banana', 'cherry']
random.shuffle(mylist)
print(mylist)  #this will print the shuffled list
print(random.seed(10))  #this will set the seed for random number generation
print(random.getrandbits(4))  #this will generate a random integer with 4 random bits
#print(random.getstate())  #this will return the current state of the random number generator
print(random.setstate(random.getstate()))  #this will set the state of the random number generator to the given state
print(random.randrange(6, 100, 5))  #this will generate a random number between 1 and 100 with a step of 5

####################################################################
####################################################################

#Python Casting
# 1. int() - converts a value to an integer
print("\nPython casting examples:")
print("\nInt casting examples:")
x=int(1)    #this will cast 1 to int
y=int(2.8)  #this will cast 2.8 to int
z=int("3")  #this will cast "3" to int
print(x)
print(y)
print(z)
# 2. float() - converts a value to a float
print("\nFloat casting examples:")
a=float(1)    #this will cast 1 to float
b=float(2.8)  #this will cast 2.8 to float
c=float("3")  #this will cast "3" to float
d=float("4.2")  #this will cast "4.2" to float
print(a)
print(b)
print(c)
print(d)

# 3. str() - converts a value to a string
print("\nString casting examples:")
e=str(1)    #this will cast 1 to string
f=str(2.8)  #this will cast 2.8 to string
g=str("3")  #this will cast "3" to string
print(e)
print(f)
print(g)
# print(type(e))
# print(type(f))

#NOTE: Int and Float casting can only be done on numeric values and strings that represent numeric values.
#Example:
#print(int("Hello"))  #this will give an error
#print(float("World"))  #this will give an error

####################################################################
####################################################################

#Python Strings
#most of the basics are already known
#Here we only talk about multiple line strings and some string methods

print("\nPython multi-line string example:\n")
multi_line_string = """This is a multi-line string.
You can write across multiple lines.
This is the third line."""
print(multi_line_string)
#or this way
multi_line_string2 = '''\nThis is another multi-line string. 
You can also use single quotes.
This is the third line.'''
print(multi_line_string2)
# Note: in the result, the line breaks are inserted at the same position as in the code.

#STRINGS IN PYTHON ARE ARRAYS

#example to access characters of string using indexing
#Square brackets can be used to access elements of the string.

print("\nString indexing example:\n")
a = "Hello, World!"
print(a[3])

#n number of string characters of a string varibale can be printed
#example
print(a[8:10])

#LOOPING THROUGH A STRING
#since strings are arrays, we can loop through the characters of a string, using a for loop.
print("\nLooping through a string example:\n")
for x in a:
    print(x)

    #STRING LENGTH
    #string length can be found using len() function
print("\nString length example:\n")
print("The length of the string a above is:", len(a))

for x in a :
   print(a, "has", len(a), "characters")
  #  print(a, "contains", a.count("l"), "'l' characters")
  #  print(x, "is present", a.count(x), "times in the string a")
  
  #CHECKING A STRING
  #To check if a certain phrase or character is present in a string, we can use the keyword "in".
print("\nChecking a string example:\n")
txt = "The best things in life are free!"
print("free" in txt)  #this will return True
print("expensive" in txt)  #this will return False

#To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in".
print("\nChecking a string not in example:\n")
print("expensive" not in txt)  #this will return True
print("free" not in txt)  #this will return False

#Sting Silicing
#You can return a range of characters by using the slice syntax.
print("\nString slicing example:\n")
b = "Hello, World!"
print(b[2:5])  #this will return characters from index 2 to 4(last index is excluded)
print(b[:5])   #this will return characters from the beginning to index 4(last index is excluded)
#First character has index 0 always
print(b[2:])   #this will return characters from index 2 to the end

#Negative Indexing
#Negative indexing means start from the end
print("\nNegative indexing example:\n")
c = "Hello, World!"
print(c[-5:-2])  #this will return characters from index -5 to -3(last index is excluded)
print(c[-5:])    #this will return characters from index -5 to the end
print(c[:-2])    #this will return characters from the beginning to index -3(last index is excluded)
#negative indexing starts from -1 for the last character

#STRING MODIFICATION METHODS
print("\nString modification methods examples:\n")
txt = "hello, welcome to the world of python programming."
print(txt.capitalize())  #this will capitalize the first character of the string
print(txt.upper())       #this will convert the string to uppercase
print(txt.lower())       #this will convert the string to lowercase
print(txt.swapcase())    #this will swap the case of the string
print(txt.title())       #this will convert the first character of each word to uppercase
print(txt.replace("python", "Java"))  #this will replace "python" with "Java" in the string
print(txt.strip())      #this will remove any leading and trailing whitespace characters
print(txt.split(" "))   #this will split the string into a list of words
print(txt.find("welcome"))  #this will return the index of the first occurrence of "welcome" in the string
print(txt.count("o"))   #this will return the number of occurrences of "o" in the string
print(txt.startswith("hello"))  #this will return True if the string starts with "hello"
print(txt.endswith("programming."))  #this will return True if the string ends with "programming."
print(txt.center(50))   #this will center the string in a field of given width
print(txt.encode())     #this will encode the string to bytes
print(txt.isalpha())    #this will return True if all characters in the string are alphabetic
print(txt.isdigit())    #this will return True if all characters in the string are digits
print(txt.isspace())    #this will return True if all characters in the string are whitespace
print(txt.zfill(60))    #this will pad the string with zeros on the left to fill the given width
print(txt.partition("world"))  #this will split the string into a tuple of three parts separated by "world"

#STRING CONCATENATION
# string concatenation is the operation of joining two or more strings end-to-end to form a new string.
# it is done using the + operator in python and is very easy to implement. no need for any example here.

