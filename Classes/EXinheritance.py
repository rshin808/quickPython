class Animal:
    def __init__(self, name):
        self._name = str(name)

    def get_name(self):
        return self._name

class Cat(Animal):
    def __init__(self, name = "", sound = "Meow~", action = "Scratch"):
        Animal.__init__(self, name)
        self._sound = str(sound)
        self._action = str(action)

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action

cat = Cat("Kitty")
print cat.get_name()
print cat.make_sound()
print cat.do_action()
