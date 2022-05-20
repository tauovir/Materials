




def list_loop():
    print("==Using for loop====")
    # new_list = []
    # for x in range(10):
    #     new_list.append(x)
    # print(new_list)

    # even_list = []
    # for x in range(1,21):
    #     if x%2 == 0 and x!=2:
    #         even_list.append(x)
    # print(even_list)
    new_l1 = []
    # [1,2,3,20,30,50,51,52,53]
    list1 = [[1, 2, 3], [20, 30, 50], [51, 52, 53]]
    for row in list1:
        new_l1 += row


    print(new_l1)


def list_compre():

    print("Using list comprehension====")
    # simple list comprehension
    new_list = [x for x in range(10)]
    even_list = [x for x in range(1,21) if x%2 ==0 and x!=2]

    name = "technical"  # t|chn|c|l   ->>|
    str1 = "".join(['|' if x in 'aeiou' else x for x in name ])

    # [1,2,3,20,30,50,51,52,53]
    # new_list2 = [n for ele in list1 for n in ele]
    # print(new_list2)

def set_compre():
    print("Set comprehension")
    l1 = [1,2,3,10,20,30,1,2,3]

    st1 = {x * 20 for x in l1}
    print(st1)

def dict_compre():
    d1 = {"name":"banana","price":20}
    d2 = {key:val for key,val in d1.items()}



def manipulate_data():
    price = 50
    data = [

        {"name": "banana", "price": 25}, # item
        {"name": "date", "price": 15}, # item
        {"name": "orange", "price": 10}, # item
        {"name": "pineapple", "price": 2}, # item
    ]
    """
    new_data = [
    {"name" : "MANGO","price":20 +20},
     {"name" : "BANANA","price":25+20},
    
    ]
    """
    new_data = [{"name" : item['name'].upper(),"price" : item['price'] + price} for item in data]
    print(new_data)









# list_loop()
# list_compre()
# set_compre()
# dict_compre()
set_compre()