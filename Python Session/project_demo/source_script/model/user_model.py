from source_script.model.db_connection import DBConnection,SQLLiteConnection
from source_script.configuration.config import FILE_PATH

class UserModel:

    table_name = "users"

    def __init__(self,connection):
        self.conn = connection


    def get_users(self):

        user_data = []
        sql = "select * from users"
        data = self.conn.execute(sql)
        columns = data.keys()
        for r in data:
            row_data = dict(zip(columns,r))
            user_data.append(row_data)
        return user_data

    def create_user(self,tuple_data):

        sql = f"INSERT INTO users(name, mobile, salary, created_at) VALUES {tuple_data};"
        self.conn.execute(sql)

    def load_data(self):
        import csv

        with open(FILE_PATH) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                self.create_user((row['name'],row['mobile'],row['salary'],row['created_at']))
               # self.create_user(tuple(row.values()))

        print("data Loaded successfully")




if __name__=="__main__":
    import datetime as dt
    data = ("Ganga", "1509870", 30000, dt.datetime.today().strftime("%Y-%m-%d"))
    db_obj1 = DBConnection()
    # db_obj1 = SQLLiteConnection()
    conn = db_obj1.get_connection()
    obj = UserModel(connection=conn)
    # user_list = obj.get_users()
    # obj.create_user(data)
    # user_list = obj.get_users()
    # print(user_list)
    #===========
    obj.load_data()
