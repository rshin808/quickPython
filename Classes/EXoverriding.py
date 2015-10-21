class Animal:
    def __init__(self, name):
        self._name = str(name)

    def __str__(self):
        return "I am an Animal with name " + self._name        

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

    def __str__(self):
        return self._sound + " I am a Cat with name " + self._name + ", and I like to " + self._action

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action

class Dog(Animal):
    def __init__(self, name = "", sound = "Woof!", action = "Fetch"):
        Animal.__init__(self, name)
        self._sound = str(sound)
        self._action = str(action)

    def __str__(self):
        return self._sound + " I am a Dog with name " + self._name+ ", and I like to " + self._action

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action

cat = Cat("Kitty")
dog = Dog("Doggy")

animals = [cat, dog]

for animal in animals:
    print str(animal)
