from database import get_db_connection
from utils.validators import expense_check
from tabulate import tabulate

def view_expenses():
    try:
        if not expense_check():
            print("No Expenses")
            return
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM EXPENSES")
        
        result = cursor.fetchall()
        
        print(tabulate(result, headers=["ID", "AMOUNT", "CATEGORY", "DESCRIPTION", "DATE"]))
        conn.close()
    
    except Exception as e:
        print(f"Error: {e}")