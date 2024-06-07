import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='master',
        password='LpTraining',
        database='LP_Training',
        port=3306
    )