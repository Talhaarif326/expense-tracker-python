from database import database
from models import Balance, Expenses
from operations.add_expense import add_expense
from operations.balance_ops import set_initial_balance
from operations.view_balance import view_balance
from operations.view_expenses import view_expenses


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
            print(f"5. Exit App.")
            
            choice = input("Enter your choice: ")
            
            
            match choice:
                case "1":
                    set_initial_balance()
                    
                case "2":
                    result = view_balance()
                    print(result)
                
                case "3":
                    result = view_expenses()
                    print(result)
                
                case "4":
                    add_expense()
                                    
                case "5":
                    break
                    
                case _:
                    print("Invalid Choice.")
        
    except Exception as e:
        print(f"Error: {e}")
        
        

if __name__ == "__main__":
    database()
    main()