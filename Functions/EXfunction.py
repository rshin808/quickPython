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
