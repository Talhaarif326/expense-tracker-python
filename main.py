from database import get_db_connection, database
from models import Balance, Expenses
from operations.add_expense import add_expense
from operations.balance_ops import set_initial_balance, get_current_balance, update_balance
from operations.view_balance import view_balance
from operations.view_expenses import view_expenses
from utils.validators import balance_check, expense_check


def main():
    try:
        while True:
            print(f"\n Welcome ")
            print(f"Select From the below Menu")
            print(f"\n\n Ξ Menu ")
            print(f"1. Set Initial Balance")
            print(f"2. View Balance. ")
            print(f"3. View Expenses. ")
            print(f"4. Add Expenses. ")
            print(f"5. View Current Balance. ")
            print(f"6. Update Balance.")
            print(f"7. Exit App.")
            
            choice = input("Enter your choice: ")
            
            
            match choice:
                case "1":
                    set_initial_balance()
                    
                case "2":
                    view_balance()
                
                case "3":
                    view_expenses()
                
                case "4":
                    add_expense()
                
                case "5":
                    get_current_balance()
                
                case "6":
                    update_balance()
                
                case "7":
                    break
                    
                case _:
                    print("Invalid Choice.")
        
    except Exception as e:
        print(f"Error: {e}")
        
        

if __name__ == "__main__":
    database()
    main()