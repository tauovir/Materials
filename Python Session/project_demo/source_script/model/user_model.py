from source_script.model.db_connection import DBConnection

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
        sql = f"INSERT INTO public.users(name, mobile, salary, created_at) VALUES {tuple_data};"
        data = self.conn.execute(sql)
        return True





if __name__=="__main__":
    db_obj1 = DBConnection()
    conn = db_obj1.get_connection()
    obj = UserModel(connection=conn)
    user_list = obj.get_users()
    print(user_list)
