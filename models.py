class Balance:
    def __init__(self,id, current_balance, last_update ):
        self.id = id
        self.current_balance = current_balance
        self.last_update = last_update
    
    
    def __str__(self):
        return f"Balance ID: {self.id}. Current Balance: {self.current_balance}. Last Update: {self.last_update}"  
        
class Expenses:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date 
        
    def __str__(self):
        return f"ID: {self.expense_id}. Amount: {self.amount}. Category: {self.category}. Detail: {self.description}. Date: {self.date}"