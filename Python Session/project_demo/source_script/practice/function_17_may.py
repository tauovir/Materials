"""
simple function
"""


def first():
    print("Hello from first")


def second():
    print("I am from second")


"""
to_upper
"""


def make_upper():
    name = "python function"
    x = name.upper()
    print(x)


"""
positional arguments/required arguments
"""


def inc(m1, m2, m3):
    m1 = m1 + m2 + m3 * 2
    return m1


"""
keyword arguments/required arguments
"""


def make_changes(name, age):
    name_uppr = name.upper()
    age += 10
    print(f"My name is {name_uppr}, I am {age} years old")


"""
default argument
"""


def make_changes2(name, age=15):
    name_uppr = name.upper()
    age += 10
    print(f"My name is {name_uppr}, I am {age} years old")


"""
positional and names arguments
"""


def pos_named(city, price, color):
    print("city:", city.upper())
    print("Price:", price)
    print("color:", color.upper())




# first()
# second()
# make_upper()
# x = inc(10,30,60)
# x = inc(10,30,60)
# make_changes(25,"ganga")
# make_changes(name ="rahul",age=26)
# make_changes2(name ="rahul")
# pos_named("Kanpur", price=25000, color="Black")

