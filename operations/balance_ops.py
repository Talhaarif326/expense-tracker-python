from database import get_db_connection
from decimal import Decimal

def set_initial_balance():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print(f"Database Connection Successfully✅.")
    
    initial_balance = Decimal(input("Enter Initial Balance: "))
    
    cursor.execute("INSERT INTO balance(BALANCE) VALUES(?)",(initial_balance,))
    
    print(f"Balance Set to: {initial_balance}")
    
    
def get_current_balance():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT BALANCE FROM balance ORDER BY ID DESC LIMIT 1")
    current_balance = cursor.fetchone()
    
    
    conn.close()
    
    return current_balance['BALANCE']



def update_balance(new_balance):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE balance SET BALANCE = ? WHERE ID= 1",(new_balance,))
    
    print(f"Balance Update successfully✅") 
    
    conn.commit()
    conn.close()       