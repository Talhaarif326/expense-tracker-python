from database import get_db_connection

def balance_check():
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT BALANCE FROM balance")
        result = cursor.fetchone()
        
        conn.close()
        
        return result is not None and result['BALANCE'] > 0 
            
    
    except Exception as e:
        print(f"Error: {e}")
    
    
def expense_check():
    try:
    
        conn = get_db_connection()
        cursor = conn.cursor()
            
        cursor.execute("SELECT * FROM EXPENSES")
        result = cursor.fetchall()
        
        conn.close()
        
        return result is not None
    
    except Exception as e:
        print("Error: {e}")