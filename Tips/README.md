#Tips  
This section just covers some helpful tips in Python.
##Paths 
Paths are important for code within multiple files. Usually, adding a __init__.py is all that is needed. However, if you need specific paths relative to the working directory, then you need to be able to define this in the code.


Example Script Path:
Note that it only works within script files.
```python
# This code will get the full path to the script file.

import os
script_path = os.path.dirname(os.path.realpath(__file__))

# Show how it looks
print script_path
```
 
After getting the full path, you can join or split the path depending on what folder(s) need to be accessed. 

Example Script Split Join:
```python
import os
script_path = os.path.dirname(os.path.realpath(__file__))

# Show how it looks
print script_path
print os.path.split(script_path)
print os.path.join(os.path.split(script_path)[0], os.path.split(script_path)[1])
```


You can also add paths during run-time.

##Help Resources    
The majority of Python resources are online. The online documentation found [here](https://docs.python.org/2/) is extremely useful when first learning about a library. Some libraries also have their own documentation, but these usually give examples so it is still easy to use the library. Python also has a large online community that provides advice as well as open-source code examples. Overall, there is an abundance of help resources for Python.
However sometimes you may not be able to use the internet. For this, you can use Python's help, dir, and docs. These commands can all be used in the interpreter, and they will help understanding how a Python module works. The help command gives a lot of information about the module, but I usually do not need this command. I normally find dir to be more useful because all I need is to know what methods are available. This is very useful when the naming conventions are well done in relation to what the function does. I can also use the docs to get more information, but I generally only need dir.

##Interpreter
Python has an interpreter that allows you to run python code. You can test small bits of code to make sure it does what you want. Then you can just put the working code into a file. The interpreter is great for helping to remember the syntax of a library. It also lets you check before adding new lines to your main script files.
 
##Standards
Python is open-source, and there are a variety of coding standards. For now a good standard is the [google standard](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html), but any standard is fine. Standards are only enforced if you are working in companies or groups. If this is just for a personal project, then just choose the standard that you like best.

##IDE  
Whatever IDE you use, always set the tabspaces to 4 or just use 4 spaces. This helps prevent indentation errors. It is also nice to set syntax highlighting for the code. IDEs like Spyder or Eclipse with Pydev can do this for you, and they also have autocomplete.

Example Vim:
In the vim folder, edit the vimrc file.
Add these lines to the end of the file:
```
sytnax on
set tabstop=4
set shiftwidth=4
set expandtab
```
