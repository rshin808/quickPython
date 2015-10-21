#Classes  
##Defining a Class  
Python classes can be defined with class. Classes have pre-defined methods that are in the base object class. These special methods are in the form \_\_xx\_\_, and they can be overloaded to suit the class. More information can be found [here](https://docs.python.org/2/reference/datamodel.html). Also note that for all methods in a class, the first parameter self is always required (sometimes it can be something else like cls).  

Example Define a Class:  
```
class Animal:
    def __init__(self, name):
        self.name = str(name)

animal = Animal("Jeremy")
print animal.name
```

\_\_init\_\_ is like the constructor for the class, and the class member variables require self in front of them.  

Like functions, Class methods can also have default arguments. When using default arguments, make sure that all parameters have a default argument.

Example Class Default Arguments:
```
class Animal:
    def __init__(self, name = ""):
        self.name = str(name)

animal = Animal()
print animal.name
```

##Encapsulation  
Encapsulation requires keeping class methods and variables hidden within the class. Only accessor methods should be used with the class. These are the private and public variables and methods. Python does not really have private variables and methods. These are implied with \_. You can still access the class variable or method, but in practice you are not supposed to. Classes also have \_\_, which prevents the method from being overridden.  

Example Encapsulation:
```
class Animal:
    def __init__(self, name = ""):
        self._name = str(name)
    
    def get_name(self):
        return self._name

animal = Animal("Jeremy")
print animal.get_name()
``` 

##Inheritance  
Inheritance allows sub classes from base classes. The sub class has access to all the base class variables and methods. The sub class is a more detailed class of the base class.

Example Inheritance:
```
class Animal:
    def __init__(self, name):
        self._name = str(name)

    def get_name(self):
        return self._name

def Cat(Animal):
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
```

##Polymorphism  
Polymorphism occurs when a condition occurs in several different forms. Sub classes inherrited from the same base class may have the same method. But, the method may be different depending on the sub class.

Example Polymorphism:
```
class Animal:
    def __init__(self, name):
        self._name = str(name)

    def get_name(self):
        return self._name

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def do_action(self):
        raise NotImplementedError("Subclass must implement abstract method")

def Cat(Animal):
    def __init__(self, name = "", sound = "Meow~", action = "Scratch"):
        Animal.__init__(self, name)
        self._sound = str(sound)
        self._action = str(action)

    def make_sound(self):
        return self._sound

    def do_action(self):
        return self._action

def Dog(Animal):
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
```

##Overriding
Polymorphism also uses overriding when it overrides the abstract methods of the base class. However, special methods can also be overridden to allow Python to call these methods.


Example Overriding:
```
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

def Cat(Animal):
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

def Dog(Animal):
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
```

##Class Summary
Classes are very important of Object-Orient Programming. Therefore it is necessary to have a strong understanding of the basic concepts. This section will cover an example showing Encapsulation, Inheritance, and Polymorphism.

Example IEEE UHM Farm:
```
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

def Cat(Animal):
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

def Dog(Animal):
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

IEEE_cat1 = Cat("Michele", sound = "NooooooNoooNooNoooo~", action = "Fire")
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
```
