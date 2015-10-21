#Syntax
The most important thing to remember is that python is a scripting language, and the syntax is fairly flexible.  

##If-Else
The if-else statement is similar to most coding languages.
However, the syntax uses : and spaces rather than brackets.  
Also note there are no ;.
 
Example If-Else Statement:
```
a = 1

if a == 1:
    a = 2
elif a == 2:
    a = 3
else:
    a = 1
```

Notice that you do not need the parenthesis for the statements. It is generally better to not use parenthesis if they are not needed for Python. This makes the code easier to read and understand.


##Loops 
Python supports the basic while and for loops, but the loops also allow for iteration of objects.  

###While Loop
The while loop is similar to most languages. However, it can also be used with an else statement.

Example While Loop
```
#Initialize i to be 0
#Initialize maxLength to be 10
i = 0
maxLength = 10

#Print i if i is less than maxLength
while i < maxLength:
    print i
    i += 1
#Else print i is greater than maxLength
else:
    print str(i) + " is greater than " + str(maxLength)
```

Notice that i += 1 is used rather than i++. i++ is not valid syntax.  

###For Loop
The for loop is slightly different than most languages. It generally iterates over a list.

Example For Loop:
```
#Similar to the While Loop example without the else
for i in range(0, 10):
    print i

#Goes through each element in array1 and prints the element
array1 = [1, 2, 3]
for i in array1:
    print i
```

###Loop Control Statements
These are statements that can be used within any loop.
####Break
This will terminate the loop and continue to the code following the loop.  

Example Break:  
```
array1 = [1, 2, 3]
for i in array1:
    if i == 2:
        break
    print i
print "end"
```
This results in:
```
>>1
>>end
```

####Continue
This will continue to the next iteration of the loop.  

Example Continue:
```
array1 = [1, 2, 3]
for i in array1:
    if i == 2:
        continue
    print i
print "end"
```

This results in:
```
>>1
>>3
>>end
```

####Pass
This will simply be a passed in the loop.  

Example Pass:
```
array1 = [1, 2, 3]
for i in array1:
    if i == 2:
        pass
    print i
print "end"
```

This results in:
```
>>1
>>2
>>3
>>end
```
##Global Variables
Python does support global variables. These are simply variables that are defined outside of objects, loops, functions, etc. These can also be defined within them with global. global is required when changing variable inside of functins or objects.  

Example Global Variables:  
```
# This is going to be our global variable
# You do not need global_ this is just what I am calling it.
global_var = 1

def function1():
    """This function will set the global variable global_var equal to 2.
    """

    global global_var
    global_var = 2

def function2(global_var):
    """This function will set the local variable input global_var equal to 3.
    """
    global_var = 3

def function3():
    """This function will set the local variable global_var equal to 4.
    """
    global_var = 4

function1()
print "global_var = ", global_var

check_var = 1
function2(check_var)
print "global_var = ", global_var
print "check_var = ", check_var

function3()
print "global_var = ", global_var
```
The console prints:
```
>>global_var = 2
>>global_var = 2
>>check_var = 3
>>global_var = 4
```

##Comments  
Comments in python can be written with # followed by the comment.  
These should be used to explain what is going on with specific lines of code.  

Example Comment:  
```
# This is a Comment.
```
##Documentation  
Documentation in python can be written with ''' or """ followed by the documentation and closed with ''' or """.
These should be used to tell the user what the class or function does.
It should also tell what the parameters and returns are if applicable.

Example Doc String 1:  
```
"""This is a Doc String
    You can type more here.
"""
```

Example Doc String 2:  
```
'''This is another Doc String.
   You can type more here.
'''
```

##Spacing  
Python defines blocks for functions or classes with spacing.  
It accepts both tabs or spaces for creating these blocks, but it is important to not mix tabs with spaces. A good rule is to never use tabs or to change tabs to spaces. For this tutorial all spacing will be 4.

Example Function:
```
def function:
    print "This is a function"
```

Note that if indentation levels occur from the compiler but the code looks like it has the same level of spaces, then the code probably mixed tabs with spaces.

##Object Format
For most of Python, everything can be thought of as an Object.  
The reason I say this is because even datatypes have functions or methods.  

Example Numbers:
```
a = 1
a.bit_length()

# The console would display 1
``` 

The basic way to access any member or method from an object is to use the . operator. This applies for classes as well.

Example Class:
```
# This is a basic class
class 

```
