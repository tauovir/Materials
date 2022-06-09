
from source_script.model.db_connection import DBConnection
from source_script.model.user_model import UserModel
import pandas as pd
import hashlib, uuid
import datetime as dt
import os
from source_script.configuration.config import FOLDER_PATH


class MainProgram:

    def __init__(self):
        db_obj1 = DBConnection()
        self.conn = db_obj1.get_connection()
        self.user_obj = UserModel(self.conn)

    def __get_hash_pwd(self, password):

        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed

    def login(self, username, password):

        user = self.user_obj._get_user(username=username)
        if not user:
            print(f" User name {username} does not exist")
        else:
            if self.__get_hash_pwd(password) == user.pwd:
                self.display_menu()
            else:
                print("In correct user name and password")

    def check_username(self):
        flag = True
        while flag:
            user_name = input("Enter username:")
            flag = self.user_obj.is_exist(user_name)
            if flag == False:
                return user_name
            else:
                print("User name already exist.Please enter unique user name")
                self.check_username()

    def get_user(self):
        users = self.user_obj.get_users()
        data_frame = pd.DataFrame(users)
        data_frame.drop(['pwd'], inplace=True, axis=1)
        print(data_frame.head(10))

    def add_new_user(self):

        user_name = self.check_username()
        name = input("Enter your name:")
        pwd = input("Enter password:")
        city = input("Enter city:")
        mobile = input("Enter your mobile:")
        hash_pwd = self.__get_hash_pwd(pwd)
        print("hash_pwd:", hash_pwd)
        create_at = dt.datetime.today().strftime("%Y-%m-%d")
        tpl = (user_name, hash_pwd, name, city, mobile, create_at)
        self.user_obj.create_user(tpl)
        os.system('cls')
        print("User user added successfully")

    def remove_user(self):
        name = input("Enter username to delete:")
        if self.user_obj.is_exist(name):
            self.user_obj.create_user(name)
        else:
            print(f"Username:{name} does not exist in our database")

    def export_user(self):

        users = self.user_obj.get_users()
        data_frame = pd.DataFrame(users)
        data_frame.drop(['pwd'], inplace=True,axis=1)
        create_at = dt.datetime.today().strftime("%Y-%m-%d")
        filepath = FOLDER_PATH + create_at + ".csv"
        try:
            data_frame.to_csv(filepath)
        except Exception as e:
            print("Exception Occured:", e)
        else:
            print("Data exported successfully")

    def invoke_methods(self, choice):
        if choice == 1:
            self.get_user()
        elif choice == 2:
            self.add_new_user()
        elif choice == 3:
            self.remove_user()
        elif choice == 4:
            self.export_user()
        else:
            print("invalid input")

    def display_menu(self):

        flag = True
        os.system('cls')
        while flag:

            print("\n\t==================WELCOME TO MAIN MENU===============\n")
            print("\tEnter 1 to get all users:")
            print("\tEnter 2 to add new user:")
            print("\tEnter 3 to delete user:")
            print("\tEnter 4 export all users in csv file:")
            print("\tEnter -1 to exit from Program:")
            choice = input("\tEnter your choice:")
            choice = int(choice)
            if choice == -1:
                print("============Good Bye==============")
                break
            else:
                obj.invoke_methods(choice)


if __name__ == "__main__":
    flag = True
    obj = MainProgram()
    print("=============Login Page===================\n")
    username = input("Enter username:")
    pwd = input("Enter Password:")
    obj.login(username, pwd)

