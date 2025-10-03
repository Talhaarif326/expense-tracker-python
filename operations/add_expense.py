from database import get_db_connection
from decimal import Decimal

def add_expense():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        print("Database Connection Establish ✅✅")
        
        expense_amount = Decimal(input("Enter Expense Amount: "))
        expense_category = input("Enter Expense Category: ")
        expense_description = input("Enter Expense Detail: ")
        
        cursor.execute("INSERT INTO EXPENSES(AMOUNT, CATEGORY, DESCRIPTION) VALUES(?,?,?)",(expense_amount, expense_category,expense_description))
        
        print(f"Expense Add Successfully ✅.")
        
        conn.commit()
        conn.close()
    
    except Exception as e:
        print(f"Error: {e}")