import sqlite3
from datetime import datetime

# SQLite bazasiga ulanish
def create_connection():
    return sqlite3.connect('database.db')

# User jadvalini yaratish
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Jadvalni yaratish
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
     # number jadvalini yaratish
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS number (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phoneNumber TEXT NOT NULL,
        voteDate TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

# Foydalanuvchini jadvalga qo'shish
def insert_user(first_name, last_name, username, tg_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Foydalanuvchini qo'shish
    cursor.execute("""
    INSERT INTO user (first_name, last_name, username, tg_id)
    VALUES (?, ?, ?, ?)
    """, (first_name, last_name, username, tg_id))
    
    conn.commit()
    conn.close()
def insert_number(phone_number, vote_date):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Yangi yozuv qo'shish
    cursor.execute("""
    INSERT INTO number (phoneNumber, voteDate)
    VALUES (?, ?)
    """, (phone_number, vote_date))
    
    conn.commit()
    conn.close()


def has_user(tg_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user WHERE tg_id = ?", (tg_id,))
    user = cursor.fetchone()
    
    conn.close()
    
    return user is not None
# Foydalanuvchilarni olish
def get_users():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    
    conn.close()
    
    return users
def get_numbers()->list:
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM number")
    numbers = cursor.fetchall()
    
    conn.close()
    
    return numbers
def search_number(phone_number)->list:
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM number WHERE phoneNumber LIKE '%{phone_number}'")
    numbers = cursor.fetchall()
    
    conn.close()
    
    return numbers

# Dastlabki sozlamalar
create_table()

# Foydalanuvchi qo'shish misoli

if __name__ == '__main__':
    insert_user("John", "Doe", "johndoe","123456")
    insert_user("Jane", "Smith", "janesmith","654321")
    users = get_users()
    for user in users:
        print(user)
    insert_number("**-*65-98-99","2025-08-22 08:23")
    insert_number("**-*21-14-97","2025-08-22 08:23")
    numbers = get_numbers()
    for number in numbers:
        print(number)
    print(search_number("7890"))

