from source_script.model.db_connection import DBConnection
from source_script.model.db_connection import SQLLiteConnection
from source_script.model.user_model import UserModel
import datetime as dt

class UserController:

    def __init__(self):
        pass

    def _get_date(self):
        return dt.datetime.today().strftime("%Y-%m-%d")

    def get_user_data(self):
        db_obj = DBConnection()
        db_connection = db_obj.get_connection()
        user_obj = UserModel(connection=db_connection)
        return user_obj.get_users()

    def add_user(self):

        db_obj = DBConnection()
        db_connection = db_obj.get_connection()
        data = ("hatim", "50209999", 26999,self._get_date())
        user_data = UserModel(connection=db_connection).create_user(data)

        db_obj.close_connection()

        return {"data": data, "status": 1, "msg": "User added successfully"}



    def add_user_from_csv(self):

        db_obj = DBConnection()
        user_data = self.read_csv_dict()
        db_connection = db_obj.get_connection()
        for row in user_data:
            data = (row['name'],row['mobile'],row['salary'],row['created_at'])
            UserModel(connection=db_connection).create_user(data)
        new_data = self.get_user_data()
        db_obj.close_connection()

        return {"data": new_data, "status": 1, "msg": "User added successfully"}

    def read_csv_dict(self):
        import csv
        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\write_users.csv"
        user_data = []
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader:
                user_data.append(row)
            return user_data

if __name__ == "__main__":
    print(UserController().add_user_from_csv())
    # obj = UserController()
    # obj.add_user()
    # print(obj.get_user_data())
