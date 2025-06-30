# database.py

import sqlite3

# Create connection to SQLite DB
def create_table():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviewtable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT,
            sentiment INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Insert review and sentiment
def insert_review(review, sentiment):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('INSERT INTO reviewtable (review, sentiment) VALUES (?, ?)', (review, sentiment))
    conn.commit()
    conn.close()

# View all reviews
def view_reviews():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reviewtable')
    data = c.fetchall()
    conn.close()
    return data
