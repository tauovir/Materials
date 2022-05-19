
"""
Variable length positional argument
"""
def show(*args):
    print(args)
    print(type(args))
    for x in args:
        print(x)

def average(*args):
    print(type(args))
    return (sum(args)/len(args))


""""
variable length keyword argument
"""
def display(**kwargs):

    print(type(kwargs))
    print(kwargs)
    # print(kwargs.keys())
    # print(kwargs.values())
    print(kwargs.items())


"""
Positional argument
variable-lenght positional argument
keyword argument
variable-lenght keyword argument
"""
def all_arg(x,y,*args,name,price,**kwargs):

    print(x,y)
    print("======Variable length positional argument")
    print(args)
    print("======Keyword arg")
    print(name,price)
    print("======variable length keyword argument===")
    print(kwargs)


"""
unpacking arguments
"""
def display_arg(m1,m2,m3,m4):
    print(m1,m2,m3,m4)


def display_arg(m1,m2,m3,m4):
    """

    :param m1:
    :param m2:
    :param m3:
    :param m4:
    :return:
    """
    print(m1,m2,m3,m4)


def display_kwarg(name,price,country):
    """
     Displaying unpacking dictionary

     """
    print(name,price,country)


def add_number(a,b):
    """
    This function is used to add two number
    :param a: integer value
    :param b: float value
    :return: (a+b)/ float
    """
    return a+b

x = add_number(20,30)

"""

"""

def recr():
    print("I am from recursive")
    recr()

# num = 5
def inc_num(num):
    print(num) # 5,6,7,8,9,10
    if num >=10:
        return      # base
    else:
        inc_num(num + 1)  # recursive block


def dec_num(num):
    print(num)
    if num <=1:
        return      # base
    else:
        dec_num(num - 1)  # recursive block


# 5! = 5 * 24
# 5* 4! = 5 * 24
# 4*3! = 4 * 6
#3*2! =>3 *2 = 6
#2*1!
def factorial(n) : #5!,4!,3!,2!,1!
    print(n)
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)







# show(10,20,30)
# c = average(10.30,20.50,30,20)
# print("avg:",c)
# display(color = "Red",price = 50,name = "Mohit", country = "India")
# all_arg(20,30,name = "Mohit",price = 20)

# l1 = [10,20,30,50]
# tpl = (5,3,2,6)
# set = {20,30,50,99,30,20,99}
# display_arg(*l1)
# display_arg(*tpl)
# display_arg(*set)

d1 = {"name" : "Mohit","price" : 200,"country":"India"}
# display_kwarg(*d1)
# display_kwarg(**d1)
# print(all_arg.__doc__)
# print(max.__doc__)
# recr()
# inc_num(1)
# dec_num(10)
fact = factorial(5)
print("fact",fact)






