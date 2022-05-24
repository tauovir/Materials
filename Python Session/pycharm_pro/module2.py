
import sys
print(sys.path)
# sys.path.append(r'C:\Users\LENOVO\Desktop\zee')
# print(sys.path)
from common_module import add_number,resp_date
from constant import *
import configuration as cfg
def main():
    print(add_number(20,30))
    print(resp_date())
    print(ACTIVE)
    print(INACTIVE)
    print(cfg.CONFIG_STATUS)
    print(cfg.load_configuration())


if __name__ == "__main__":
    main()

