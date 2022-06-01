"""
try->finally ( without except,here exception not caough but raised)
try must followed either except/finally
else must come before finally
"""

def calc():
    print(".....Program Statrted.........")
    try:
        x = 2/0
        print("x:",x)
    finally:
        print("Enter in Program")

def calc2():
    print(".....Program Statrted.........")
    try:
        x = 2/0
        print("x:",x)


    except BaseException as e:
        print("Base exceptipn:",e)
    except Exception as e:
        print("Exception Operation:", e)
    except ArithmeticError as e:
        print("Arithmatix Operation:", e)


    else:
        print("no exception")
    finally:
        print("Relasing resource")


def classtree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)


def clstree(cls,indentaion):
    print("_" * indentaion, cls.__name__)
    for subcls in cls.__subclasses__():
        clstree(subcls,indentaion+3)

def built_err():
    print(dir(locals()))
def sysntax_err():
    exp = """print("pppp")"""
    try:
        c = eval(exp)
        print(c)
    except SyntaxError as e:
        print("error Occured:",e)


def test_ecp():
    print("Program started")
    try:
        c = 10/5
        print("Hi there")
        # exit()
        print("Try end")
    except Exception as e:
        print("Exception ocured")

    else:
        print("exception not coocured")
    finally:
        print("Finally resource released")

if __name__ == "__main__":
    # calc()
    # calc2()
    # classtree(BaseException)
    # clstree(BaseException,0)
    # print(sysntax_err())
    # built_err()
    # print(dir(locals()['__builtins__']))
    test_ecp()