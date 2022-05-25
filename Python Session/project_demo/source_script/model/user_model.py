

class UserModel:
    table_name = "users"

    def __init__(self,connection):
        self.conn = connection

    def create_user(self,data):
        sql = f"INSERT INTO {UserModel.table_name} (name,mobile,salary) VALUES {data}"
        self.conn.execute(sql)

    def get_users(self):
        user_data = []
        sql = "select * from users"
        data = self.conn.execute(sql)
        columns = data.keys()
        for r in data:
            row_data = dict(zip(columns,r))
            user_data.append(row_data)
        return user_data

"""
db,execute("DELETE FROM users WHERE id = 20")
db.execute ("UPDATE users SET name = "nanana" where id = 20")

"""