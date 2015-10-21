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
