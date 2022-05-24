

def decorate_me(func):

    def wrapper():
        print("I am decorating")
        x = 10+5
        func()
        print("Jus finished decoration")

        # return 10
    return wrapper



def decorate(func):
    def wrapper(*args,**kwargs):
        print("decorating")
        func(*args,**kwargs)

    return wrapper



@decorate_me  # warpper_obj = decorate_me(display)
def display():
    print("I am display function")
@decorate_me  #warpper_obj1 = decorate_me(show)
def show():
    print("I am showe function")

@decorate
def result(*args,**kwargs):
    print(args)
    print(kwargs)


#Calling section.......

# display()
# show()
result(10,2,30, name = "Decirate")
