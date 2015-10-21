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

IEEE_cat1 = Cat("Michele", sound = "NooooooNoooNooNoooo~", action = "Put out fires")
IEEE_cat2 = Cat("Fernan", action = "Rub head")
IEEE_dog1 = Dog(name = "Jeremy", sound = "Where's my shoes?", action = "Play Wii")
IEEE_dog2 = Dog("Richie", action = "Sleep") 

IEEE_farm = []
IEEE_farm.append(IEEE_cat1)
IEEE_farm.append(IEEE_cat2)
IEEE_farm.append(IEEE_dog1)
IEEE_farm.append(IEEE_dog2)

for IEEE_animal in IEEE_farm:
    print str(IEEE_animal) 
