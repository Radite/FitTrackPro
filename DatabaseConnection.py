import mysql.connector
from mysql.connector import Error

# Database connection function
def connect_to_database(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except Error as e:
        print("Database connection error:", e)
        return None

# Execute an SQL query with parameters
def execute_query(conn, query, params=None):
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor
    except Error as e:
        print("Query execution error:", e)
        return None

# Close the database connection
def close_connection(conn):
    if conn:
        conn.close()
