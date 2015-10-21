
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
print ee_algorithms
print ee_hardware

# Difference
ee_nonhardware = ee - ee_hardware
print ee_nonhardware
