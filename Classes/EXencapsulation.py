class Animal:
    def __init__(self, name = ""):
        self._name = str(name)
    
    def get_name(self):
        return self._name

animal = Animal("Jeremy")
print animal.get_name()
