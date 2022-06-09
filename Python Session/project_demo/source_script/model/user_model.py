
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
        sql = f"INSERT INTO users(user_name, pwd,name,city,mobile, created_at) VALUES {tuple_data};"
        self.conn.execute(sql)

    def delete_user(self,user_name):
        sql = f"DELETE FROM users WHERE user_name ={user_name};"
        self.conn.execute(sql)

    def is_exist(self,username):
        sql = f"select * from users where user_name = '{username}'"
        data = self.conn.execute(sql)
        user = data.fetchone()
        if user:
            return True
        else:
            return False

    def _get_user(self, username):
        sql = f"select * from users where user_name = '{username}'"
        data = self.conn.execute(sql)
        user = data.fetchone()
        return user


    def load_data(self):
        import csv

        with open(FILE_PATH) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                self.create_user((row['name'],row['mobile'],row['salary'],row['created_at']))
               # self.create_user(tuple(row.values()))

        print("data Loaded successfully")




if __name__=="__main__":
    pass
