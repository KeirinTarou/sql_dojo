import mysql.connector
import os
from sql_dojo.config import (
    DB_DRIVER, 
    DB_SERVER, 
    DB_PORT, 
    DB_DATABASE, 
    DB_USER, 
    DB_PASSWORD, 
)

def get_connection_string():
    return """
        DRIVER={MySQL ODBC 9.4 Unicode Driver};
        SERVER=localhost;
        PORT=3306;
        DATABASE=sampledb;
        UID=user;
        PWD=userpass;
        OPTION=3;
    """
    # return f"""
    #     DRIVER={{{ DB_DRIVER }}};
    #     SERVER={ DB_SERVER };
    #     PORT={ DB_PORT };
    #     DATABASE={ DB_DATABASE };
    #     UID={ DB_USER };
    #     PWD={ DB_PASSWORD };
    #     OPTION=3;
    # """
    # return f"""
    #     DRIVER={ os.getenv('DB_DRIVER') };
    #     SERVER={ os.getenv('DB_SERVER') };
    #     PORT={ os.getenv('DB_PORT') };
    #     DATABASE={ os.getenv('DB_DATABASE') };
    #     UID={ os.getenv('DB_USER') };
    #     PWD={ os.getenv('DB_PASSWORD') };
    #     OPTION=3;
    # """

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_SERVER"),     
        port=os.getenv("DB_PORT"), 
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASSWORD"), 
        database=os.getenv("DB_DATABASE"), 
    )
