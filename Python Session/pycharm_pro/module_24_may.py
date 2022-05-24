
import json
import datetime
import common_module
from common_module import display_msg,add_two_num
from constant import INACTIVE,ACTIVE

# from controller.test_controller import test_list
from controller import test_controller

def display():
    print("I am display")
    data = [
        {"name" : "rahul","city" : "Meerut","age" : 25},
        {"name": "amit", "city": "Kanpur", "age" : 20}
    ]
    # return data
    return json.dumps(data)

def get_date():
    today_date = datetime.date.today()
    return today_date



def main():
    x = add_two_num(10,20)
    print(ACTIVE)
    print(INACTIVE)
    # y = common_module.sub_two_num(50,30)
    data = [
        {"name": "rahul", "city": "Meerut", "age": 25},
        {"name": "amit", "city": "Kanpur", "age": 20}
    ]
    resp = display_msg(data = data,msg=" data loaded successfully",status=99)
    print(resp)
    print("test_list:",test_controller.test_list())


print("module24:",__name__)
#
if __name__ == "__main__":
    main()