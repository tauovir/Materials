"""

# Syntex error can not be causght
#IndentationError
"""
#====================

def err():
    a,b = 10,'ab'
    # c = a+b  # type error
    # c = 100 / 0  #Zero Division Error
    # import csv33  # ModuleNotFoundError:
    pass

def key_interrup():
    try:
        inp = input(" Enter value")
        print('Press Ctrl+C or Interrupt the Kernel:')
    except KeyboardInterrupt:
        print('Caught KeyboardInterrupt')
    else:
        print("No exception occurred")
    finally:
        relase_resource()


    print("Program end")

def zero_div():
    try:
        a = 100 / 0
        print(a)
    except ZeroDivisionError:
        print("Zero Division Exception Raised.")
    else:
        print("No exception occurred")
    finally:
        relase_resource()
    print("Program End")


def index_err():
    try:
        a = ['a', 'b', 'c']
        print(a[4])
    except LookupError:
        print("Index Error Exception Raised, list index out of range")
    else:
        print("Success, no error!")
    finally:
        relase_resource()
    print("Program End")

def multi_handl_v1():
    try:
        # c = 100/0
        d = {"p":10}
        d1 = d["pp"]
        inp = input(" Enter value")
        print('Press Ctrl+C or Interrupt the Kernel:')
    except KeyboardInterrupt:
        print('Caught KeyboardInterrupt')
    except ZeroDivisionError:
        print('zero div error')
    except LookupError:
        print('lookup error')
    except Exception:
        print("all exception")
    else:
        print("NO exception occurred")
    finally:
        relase_resource()
    print("Program End")


def relase_resource():
    print("resource released successfully")

def multi_handl_v2():
    try:
        c = 100/0
        d = {"p":10}
        d1 = d["p"]
        inp = input(" Enter value")
        print('Press Ctrl+C or Interrupt the Kernel:')
    except (KeyboardInterrupt,ZeroDivisionError,LookupError):
        print('Caught')
    except Exception:
        print("all exception")
    finally:
        relase_resource()
    print("Program End")



if __name__=="__main__":
    # err()
    # key_interrup()
    # zero_div()
    # index_err()
    # multi_handl_v1()
    # multi_handl_v2()



