
import sys

print(sys.path)

import test
from source_script.model import users




def show():
    print("Show user table")
    print(test.Test)
    print(users.Table)


show()