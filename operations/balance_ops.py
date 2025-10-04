from database import get_db_connection
from tabulate import tabulate

def set_initial_balance():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        print(f"Database Connection Successfully✅.")
        
        initial_balance = float(input("Enter Initial Balance: "))
        
        cursor.execute("INSERT INTO balance(BALANCE) VALUES(?)",(initial_balance,))
        
        conn.commit()
        
        
        print(tabulate([[initial_balance]], headers=["Balance"]))
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
    
def get_current_balance():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT BALANCE FROM balance ORDER BY ID DESC LIMIT 1")
        result = cursor.fetchone()
        current_balance = result['BALANCE']
        
        conn.close()
        
        return tabulate([[current_balance]], headers=["Balance"])

    except Exception as e:
        print(f"Error: {e}")
