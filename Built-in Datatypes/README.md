#Built-in Datatypes
##Numbers
Numbers could be integers, floats, binary, etc. Python handles these all the same. You can also get the other format representation of the number, but this will be a string type.  

Example Numbers:  
```
# Integer
i = 10

# Float
i = 10.0

# Binary
i = 0b1010

# Hexadecimal
i = 0xa

# Octal
i = 012
```

Example Number Conversions:
```
# Integer to Float, Binary, Hexadecimal, and Octal
i = 10
i = float(i)
i = bin(i)
i = hex(i)
i = oct(i)

print type(i)
```

Note that you can also apply bitwise operators to numbers.  

Bitwise Operators:
* << - bit shift left (multiply by 2)
* >> - bit shift right (divide by 2)
* &  - and
* |  - or
* ~  - not
* ^  - exclusive or

##Strings
Strings in Python can be written with " or ' wrapping the string. Having both allows users to include " or ' within the string as well. Strings can also be concatted to other strings with +. Strings can also be split and indexed by. 

Example String:  
```
# Basic string manipulation
string1 = "Hi you're awesome!"
string2 = 'Thank you :)'
string3 = string1 + string2
letterEX = string1[-1]
array_string1 = string3.split("!")

# Fun string manipulation
string4 = string3.split("!")[0] + string1[-1]

print string1
print string2
print string3
print letterEX
print array_string1
print string4
```

The console prints:
```
>>Hi you're awesome!
>>Thank you :)
>>Hi you're awesome! Thank you :)
>>!
>>Hi you're awesome
>>Hi you're awesome!
```

Python can also convert other datatypes into strings. It can also convert classes if the string handler is defined.  

Example String Conversions:
```
i = 10
string_i = str(i)
print string_i

a = [1, 2, 3]
string_a = str(a)
print string_a

class Hi:
    def __str__(self):
        return "Hi"

print str(Hi())
```

The console prints:
```
>>10
>>[1, 2, 3]
>>Hi
```

##Lists
Lists are the same as arrays. But in Python there are many methods for them, and they can be used to implement other data structures like Queues or Stacks. Lists are defined using [].   

Example Basic List Methods:
```
# Create a List
list1 = [1, 2, 3]
print list1

# Add to the end of a List
list1.append(4)
print list1

# Insert into a List at Index
i = 0
list1.insert(i, 0)
print list1

# Remove the first item in List by a Value
v = 4
list1.remove(v)
print list1

# Pop an item from the List at Index and Return it
i = 0
list1.pop(i)
print list1

# Reverse a List
list1.reverse()
print list1
```

The console prints:
```
>>[1, 2, 3]
>>[1, 2, 3, 4]
>>[0, 1, 2, 3, 4]
>>[0, 1, 2, 3]
>>[1, 2, 3]
>>[3, 2, 1]
```

Python also allows list manipulation and indexing.  

Example List Manipulation and Indexing:
```
a = [1, 2, 3, 4]
print a[0]
print a[2]
print a[-1]
print a[-2]
print a[::-1]
print a[1:]
print a[:2]
print a[1:2]

b = [i for i in range(5)]
print b

print len(b)
print a == b

```

The console prints:
```
>>1
>>3
>>-4
>>-3
>>[1, 2, 3, 4]
>>[2, 3, 4]
>>[1, 2, 3]
>>[2, 3]
>>[1, 2, 3, 4]
>>5
>>True
```

One more important note is that List assignments point to the List. You need to make a deep copy of the List to not affect the other.

Example List Copy:
```
a = [1, 2, 3]
b = a

print a
print b

b.append(4)
print a
print b

b = list(a)
print a
print b

b.pop()
print a
print b
```

The console prints:
```
>>[1, 2, 3]
>>[1, 2, 3]
>>[1, 2, 3, 4]
>>[1, 2, 3, 4]
>>[1, 2, 3, 4]
>>[1, 2, 3, 4]
>>[1, 2, 3, 4]
>>[1, 2, 3]
```

##Tuples
Tuples in the same as Lists, but the elements in them cannot be changed. These are defined with ().  

Example Tuple:  
```
tuple1 = (1, 2)
list1 = [1, 2]

print tuple1
print list1

print tuple1 == list1
print tuple1 == tuple(list1)

print list1
print tuple(list1)

tuple1 = list1
print tuple1
```

The console prints:
```
>>(1, 2)
>>[1, 2]
>>False
>>True
>>[1, 2]
>>(1, 2)
>>[1, 2]
```

##Dictionaries
Dictionaries are lists with a key and values. These have a key that can be used as the index for the value they represent. These are defined with {}.    

Example Dictionary:
```
dict1 = {
    "key" : "value",
    "1" : 1,
}

print str(dict1)
print dict1["1"]
```

##Sets
Sets are unordered collections of unique elements. These allow standard math operations on sets like intersection, union, and difference. These are defined with ([]).  

Example Set:
```
# Import the library
from sets import Set

# Define Sets
ce = Set(["Michele", "Jason"])
ep = Set(["Cristina", "Fernan"])
s = Set(["Jeremy"])

# Add
ep.add("Reed")

# Union
ee = ce | ep | s
print ee
algorithms = ce | s
print algorithms

# Intersection
ee_algorithms = ee & algorithms
ee_hardware = ee & ep

# Difference
ee_nonhardware = ee - ee_hardware

```
