import sqlite3
import os

DB_PATH = "bot_users.db"

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                free_tips_used INTEGER DEFAULT 0,
                has_subscription BOOLEAN DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def create_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def increment_free_tips(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET free_tips_used = free_tips_used + 1 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
