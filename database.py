import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            description TEXT,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense(date, amount, description, category):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, amount, description, category) VALUES (?,?,?,?)",
              (date, amount, description, category))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    data = c.fetchall()
    conn.close()
    return data

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

def get_expense_by_id(expense_id):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expenses WHERE id=?", (expense_id,))
    row = c.fetchone()
    conn.close()
    return row

def update_expense(expense_id, date, amount, description, category):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("""
        UPDATE expenses 
        SET date=?, amount=?, description=?, category=? 
        WHERE id=?
    """, (date, amount, description, category, expense_id))
    conn.commit()
    conn.close()