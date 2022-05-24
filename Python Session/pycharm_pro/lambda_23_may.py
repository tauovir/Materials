
def multi(x,y):
    print("Common function")
    return x*y

def my_func():
    lamd1 = lambda x,y : x * y
    print(lamd1(20,30))

def my_func2():

    lamb2 = lambda *args : sum(args)
    print(lamb2(20,30,100))



def filter_list():

    l1 = [10,2,50,20,30,44,3,25]
    filter_obj = filter(lambda x : x > 20,l1)
    print("I am in filter function")
    print(list(filter_obj))
    new_list = list(filter(lambda x: x%2==0, l1))
    print("Even number")
    print(new_list)

def map_func():
    print(" I am in Map funxtion")
    l1 = [10, 2, 50, 20, 30, 44, 3, 25,0]
    new_list = map(lambda x : x +2,l1)

    # new_list_f = list(filter(lambda x: False, l1))
    # new_list_m = list(map(lambda x: 5, l1))
    # print(new_list_f)
    # print(new_list_m)
    l2 = [11, 22, 50, 20]
    new_map =list(map(lambda x,y:x+y,l1,l2))
    print(new_map)




#====================================
# my_func()
# print(multi(20,30))
# my_func2()
# filter_list()
map_func()
