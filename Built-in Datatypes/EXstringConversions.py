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
