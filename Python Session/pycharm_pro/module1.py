#
import json
import datetime
import common_module

def get_resp():
    data = {
        "name" : "Ganga","city":"Delhi","role" : "admin"
    }
    return json.dumps(data)

def get_date():
    return datetime.date.today()


def main():
    resp = common_module.add_number(10,30)
    data = {"name":"Ganga","val":resp, "response_date" : common_module.resp_date()}
    return common_module.display_msg(data=data,msg="Fetch data successfully",status=1)


if __name__ == "__main__":
    # data = get_resp()
    # print(type(data))
    # print(type(get_date()))
    print(main())

