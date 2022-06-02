

def _calc(val):
    return (10+val)

def test_debug2():
    print("=====Program Started=========")
    l1 = [10,20,1,2,3,4]
    for ele in l1:
        c = _calc(ele)
        print(c)

def test_debug():
    print("=====Program Started=========")
    l1 = [10,20,1,2,3,4]
    for ele in l1:
        c = 10 + ele
        print(c)


test_debug2()