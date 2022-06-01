
class CustExcep(Exception):
    def __init__(self,msg,val):
        self.msg = msg
        self.val = val

    def __str__(self):
        return f"Exception:{self.msg}:{self.val}"


def rais_excep(a):

    if a <=0:
        raise ValueError('In Valid value provided.')
    else:0
        return a *3

def account():
    balance = 1000
    with_draw = float(input("Enter withdrwal amount"))
    if with_draw > balance:
        raise CustExcep("Insufficient balance",balance)

    balance = balance-with_draw
    return balance

def call():
    n = int(input("Enter number:"))
    res = None
    try:
        res = rais_excep(n)

    except ValueError as e:
        print(e)
    else:
        print("No exception is here")
    print("result:",res)

def call2():

    res = None
    try:
        res = account()

    except ValueError as e:
        print(e)
    except CustExcep as e:
        print(e)
    else:
        print("No exception is here")
    print("Balnce:",res)


if __name__=="__main__":
    # call()
    call2()