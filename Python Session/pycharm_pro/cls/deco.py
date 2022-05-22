
def decorate(func):
    print("func:",func)

    def wraper(num):
        print("in nump")
        print("rapper function")
        return func(num)

    return wraper



def get_data(num):
    """
    Adding list data
    :return:
    """
    l1 = [2,3,4,5,6]
    print("...Adding list....")
    l1.append(num)
    x = sum(l1)
    print("Sum:",x)
    return x



if __name__ =="__main__":
    wrapper = decorate(get_data)
    resp = wrapper(20)
    print("Resp",resp)