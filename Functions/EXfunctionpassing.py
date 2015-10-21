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
check(function3)
