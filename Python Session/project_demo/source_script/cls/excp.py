import sys
"""
How python code compile
https://towardsdatascience.com/how-does-python-work-6f21fd197888#:~:text=For%20the%20most%20part%2C%20Python,pyc%20or%20.
http://net-informations.com/python/iq/linking.htm#:~:text=Compiled%20code%20is%20usually%20stored,py%20files%20or%20the%20.
"""
def excep1():
    a = [2,6,0,5]
    b = 100
    for val in a:
        m1 = b/val
        print("M1:",m1)

def excep2():
    """
    Catch the exception and complete the flow
    :return:
    """
    a = [2, 6, 0, 5]
    b = 100
    for val in a:
        try:
            m1 = b / val
            print(f"{b}/{val} = {m1}")
        except Exception as e1:
            print("error occured",e1)
            # Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()
            print("ex_type!", ex_type, "occurred.")
            print("ex_traceback!", ex_traceback, "occurred.")
            print("ex_traceback!", ex_traceback, "occurred.")
            print("__class__!", e1.__class__, "occurred.")

    print("End program")


def excep3():
    """
    Catching Specific Exceptions in Python
    try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

    :return:
    """


def raise_excp():
    a = [2, 6, 15, 5]
    b = 100
    for val in a:
        if val == 0:
            raise  ValueError("Value should be greater than 0")
        m1 = b / val
        print("M1:", m1)
    print("Program end")

def call_raise():
    """
    Python try with else clause
    In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
     For these cases, you can use the optional else keyword with the try statement.

    :return:
    """

    try:
        raise_excp()
    except ValueError as e:
        print(e)
    else:
        print("No exception occure")
    print("Program fineshed")


if __name__ =="__main__":
    pass
    # excep1()
    # excep2()
    # call_raise()
    # c = 10 + b
