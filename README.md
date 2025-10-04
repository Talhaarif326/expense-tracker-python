# Expense Tracker 💰

A professional Python-based expense tracking application with beautiful console UI and SQLite database.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

## 🚀 Features

- 💵 **Balance Management** - Set and track your finances  
- 📊 **Expense Tracking** - Add expenses with automatic balance deduction  
- 🎨 **Beautiful UI** - Professional tables with Tabulate formatting  
- 💾 **Data Persistence** - SQLite database for reliable data storage  
- ✅ **Input Validation** - Prevent overspending and invalid inputs  
- 🏗️ **Modular Architecture** - Clean, maintainable OOP design  

## 📸 Demo

┌───────────────────┐
│ 💰 CURRENT BALANCE │
├───────────────────┤
│ $1000.00 │
└───────────────────┘

bash
Copy code

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher  
- pip package manager  

### Setup

```bash
# Clone the repository
git clone https://github.com/Talhaarif326/python-expense-tracker.git

# Navigate to project directory
cd python-expense-tracker

# Install dependencies
pip install tabulate

# Run the application
python main.py
````
🎯 Usage
Set Initial Balance – Start by setting your financial balance

Add Expenses – Record expenses (automatically deducts from balance)

View Balance – Check current available funds

View Expenses – Review spending history in beautiful tables

Exit – Close the application

🏗️ Project Structure
bash
Copy code
expense_tracker_project/
├── main.py                 # Application entry point
├── database.py             # Database connection & setup
├── models.py               # OOP models (Balance, Expenses)
├── operations/             # Business logic
│   ├── add_expense.py      # Add expense functionality
│   ├── balance_ops.py      # Balance operations
│   ├── view_balance.py     # Balance display
│   └── view_expenses.py    # Expenses display
├── utils/                  # Helper functions
│   └── validators.py       # Input validation
**💻 Technology Stack**
Backend: Python 3.11

Database: SQLite

UI: Tabulate (for beautiful console tables)

Architecture: Object-Oriented Programming (OOP)

Error Handling: Comprehensive try-except blocks

**🎨 Features in Detail**
**💵 Balance Management**
Set initial balance with professional formatting

Real-time balance updates with each expense

Automatic deduction validation

Persistent storage across sessions

**📊 Expense Tracking**
Categorized expense recording

Timestamped entries

Beautiful tabular display

Full CRUD operations

**🧭 User Experience**
Intuitive menu system

Clear error messages

Professional data presentation

Input validation and safeguards

**🤝 Contributing**

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

**👨‍💻 Developer**
Talha Arif
GitHub: @Talhaarif326

