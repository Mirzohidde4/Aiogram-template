import sqlite3

def sql_connect():
    try:
        connection = sqlite3.connect(".../db.sqlite3")  # SQLite3 bazasiga bog'lanish
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def sql_connection():
    connection = sqlite3.connect(".../db.sqlite3")  # SQLite3 bazasiga bog'lanish
    connection.commit()
    return connection


def create_table():
    try:
        connection= sqlite3.connect('db.sqlite3')
        table = """ CREATE TABLE Products (
                    chat_id BIGINT NOT NULL ,
                    title TEXT NOT NULL,
                    image TEXT NOT NULL,
                    description TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    soni INTEGER PRIMARY KEY NOT NULL
                ); """
        cursor = connection.cursor()
        print("databaza yaratildi")
        cursor.execute(table)
        cursor.close()
    
    except sqlite3.Error as error:
        print("hatolik", error)
    finally:
        if connection:
            connection.close()    
            print("sqlite o'chdi")
# create_table()


def read_database(table):
    if not sql_connect():
        return False
    
    try:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        res = cursor.fetchall()

        return list(res) if res else False
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        conn.close()

    
def add_to_database(table, id1, id2, id3):
    if not sql_connect():
        return False

    try:
        conn = sql_connection()
        conn.execute(
            f"INSERT INTO {table} (id1, id2, id3) VALUES (?, ?, ?)",
            (table, id1, id2, id3),
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        conn.close()


def update_database(table, column, value, condition_column, condition_value):
    if not sql_connect():
        return False

    try:
        conn = sql_connection()
        conn.execute(
            f"UPDATE {table} SET {column} = ? WHERE {condition_column} = ?",
            (value, condition_value),
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        conn.close()


def delete_at_datebase(table, key, value):
    if not sql_connect():
        return False

    try:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE {key} = {value}")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def drop_table(table):
    if not sql_connect():
        return False

    try:
        conn = sql_connection()
        conn.execute(f"DROP TABLE IF EXISTS {table}")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        conn.close()
