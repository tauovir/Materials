from source_script.model.db_connection import DBConnection


def user_schema():


    user_tbl = """
    CREATE TABLE IF NOT EXISTS public.users
    (
        id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
        name character varying(100) COLLATE pg_catalog."default",
        mobile character varying(20) COLLATE pg_catalog."default",
        salary integer,
        created_at date
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

def main(conn):
    """
    creat tables
    :return:
    """
    schemas = [user_schema,address_schema]
    for func in schemas:
        ddl = func()
        conn.execute(ddl)

    print("====DB schema Created Successfully===")


if __name__ =="__main__":
    db_obj1 = DBConnection()
    conn = db_obj1.get_connection()
    main(conn)
