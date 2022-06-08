from source_script.model import db_schema
from source_script.model.db_connection import DBConnection
from  source_script.model.user_model import UserModel
import pandas as pd
import hashlib, uuid
import datetime as dt
class MainProgram:

    def __init__(self):
        db_obj1 = DBConnection()
        self.conn = db_obj1.get_connection()
        self.user_obj = UserModel(self.conn)

    def __get_hash_pwd(self,password):

        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return hashed_password

    def login(self,username,password):
        user = self.user_obj._get_user(username = username)
        if not user:
            print(f" User name {username} does not exist")
        else:
            print(password)
            hash_pwd = self.__get_hash_pwd(password)
            print(user.pwd)
            print(hash_pwd)



    def check_username(self):
        flag = True
        while flag:
            user_name = input("Enter username:")
            flag = self.user_obj.is_exist(user_name)
            if flag== False:
                return user_name
            else:
                print("User name already exist.Please enter unique user name")
                self.check_username()



    def get_user(self):
        users = self.user_obj.get_users()
        data_frame = pd.DataFrame(users)
        print(data_frame.head(10))

    def add_new_user(self):

        user_name = self.check_username()
        name = input("Enter your name:")
        pwd = input("Enter password:")
        city = input("Enter city:")
        mobile = input("Enter your mobile:")
        hash_pwd = self.__get_hash_pwd(pwd)
        print("hash_pwd:",hash_pwd)
        create_at = dt.datetime.today().strftime("%Y-%m-%d")
        tpl = (user_name,hash_pwd,name,city,mobile,create_at)
        self.user_obj.create_user(tpl)
        print("User user added successfully")




    def invoke_methods(self,choice):
        if choice==1:
            self.get_user()
        elif choice==2:
            self.add_new_user()
        else:
            print("invalid input")

if __name__ == "__main__":
    flag = True
    obj = MainProgram()
    obj.login(username='orange101',password='khan102030')
    # while flag:
    #     print("Enter 1 to get all users:")
    #     print("Enter 2 to add user:")
    #     print("Enter 99 to exit from Program:")
    #     choice = input("Enter your choice:")
    #     choice = int(choice)
    #     if choice ==99:
    #         print("Good Bye...")
    #         break
    #     else:
    #         obj.invoke_methods(choice)









