class Animal:
    def __init__(self, name):
        self._name = str(name)

    def get_name(self):
        return self._name

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def do_action(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def __init__(self, name = "", sound = "Meow~", action = "Scratch"):
        Animal.__init__(self, name)
        self._sound = str(sound)
        self._action = str(action)

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action

class Dog(Animal):
    def __init__(self, name = "", sound = "Woof!", action = "Fetch"):
        Animal.__init__(self, name)
        self._sound = str(sound)
        self._action = str(action)

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action
    
    
cat = Cat("Kitty")
dog = Dog("Doggy")

animals = []
animals.append(cat)
animals.append(dog)

for animal in animals:
    print animal.__class__.__name__
    print animal.get_name()
    print animal.make_sound()
    print animal.do_action() 
