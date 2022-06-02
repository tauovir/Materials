from source_script.practice import helper
def test_debug():
    print("Program started.......")
    x = 10
    y = 25
    z = x +y
    m1 = x*y
    print("z:",z)
    print("m1:",m1)


def test_debug2():
    print("===Program started=====")
    result = []
    l1 = [10,20,30,40,50]
    for ele in l1:
        c = 10 + ele
        result.append(c)
    print("Result:",result)

    print("Program Ended....")

def test_debug3():
    print("Program started...")
    l1 = [1,2,3,4]
    resp = {"add":0,"mul":0,"total" : 0}
    for ele in l1:
        addi = helper.add(ele,10)
        mul1 = helper.mul(ele,5)
        resp['add'] = addi
        resp['mul'] = mul1
        resp['total'] = addi + mul1
        mix = helper.add(helper.mul(ele,5),6)

        print("resp:",resp)
        print("Program endedd")



test_debug3()
