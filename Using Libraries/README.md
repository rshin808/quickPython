#Using Libraries
##Importing Libraries
Python libraries can be added by using import. Python comes with many pre-installed libraries, but the libraries still need to be imported. There are also other libraries that may need to be installed. The easiest way to do this is with pip, but others may need to be installed from the source. Also when installing these packages make sure you meet the requirements.  

Example Install from Pip:
Note this is installed from the command-line.
```
# After installing the requirements
pip install psycopg2
```

Example Install from Source:
Note this is installed from the command-line.
```
# After extracting the source
# Changing to the extracted source directory
# This build option is not usually used, but it is required for the psycopg2 installer
python setup.py build
sudo python setup.py install
```

Example Import Library:
```python
import psycopg2
```

##Checking Library Features
The best way to check what a library has to offer is by going to the documentation for the library. Another way is if you already know the library function, then you can use dir. Dir works well if you are looking what methods a class has to offer and what you can access. But you should not use it on the library unless you do not have access to the documentation or the library is small. A better alternative would be to use help. Another alternative is to use the doc strings by calling the __doc__ method.

For me, I typically use the documentation. However, if I cannot access the documentation, then I would start with dir. Dir will show me what the module has to offer (usually you can guess the basic functions from the naming convention). Then, I would use dir or __doc__ on the modules members that I may want to use. If I really do not understand how to use the module, then I would use help.

Note that these should be from the python interpreter (sandbox).

Example Libary Documentation:
The psycopg2 documentation can be found [here](initd.org/psycopg/docs/).
This is a good way to learn about how to use the library and its features.

Example Dir:
```python
import psycopg2

# This shows what is in module
dir(psycopg2)
```

The console prints:
```
BINARY,Binary,DATETIME,DataError,DatabaseError,Date,DateFromTicks,Error,IntegrityError,InterfaceError,InternalError,NUMBER,NotSupportedError,OperationalError,ProgrammingError,ROWID,STRING,Time,TimeFromTicks,Timestamp,TimestampFromTicks,Warning,__builtins__,__doc__,__file__,__name__,__package__,__path__,__version__,_connect,_ext,_json,_param_escape,_psycopg,_range,apilevel,connect,extensions,paramstyle,threadsafety,tz
```

Example Help:
```python
import psycopg2

# This gives alot of information
help(psycopg2)
```

Example Doc String:
```python
import psycopg2
# This will not give too much information unless well documented
psycopg2.__doc__ 

# Looking at the Doc strings for methods, functions, or objects is better with __doc__
psycopg2.Timestamp.__doc__
```
