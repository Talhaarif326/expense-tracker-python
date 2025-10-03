from database import get_db_connection
from operations.balance_ops import get_current_balance, set_initial_balance
from utils.validators import balance_check                   

def view_balance():
    
    try:
        if not balance_check():
            print("Balance is not set.")
            set_initial_balance()
            
            balance = get_current_balance()
            
            if balance is not None:
                return f"✅ Balance set successfully! Current Balance: {balance}"
            else:
                return "❌ Failed to set balance. Please try again."

        balance = get_current_balance()

        return f"Current Balance: {balance}"
    except Exception as e:
        print(f"Error: {e}")
