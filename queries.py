
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


def update_user(user_id: int, fullname: str, username: str, new_password=""):

    if new_password:
        query = f"UPDATE `admin` SET `fullname` = '{fullname}', `username` = '{username}', `password` = '{new_password}' WHERE `admin`.`id` = {user_id}"
    else:
        query = f"UPDATE `admin` SET `fullname` = '{fullname}', `username` = '{username}' WHERE `admin`.`id` = {user_id}"

    cursor.execute(query)

# vehicles


def get_parked_vehicles():
    query = "SELECT vehicle_info.id, category.category_name, vehicle_info.plate_number, vehicle_info.in_time, TIMEDIFF(now(), vehicle_info.in_time) AS parked_hours FROM vehicle_info INNER JOIN category ON vehicle_info.category_id=category.id WHERE vehicle_info.out_time IS NULL"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def get_parked_vehicles_by_id(v_id: int):
    query = f"SELECT vehicle_info.id, category.category_name, vehicle_info.plate_number, vehicle_info.in_time, NOW() AS exit_time, TIMEDIFF(now(), vehicle_info.in_time) AS parked_hours FROM vehicle_info INNER JOIN category ON vehicle_info.category_id=category.id WHERE vehicle_info.out_time IS NULL AND vehicle_info.id={v_id}"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def insert_vehicles(cat_id: int, reg_num: str):
    query = f"INSERT INTO `vehicle_info` (`id`, `category_id`, `plate_number`, `in_time`, `out_time`, `fees`, `total_hours`) VALUES (NULL, '{cat_id}', '{reg_num}', NOW(), NULL, NULL, NULL)"
    cursor.execute(query)


# category

def get_categories():
    query = "SELECT * FROM category"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def get_category_by_id(c_id: int):
    query = f"SELECT * FROM category WHERE `id` = {c_id}"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def insert_category(name: str, desc: str):
    query = f"INSERT INTO `category` (`id`, `category_name`, `description`, `creationDate`) VALUES (NULL, '{name}', '{desc}', NOW())"
    cursor.execute(query)


def update_category(c_id: int, name: str, desc: str):
    query = f"UPDATE `category` SET `category_name` = '{name}', `description` = '{desc}' WHERE `category`.`id` = {c_id}"
    cursor.execute(query)


def delete_category(c_id: int):
    query = f"DELETE FROM `category` WHERE `category`.`id` = {c_id}"
    cursor.execute(query)
