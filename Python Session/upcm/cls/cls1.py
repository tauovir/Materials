"""

lthough too advanced a topic for a beginning Python book,
understanding dunder methods is an important part of mastering object-oriented programming
 in Python.
"""


class Dog:
    #class attributes,Class attributes are defined directly beneath the first line of the class name
    #When an instance of the class is created, class attributes are automatically created and
    # assigned to their initial values
    #Use class attributes to define properties that should have the same value for every class instance.
    # Use instance attributes for properties that vary from one instance to another.
    species = "Canis familiaris"
    def __init__(self, name, age):

        """
        An instance attribute’s value is specific to a particular instance of the class
        :param name:
        :param age:
        """
        self.name = name  # instance attributes.
        self.age = age

        # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

        # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


class Dog1:
    pass

if __name__ == "__main__":
    """
    Creating a new object from a class is called instantiating an object. 
    You can instantiate a new Dog object by typing the name of the class, 
    followed by opening and closing parentheses:
    """
    obj1 = Dog("Black Dog",15)
    obj2 = Dog("Red doc",18)
    # print("nam:",obj1.name)
    # print("age:",obj1.age)
    #
    # obj1.age = 55
    # Dog.species = "Kaka spcied"
    # print("Dog:", Dog.species)
    # print("Dog:", obj1.age)
    # print("Dog:", obj1.species)
    # print("Dog:", obj2.species)

    # print(obj1.())
    print(obj1)

