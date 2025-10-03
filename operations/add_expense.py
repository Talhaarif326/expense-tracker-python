from database import get_db_connection
from operations.balance_ops import get_current_balance, update_balance

def add_expense():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        print("Database Connection Establish ✅✅")
        
        expense_amount = float(input("Enter Expense Amount: "))
        expense_category = input("Enter Expense Category: ")
        expense_description = input("Enter Expense Detail: ")
        
        current_balance = get_current_balance()
        
        if expense_amount > current_balance:
            print(f"Insufficient Funds")
            return
        
        new_balance = current_balance - expense_amount
        
        cursor.execute("INSERT INTO EXPENSES(AMOUNT, CATEGORY, DESCRIPTION) VALUES(?,?,?)",(expense_amount, expense_category,expense_description))
        update_balance(new_balance)
        print(f"Expense Add Successfully ✅.")
        print(f"\n Remaining Balance: {new_balance}")
        
        conn.commit()
        conn.close()
    
    except Exception as e:
        print(f"Error: {e}")