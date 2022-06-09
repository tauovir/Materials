from source_script.model.db_connection import DBConnection
import hashlib, uuid
import datetime as dt
from source_script.configuration.config import IS_POSTGRES_DB

def sqlite_user_schema():
    sql = """
        CREATE TABLE IF NOT EXISTS "users" (
    	"id"	INTEGER,
    	"user_name"  TEXT,
    	"pwd"   TEXT,
    	"name"	TEXT,
    	"city"	INTEGER,
    	"mobile"	TEXT,
    	"created_at"	TEXT,
    	PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
    return sql

def sqlite_address_schema():
    sql = """
    CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"user_id"  INTEGER,
	"addr"   TEXT,
	"city"	TEXT,
	"city"	INTEGER,
	"country"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    return sql


def user_schema():

    user_tbl = """
    CREATE TABLE IF NOT EXISTS public.users
    (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
	 pwd character varying(250) COLLATE pg_catalog."default" NOT NULL,
    name character varying(100) COLLATE pg_catalog."default",
    city character varying(50) COLLATE pg_catalog."default",
    mobile character varying(15) COLLATE pg_catalog."default",
    created_at date,
    CONSTRAINT user_pkey PRIMARY KEY (id)
    )
    """
    return user_tbl

def address_schema():
    addr_tbl = """
    CREATE TABLE IF NOT EXISTS public.address
    (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer,
    addr character varying(200) COLLATE pg_catalog."default",
    city character varying(100) COLLATE pg_catalog."default",
    country character varying(100) COLLATE pg_catalog."default"
    )
    """
    return addr_tbl

def create_admin(conn):

    print("Create Super admin")
    user_name = input("Enter your username:")
    name = input("Enter your name:")
    pwd = input("Enter password:")
    city = input("Enter city:")
    mobile = input("Enter your mobile:")
    hash_pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    create_at = dt.datetime.today().strftime("%Y-%m-%d")
    tpl = (user_name, hash_pwd, name, city, mobile, create_at)
    sql = f"INSERT INTO users(user_name, pwd,name,city,mobile, created_at) VALUES {tpl};"
    conn.execute(sql)
    print("Admin created successfully")

def main(conn):
    """
    creat tables
    :return:
    """
    if IS_POSTGRES_DB:
        schemas = [user_schema,address_schema]
    else:
        schemas = [sqlite_user_schema, sqlite_address_schema]
    for func in schemas:
        ddl = func()
        conn.execute(ddl)

    print("Database Schema loaded Successfully")
    create_admin(conn)



if __name__ =="__main__":
    db_obj1 = DBConnection()
    conn = db_obj1.get_connection()
    main(conn)
