
def err():

    a,b = 10,'ab'
    # c = a + b
    # c = a/0
    import csv30

def release_resource():
    print("released resource")

def key_err():
    print(" Program started........")
    ## Perform some logical operation
    try:
        # l1  = [10,20,30]
        # n = input("Enter number:")
        # n = int(n)
        # c = n/2
        # print("l1:",l1[5])
        print("====================gggggggg")
        return 10
    except KeyboardInterrupt:
        print("Exception occured")
    except ZeroDivisionError:
        print("Zero division error occured")
    except Exception:
        print("main Exception occurred")
    else:
        print("No exception occured")
    finally:
        release_resource()


    print("Program End....")

def excep1():

    print(" Program started........")
    ## Perform some logical operation
    try:
        n = 10/0
        print("====================gggggggg")
        return 10
    except (KeyboardInterrupt,ZeroDivisionError,IndexError):
        print("Sending notification send_no_manager") # send_no_manager
    except Exception:
        print("main Exception occurred")
    else:
        print("No exception occured")
    finally:
        release_resource()


    print("Program End....")


class CustExcep(Exception):

    def __init__(self,msg,val):
        self.msg = msg
        self.val = val

    def __str__(self):
        return f"Exception:{self.msg}:{self.val}"



def account():
    balance = 1000
    withdrawl = float(input("Enter amount to withdraw:"))

    if withdrawl > balance:
        raise CustExcep("Insufficient Balance:",balance)

    balance = balance - withdrawl
    print(f"Your balance is:{balance}, withdrwal amount:{withdrawl}")


def main():
    print("ATM Sessiuon started")
    try:
        account()

    except CustExcep as e1:
        print(e1)
    else:
        print("Your session executed successfully")
    finally:
        release_resource()

    print(" Thank you for visiting ATM")


if __name__ =="__main__":
    # err()
    # key_err()
    # excep1()
    main()