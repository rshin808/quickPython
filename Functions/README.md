#Functions
##Defining a Function
Python functions are defined using def followed by the function name. The parameters are put in parenthesis following the function name. The function also does not need return argument, and the return does not need to be the same datatype. The main requirement is that the function is defined before it is called.  

Example Function:
```python
def function1():
    print "Hello"    

def function2(par1):
    return par1

def function3(par1, par2):
    print str(par1)
    print str(par2)

    if par1 == 1:
        return "par1"
    else:
        if par2 == 1:
            return par2

function1()
print function2("Hi")
print function3(1, 1)
function3(0, 1)
print function3(0, 0)
```

##Passing Function Arguments
Python functions can pass arguments like most languages. The arguments can also be changed in the function if they are mutable. 

Example Function Arguments:
```python
test1 = 0
test2 = [1, 2, 3]

def function1(par1):
    par1 = 10
    print par1

def function2(par1):
    par1[0] = 0
    print par1

print test1
function1(test1)
print test1

print test2
function2(test2)
print test2
``` 

##Passing a Function as an Argument
Python allows functions to be passed as arguments.  

Example Function Passing:
```python
def check(func):
    if func() == 1:
        print "function1"
    elif func() == 2:
        print "function2"
    else:
        print "uknown function"

def function1():
    return 1

def function2():
    return 2

def function3():
    pass

check(function1)
check(function2)
check(pass)
```

##Lambda Functions
Lambda functions create functions without a name. These are functions that are just needed where they are created and not usually re-used. These are devined with lambda.  

Example Lambda Function:
```python
lfunc = lamba x, y: x + y
print lfunc(2, 1)
```
