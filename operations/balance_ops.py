from database import get_db_connection

def set_initial_balance():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        print(f"Database Connection Successfully✅.")
        
        initial_balance = float(input("Enter Initial Balance: "))
        
        cursor.execute("INSERT INTO balance(BALANCE) VALUES(?)",(initial_balance,))
        
        conn.commit()
        
        
        print(f"Balance Set to: {initial_balance}")
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
    
def get_current_balance():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT BALANCE FROM balance ORDER BY ID DESC LIMIT 1")
        current_balance = cursor.fetchone()
        
        
        conn.close()
        
        return current_balance['BALANCE']

    except Exception as e:
        print(f"Error: {e}")
