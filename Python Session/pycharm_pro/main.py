""

def list_for():
    list1 = []
    # for i in range(10):
    #     list1.append(i)

    # for item in ['name',"khan","orange"]:
    #     list1.append(item.upper())

    for x in range(1,13):
        if x%2 ==0 or x ==1:
            list1.append(x)
    list1 = []
    for x in "Technical":
        if x in "aeiou":
            list1.append('|')
        else:
            list1.append(x)
    # print("".join(list1))
    arr = [[1, 2, 3], [10, 20], [101, 102, 103]]
    a = []
    for row in arr:
        for ele in row:
            a.append(ele)

    print(a)


def list_comprehension():
    l1 = [x for x in range(10)]
    # print(l1)
    l2 = [x.upper() for x in ['name',"khan","orange"]]
    # print(l2)
    # sum1 = sum([int(x)+2 for x in [20,30,10,'5']])
    #
    # # if statements
    even_list = [x for x in range(1,13) if x%2==0 or x==1]
    # print(even_list)
    string1 = "Technical"
    # # if else statement
    a = "".join(['|' if ele in 'aeiou' else ele for ele in string1])
    # print(a)
    # multifor statement
    arr = [[1,2,3],[10,20],[101,102,103]]
    a1 = [n for ele in arr for n in ele]


def matrix():
    """
    [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]

    :return:
    """
    list1 = [[x for x in range(5)] for _ in range(5)]
    # print(list1)
    l2 = [a+b for a in [1,2,3] for b in [3,4,5]]
    print("l2:",l2)
    l3 = []
    for a in [1,2,3]:
        for b in [3,4,5]:
            l3.append(a+b)

    l4 = [[a+b for a in [1,2,3]] for b in [3,4,5]]
    print("l3",l3)
    print("l4",l4)
    l5 = []
    for a in [1,2,3]:
        x = []
        for b in [3,4,5]:
            x.append(a+b)
        l5.append(x)
    print("l5",l5)

def dict_comp():
    data = [
        {"name" : "khan","price" : 20},
        {"name": "amit", "price": 20},
    ]
    d1 = {'a':10,"b":20,"c":30,"d":40}
    d2 = {key:val**2 for key,val in d1.items()}
    d2 = {key: val ** 2 for key, val in d1.items() if val > 20}
    lis2 = [{"name" : item['name'].upper(),"price" : item['price'] + 10} for item in data]
    print(lis2)

def set_compre():
    l1 = [20,30,1,2,4,20,30,1,6]
    l2 = {ele + 20 for ele in l1 if ele > 2}
    print(l2)



if __name__ == "__main__":
    # list_comprehension()
    # list_for()
    # dict_comp()
    # set_compre()
    # matrix()
    dict_comp()

