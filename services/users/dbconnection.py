import psycopg2

def connect():
    connection = psycopg2.connect(
        host="users-db", port="5432",
        database="users", user="postgres",
        password = "postgres"
    )
    return connection

def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

def select_querry(cursor, querry: str, params: tuple):
    cursor.execute(querry, params)
    result = cursor.fetchall()
    return result

def insert_querry(cursor, querry: str, params: tuple):
    cursor.execute(querry, params)

