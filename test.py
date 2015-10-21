import os
s = os.path.dirname(os.path.realpath(__file__))
print os.path.split(s)
print os.path.join(os.path.split(s)[0], os.path.split(s)[1])
