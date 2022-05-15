#=======================================


# def show(name, price, incentive):
#     total = price + incentive
#     print(f"My name is:{name},total amount :{total}")
#
#
#
# # show()  # missing argument
# show("Rahul",20,50)
# # show(20,30,"Rahul")
#

#======================================================




# def show(name, price, incentive):
#     """
#     Keyword argument can be passed  out of order.
#     Python intereter uses keyword(variable name) matched to the value passed with argument.
#     """
#     total = price + incentive
#     print(f"My name is:{name},total amount :{total}")


# show()  # missing argument
# show(name = "Rahul",price = 2500,incentive=100)
# show(price=5000,incentive=25,name="Mohit")
# show(price=5000,incentive=25,name2="Mohit")


# ===================================================================================
"""
We can also use Positional as well as keyword argument.
If we do so,the positional argument must precede keyword argument
"""

# def show(name, price, incentive):
#     total = price + incentive
#     print(f"My name is:{name},total amount :{total}")


# show("Ganga",price=55,incentive=60)
# show("Ganga",incentive=60,price=55)
# show(incentive=60,"Ganga",price=55)


# ============================================================================================================

"""
Sometime , number of positional argument to be passed to a function is not certain,
In such-case, variable-lenght positional argument  can be received using *args
"""

# def display(*args):
#     for var in args:
#         print(var)


# display(10)
# display(10,25)
# display(10,25,[10,20,50],(20,5))


# ================================================

"""
Sometime, number of keyword argument  passed to a function is not certain,
In such case,variable length key-word  argument can be received using **kwargs
"""

# def display(**kwargs):
#
#     for key, val in kwargs.items():
#         print(key, val)
#
#
# # display(name = "Khan",price = 20)
# display(name="Khan", price=20, incentive=20,list1 = [10,20])


# ===================================================
"""
If function is to receive required as well as opetional argument,then they must occure
in the following order
    positional argument
    variable-lenght positiona argument
    keyword argument
    variable-length keyword argument

"""

# def show_all(x, y, *args, name, price, **kwargs):
#     print(f"x= {x},y={y}")
#     print("variable-lenght positiona argument")
#     for var in args:
#         print(var)
#
#     print("keyword argument")
#     print(f"name= {name},price={price}")
#
#     print("**kwargs")
#     for key, val in kwargs.items():
#         print(key, val)


# show_all(20, 50, name="Ganga", price=5000)
# show_all(20, 50, 500, 600, name="Ganga", price=5000,city = "Meerut",country = "country")
# show_all(20, 50, 500, 600, name="Ganga", price=5000,city = "Meerut",country = "country")

# def deful(a,b,name,country = "India"):
#
#     """
#     while defining default argument,it must follow the non default argument
#     """
#     print(a,b)
#     print(country)
#     print(name)
#
# deful(10,20,name = "Ganga")


# =====================================================================

"""
Unpacking Argument:
Suppose a function is expecting positinal arguments and the arguments to be
passed are in a list,tuple or set.
In such case we need to unpack the list/tuple/set using * operator before passing it to the function
"""


# def show_arg(a, b, c):
#     print(a, b, c)
#
#
# l1 = [10, 20, 30]
# tpl = (200, 'A', 300)
# s1 = {1,2,3}
# # show_arg(*l1)
# # show_arg(*tpl)
# show_arg(*l1)
# l1 = [10,20,20]
# print(*l1)



#==============================================================================

"""
Unpacking Argument:
Suppose a function is expecting keyword arguments and the arguments to be
passed are in a dictionary
In such case we need to unpack the dictionary using * operator before passing it to the function
"""

def show_dict(name,city,color):
    print(f"Name:{name},City:{city},color:{color}")



data = {"name":"Ganga","city":"Mumbai","color":"Red"}

show_dict(*data)  # pass key
show_dict(**data)   # pass way