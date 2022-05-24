
from controller import test_controller
from api.api_constant import API
def display_msg():
    print("Display message")
    print("test_list:", test_controller.test_list())
    print(API)



if __name__ =="__main__":
    display_msg()