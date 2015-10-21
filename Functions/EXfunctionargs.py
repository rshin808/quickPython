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
