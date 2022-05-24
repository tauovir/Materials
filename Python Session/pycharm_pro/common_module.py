import json
import datetime

def add_number(x,y):
    return x+y

def resp_date():

    format = "%Y-%m-%d"
    return datetime.date.today().strftime(format)


def display_msg(data = [],msg = "success",status = 1):

    data = {
        "data" : data,
        "msg" : msg,
        "status" : status
    }
    return json.dumps(data)


def _main():
    print(resp_date())


print("common_module_name:",__name__)
if __name__ == "__main__":
    _main()
    print("Sucessfull")
