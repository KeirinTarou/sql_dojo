# import mysql.connector
import pyodbc
import os

def get_connection_string():
    return (
        f"DRIVER={ os.getenv("DB_DRIVER") };"
        f"SERVER={ os.getenv('DB_SERVER') };"
        f"PORT={ os.getenv('DB_PORT') };"
        f"DATABASE={ os.getenv('DB_DATABASE') };"
        f"UID={ os.getenv('DB_USER') };"
        f"PWD={ os.getenv('DB_PASSWORD') };"
        "OPTION=3;"
    )

def get_connection():
    """`pyodbc.Connection`インスタンスを返す
    """
    return pyodbc.connect(get_connection_string())

# mysql.connector版
# def get_connection():
#     return mysql.connector.connect(
#         host=os.getenv("DB_SERVER"),     
#         port=os.getenv("DB_PORT"), 
#         user=os.getenv("DB_USER"), 
#         password=os.getenv("DB_PASSWORD"), 
#         database=os.getenv("DB_DATABASE"), 
#     )
