from source_script.model.db_connection import DBConnection

from source_script.model.user_model import UserModel


class UserController:

    def __init__(self):
        pass

    def get_user_data(self):
        db_connection = DBConnection().get_connection()
        user_obj = UserModel(connection=db_connection)
        return user_obj.get_users()

    def add_user(self):

        db_obj = DBConnection()
        db_connection = db_obj.get_connection()
        data = ("Banana", "502033448", 50000)
        user_data = UserModel(connection=db_connection).create_user(data)
        print("db_obj11:", db_obj.conn)
        db_obj.close_connection()
        print("db_obj22:", db_obj.conn)
        return {"data": data, "status": 1, "msg": "User added successfully"}


if __name__ == "__main__":
    obj = UserController()
    print(obj.add_user())
