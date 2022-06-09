

if __name__ =="__main__":
    flag = input("Do you want to load DB Schema? yes/no:")
    if flag.lower() =='yes':
        from source_script.model.db_connection import DBConnection
        from source_script.model import db_schema
        conn = DBConnection().get_connection()
        db_schema.main(conn)
    else:
        print("Process cancelled")