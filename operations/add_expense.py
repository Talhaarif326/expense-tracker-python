from database import get_db_connection
from operations.balance_ops import get_current_balance, update_balance

def add_expense():
    try:
        # Step 1: Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()
        print("Database Connection Establish ✅✅")
        
        # Step 2: Get user input for expense details
        expense_amount = float(input("Enter Expense Amount: "))
        expense_category = input("Enter Expense Category: ")
        expense_description = input("Enter Expense Detail: ")
        
        # Step 3: Check current balance from database
        cursor.execute("SELECT BALANCE FROM balance ORDER BY ID DESC LIMIT 1")
        result = cursor.fetchone()
        current_balance = result['BALANCE'] if result else 0
        
        # Step 4: Validate if user has sufficient funds
        if expense_amount > current_balance:
            print(f"Insufficient Funds. Current Balance: {current_balance} ")
            return
        
        # Step 5: Calculate new balance after expense deduction
        new_balance = current_balance - expense_amount
        
        # Step 6: Update balance in database        
        cursor.execute("UPDATE balance SET BALANCE = ? WHERE ID= 1",(new_balance,))        
        print(f"Balance Update successfully✅") 
        
        # Step 7: Add expense record to expenses table
        cursor.execute("INSERT INTO EXPENSES(AMOUNT, CATEGORY, DESCRIPTION) VALUES(?,?,?)",(expense_amount, expense_category,expense_description))        
        
        # Step 8: Confirm success and show remaining balance
        print(f"Expense Add Successfully ✅.")
        print(f"\n Remaining Balance: {new_balance}")
        
        conn.commit()   # Step 9: Commit both operations (balance update + expense insert)
        conn.close()    # Close database connection
    
    except Exception as e:
        print(f"Error: {e}")