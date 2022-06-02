import helper



def main():
    print("Program Started")
    data = {}
    a = input("Enter number1:")
    b = input("Enter number2:")
    add = helper.add(a,b)
    mul = helper.mul(b,a)
    data["first"] = add + mul

    resp = helper.mul(helper.add(a,b),a)
    data["resp"] = resp
    return data

if __name__ =="__main__":
    main()


