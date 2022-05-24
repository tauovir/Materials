

print("common_module_name:",__name__)

def add_two_num(a,b):
    return a+b



def sub_two_num(a,b):
    return a-b


def display_msg(data = [],msg = "success",status = 1):

    return {
        "data" : data,
        "msg" : msg,
        "status" : status
    }