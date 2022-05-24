

def outer():
    print("outer")
    def inner():
        print("I am inner function")

    return inner


# def show_from_me(name,func,func2):
#     print("show from me")
#     func(name)
#     func2()
# #
# def show(name):
#     print("Name is :",name)
#
#
# def display():
#     print("Display me")
#
#
# def return_func(func):
#     print("return_func")
#     return func
#
#
#
# # Calling section
# show_from_me(name = 'Apple',func = show,func2=display)

# function_var = return_func(display())
# print(function_var)
# function_var()
inner_func = outer()
inner_func()