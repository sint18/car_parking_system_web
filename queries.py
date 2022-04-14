
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
    record = cursor.fetchone()
    return record

# dashboard


def custom_query(query: str):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def count_parked_vehicles():
    query = "SELECT COUNT(*) FROM `vehicle_info` WHERE out_time IS NULL AND fees IS NULL"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result


def count_categories():
    query = "SELECT COUNT(*) FROM category"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result


def count_history():
    query = "SELECT COUNT(*) FROM vehicle_info WHERE out_time IS NOT NULL AND fees IS NOT NULL"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result


def count_over_parked(limit: str):
    query = f"SELECT COUNT(id) FROM `vehicle_info` WHERE TIMEDIFF(NOW(), in_time) > TIME('{limit}') AND out_time IS NULL"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result

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


def update_user_status(user_id: int, status: str):
    query = f"UPDATE `admin` SET `status` = '{status}' WHERE `admin`.`id` = {user_id}"
    cursor.execute(query)


# vehicles


def get_vehicle_history():
    query = "SELECT vehicle_info.id, vehicle_info.plate_number, category.category_name, vehicle_info.in_time, vehicle_info.out_time, vehicle_info.fees, vehicle_info.total_hours FROM `vehicle_info` INNER JOIN category ON vehicle_info.category_id = category.id WHERE vehicle_info.fees IS NOT NULL AND vehicle_info.out_time is NOT NULL ORDER BY `id` DESC"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


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


def get_vehicle_info_by_id(v_id: int):
    query = f"SELECT vehicle_info.id, vehicle_info.plate_number, category.category_name, vehicle_info.in_time, vehicle_info.out_time, vehicle_info.fees, vehicle_info.total_hours, vehicle_info.fined FROM `vehicle_info` INNER JOIN category ON vehicle_info.category_id = category.id WHERE vehicle_info.id = {v_id}"
    cursor.execute(query)
    record = cursor.fetchone()
    return record


def insert_vehicles(cat_id: int, reg_num: str):
    query = f"INSERT INTO `vehicle_info` (`id`, `category_id`, `plate_number`, `in_time`, `out_time`, `fees`, `total_hours`) VALUES (NULL, '{cat_id}', '{reg_num}', NOW(), NULL, NULL, NULL)"
    cursor.execute(query)


def update_vehicle(v_id: int, out_time, fees, total_hours, fine):
    query = f"UPDATE `vehicle_info` SET `out_time` = '{out_time}', `fees` = '{fees}', `total_hours` = '{total_hours}', `fined` = '{fine}' WHERE `vehicle_info`.`id` = {v_id}"
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


# members

def get_member_info_by_id(plate_number):
    query = f"""SELECT members.member_id, members.plate_number, members.status,
    membership_tier.discount, membership_tier.tier, membership_tier.cost, 
    membership.start_date, membership.valid_until FROM membership 
    INNER JOIN members ON members.member_id = membership.member_id 
    INNER JOIN membership_tier ON membership.tier_id = membership_tier.id 
    WHERE members.plate_number = '{plate_number}' 
    ORDER BY membership.start_date DESC LIMIT 1"""
    cursor.execute(query)
    record = cursor.fetchone()
    return record


def get_members():
    query = "SELECT * FROM members"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def get_tiers():
    query = "SELECT * FROM membership_tier"
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def get_tier_by_id(t_id: int):
    query = f"SELECT * FROM membership_tier WHERE id = {t_id}"
    cursor.execute(query)
    record = cursor.fetchone()
    return record


def extend_member(member_id, tier_id, start_date, valid_until):
    query = f"INSERT INTO `membership` (`id`, `member_id`, `tier_id`, `start_date`, `valid_until`) VALUES (NULL, '{member_id}', '{tier_id}', '{start_date}', '{valid_until}')"
    cursor.execute(query)


def update_status(member_id):
    query = f"SELECT * FROM `membership` WHERE member_id = {member_id}"
    cursor.execute(query)
    records = cursor.fetchall()

    if not records or not is_valid(member_id):
        query1 = f"UPDATE `members` SET `status` = 'inactive' WHERE `members`.`member_id` = {member_id}"
        cursor.execute(query1)
    elif is_valid(member_id):
        query1 = f"UPDATE `members` SET `status` = 'active' WHERE `members`.`member_id` = {member_id}"
        cursor.execute(query1)


def is_valid(member_id):
    query = f"SELECT * FROM `membership` WHERE member_id = {member_id} AND start_date <= NOW() AND valid_until >= NOW()"
    cursor.execute(query)
    records = cursor.fetchall()
    if records:
        return True
    return False


def register_member(reg_no, tier_id, start_date, valid_until):
    query1 = f"INSERT INTO `members` (`member_id`, `plate_number`, `status`) VALUES (NULL, '{reg_no}', 'active')"
    cursor.execute(query1)

    query2 = f"SELECT * FROM `members` WHERE plate_number = '{reg_no}'"
    cursor.execute(query2)
    member_id = cursor.fetchone()[0]

    query3 = f"INSERT INTO `membership` (`id`, `member_id`, `tier_id`, `start_date`, `valid_until`) VALUES (NULL, '{member_id}', '{tier_id}', '{start_date}', '{valid_until}')"
    cursor.execute(query3)


def revoke_membership(m_id: int):
    query = f"UPDATE `membership` SET `valid_until` = NOW() WHERE `membership`.`id` = {m_id}"
    cursor.execute(query)


def get_member_info(member_id: int):
    query = f"SELECT * FROM membership INNER JOIN membership_tier ON membership_tier.id = membership.tier_id WHERE member_id = {member_id}"
    cursor.execute(query)
    records = cursor.fetchall()
    return records
