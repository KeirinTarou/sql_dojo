# import mysql.connector
import pyodbc
import os
from pathlib import Path

def get_connection_string():
    if os.getenv("USE_ODBC") == "USE_MYSQL":
        return (
            f"DRIVER={ os.getenv("MYSQL_DB_DRIVER") };"
            f"SERVER={ os.getenv('MYSQL_DB_SERVER') };"
            f"PORT={ os.getenv('MYSQL_DB_PORT') };"
            f"DATABASE={ os.getenv('MYSQL_DB_DATABASE') };"
            f"UID={ os.getenv('MYSQL_DB_USER') };"
            f"PWD={ os.getenv('MYSQL_DB_PASSWORD') };"
            "OPTION=3;"
        )
    elif os.getenv("USE_ODBC") == "USE_SQLITE":
        DB_PATH = Path(__file__).parent / os.getenv("SQLITE_DB_NAME")
        return (
            f"DRIVER={ os.getenv("SQLITE_DB_DRIVER") };"
            f"DATABASE={ DB_PATH };"
        )

def get_connection():
    """`pyodbc.Connection`インスタンスを返す
    """
    print(get_connection_string())
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
