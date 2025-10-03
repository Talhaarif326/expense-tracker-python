from database import get_db_connection
from balance_ops import get_current_balance

def view_balance():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    balance = get_current_balance()
    
    conn.close()
    
    return f"Current Balance: {balance}"
