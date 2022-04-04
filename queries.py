
import mysql.connector


config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "car_parking",
    "autocommit": True
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

except mysql.connector.Error as err:
    if err:
        print(err)


def login(username, password):

    query = f"SELECT * FROM `admin` WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    record = cursor.fetchall()
    return record


# users


def get_user_by_id(user_id: int):
    query = f"SELECT * FROM `admin` WHERE id = {user_id}"
    cursor.execute(query)
    record = cursor.fetchall()
    return record


def get_user_list():

    query = "SELECT * FROM `admin`"
    cursor.execute(query)
    record = cursor.fetchall()
    return record


def delete_user(user_id: int):
    query = f"DELETE FROM `admin` WHERE `admin`.`id` = {user_id}"
    cursor.execute(query)


def insert_user(fullname: str, username: str, password: str):

    query = f"INSERT INTO `admin` (`id`, `fullname`, `username`, `password`) VALUES (NULL, '{fullname}', '{username}', '{password}')"
    cursor.execute(query)
