from database import get_db_connection

def view_expenses():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM EXPENSES")
    
    result = cursor.fetchall()
    
    conn.close()
    
    return result