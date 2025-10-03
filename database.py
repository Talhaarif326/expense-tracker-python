import sqlite3

def get_db_connection():  # making a connection with the database
    """
    Create and Return Database Connection
    """
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row   # This allows us to access columns by name
    return conn

def database():
    """
    Initializing the database and Creating the required Table
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXIST balance(
            ID INTEGER PRIMARY KEY,
            BALANCE INTEGER REAL DEFAULT=0,
            LAST UPDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS EXPENSES(
            ID INTEGER PRIMARY KEY,
            AMOUNT REAL NOT NULL,
            CATEGORY TEXT NOT NULL,
            DESCRIPTION TEXT,
            EXPENSE_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            
        )
        """
        )
    
    conn.commit()
    conn.close()
    
    print("Database initialized successfully ✅✅")