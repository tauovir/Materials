

"""

First Class Objects
In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
"""

def decorate(func):
    print("I am decorater")

    def wraper(*args, **kwargs):
        return func(args[0])

    return wraper

def decorate2(func):
    print("I am decorate2 two")

    def wraper(*args, **kwargs):
        return func(args[0])

    return wraper

@decorate2
@decorate
def get_data(num):
    """
    Adding list data
    :return:
    """
    print("num:",num)
    l1 = [2,3,4,5,6]
    print("...Adding list....")
    l1.append(num)
    x = sum(l1)
    print("Sum:",x)
    return x



if __name__ =="__main__":
    resp = get_data(20)
    print("Resp",resp)