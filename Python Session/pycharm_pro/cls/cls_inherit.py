
"""
Inheritance is the process by which one class takes on the attributes and methods of another.
 Newly formed classes are called child classes,
and the classes that child classes are derived from are called parent classes.

Child classes can override or extend the attributes and methods of parent classes. In other words,
child classes inherit all of the parent’s
attributes and methods but can also specify attributes and methods that are unique to themselves.


You may have inherited your hair color from your mother.
It’s an attribute you were born with. Let’s say you decide to color your hair purple.
Assuming your mother doesn’t have purple hair, you’ve just overridden
the hair color attribute that you inherited from your mom.

You also inherit, in a sense, your language from your parents.
If your parents speak English, then you’ll also speak English. Now imagine you decide to learn a second language,
like German. In this case you’ve extended your attributes because you’ve added an attribute that your parents don’t have.
"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound):
        """
        method overiding
        :param sound:
        :return:
        """
        return f"{self.name} does not say {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


if __name__ == "__main__":
    obj = Dog("Bulldog",15)
    print(obj)
    obj.speak(sound=25)
    miles = JackRussellTerrier("Miles", 4)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    print(miles.name)
    print(type(miles))
    """
    More generally, all objects created from a child class are instances of the parent class, 
    although they may not be instances of other child classes
    """
    # print(isinstance(miles, Dog))
    # print(isinstance(miles, JackRussellTerrier))
    # print(isinstance(miles, Dachshund))
    print(miles.speak(100))
