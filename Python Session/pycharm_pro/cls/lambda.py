

def lam1():
    lamb = lambda x, y, z: x + y + z
    x = lamb(10,20,30)
    print("Retun value:",x)

def lam2():
    """
    Opetional
    :return:
    """
    lamb = lambda *arg,**kwargs: sum(arg + tuple(kwargs.values()))
    x = lamb(10,20,30,x = 50,y = 12)
    print("Retun value:",x)

def lam1():
    lamb = lambda x, y, z: x + y + z
    print("lamb:",lamb)
    x = lamb(10,20,30)
    print("Retun value:",x)


def filter_func(x):
    if x >4:
        return True
    return False

def filter_out():
    """
    The filter function is used to select some particular elements from a sequence of elements.
     The sequence can be any iterator like lists, sets, tuples, etc.
     The elements which will be selected is based on some pre-defined constraint. It takes 2 parameters:
      1.  A function that defines the filtering constraint
      2.  A sequence (any iterator like lists, tuples, etc.)
    :return:
    """
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: x%2==0,my_list))
    new_list = list(filter(lambda x: x > 4, my_list))
    new_list2 = list(filter(filter_func, my_list))

    print("Filter")
    print(new_list)
    print(new_list2)

def map_out():
    """
    The map() function in Python takes in a function and a list.
    The function is called with all the items in the list and a new list is
     returned which contains items returned by that function for each item.
    :return:
    """
    # Program to double each item in a list using map()

    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    my_list2 = [10,20,30,50]

    # new_list = list(map(lambda x: x * 2, my_list))
    new_list = list(map(lambda x,y: x+y, my_list,my_list2))
    print("map")
    print(new_list)

def lamb3():
    """
    n this part, we are defining a lambda and calling it immediately by passing the string as an argument.
    This is something called an IIFE, and you’ll learn more about it in the upcoming sections of this tutorial.
    IIFE stands for immediately invoked function execution
    :return:
    """
    x = "some kind of a useless lambda"
    (lambda x: print(x))(x)

def lamb4():
    """
    Opetional
    :return:
    """
    # lamb = lambda *arg,**kwargs: sum(arg + tuple(kwargs.values()))
    # x = lamb(10,20,30,x = 50,y = 12)
    print((lambda *arg, **kwargs: sum(arg + tuple(kwargs.values())))(10,20,30,x = 20))
    print((lambda x: x + x)(2))


if __name__ =="__main__":
    # lam1()
    # lam2()
    # filter_out()
    map_out()
    # lamb3()
    # lamb4()
