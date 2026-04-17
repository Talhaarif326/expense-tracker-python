<div align="center">

# 💰 Expense Tracker

> A Python CLI expense tracking app with balance management, categorized expenses, and SQLite persistence.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![SQLite](https://img.shields.io/badge/Storage-SQLite-003B57?logo=sqlite)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📖 Overview

**Expense Tracker** is a command-line application that helps you manage your personal finances. Set an initial balance, log categorized expenses, and view your spending history — all stored persistently in a local SQLite database.

The app validates your balance before every expense, prevents overspending, and displays data in clean tabulated format.

**Built with:** Python · SQLite3 · Tabulate

---

## ✨ Features

- 💳 **Set Initial Balance** — Initialize your wallet balance before tracking
- 👁️ **View Balance** — See your current remaining balance at any time
- 📋 **View Expenses** — Browse all logged expenses in a formatted table
- ➕ **Add Expense** — Log an expense with amount, category, and description
- 🛡️ **Insufficient Funds Guard** — Blocks expenses that exceed your current balance
- 🗄️ **SQLite Persistence** — All data stored locally and survives app restarts
- ✅ **Smart Validation** — Checks if balance/expenses exist before any operation

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| sqlite3 (stdlib) | Local database — balance + expenses tables |
| tabulate | Formatted table output for expenses and balance |

---

## 🚀 Setup

### Prerequisites

- Python 3.10 or higher

### Install & Run

```bash
# Clone the repo
git clone https://github.com/Talhaarif326/expense-tracker-python.git

cd expense-tracker-python

# Install dependencies
pip install tabulate

# Run the app
python main.py
```

---

## 🏗️ Project Structure

```
expense-tracker-python/
├── main.py                       # Entry point — menu loop and routing
├── database.py                   # SQLite connection + table initialization
├── models.py                     # Balance and Expenses data classes
├── expense_tracker.db            # Auto-generated SQLite database
├── operations/
│   ├── add_expense.py            # Log new expense + deduct from balance
│   ├── balance_ops.py            # Set initial balance / get current balance
│   ├── view_balance.py           # Display balance (auto-prompts if not set)
│   └── view_expenses.py          # Display all expenses in tabulate grid
└── utils/
    └── validators.py             # balance_check() and expense_check() guards
```

---

## 📋 Usage

```
 Welcome
 Select From the below Menu

 Ξ Menu
1. Set Initial Balance
2. View Balance.
3. View Expenses.
4. Add Expenses.
5. Exit App.

Enter your choice:
```

**Adding an expense:**
```
Enter Expense Amount: 500
Enter Expense Category: Food
Enter Expense Detail: Dinner at restaurant

Balance Updated successfully ✅
Expense Added Successfully ✅
Remaining Balance: 4500
```

---

## 📝 Changelog

### v1.0.0
- ✨ Initial release
- Balance management with SQLite persistence
- Categorized expense logging
- Insufficient funds validation
- Tabulate-formatted output

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙌 Credits

- Built by [Talhaarif326](https://github.com/Talhaarif326)

---

<div align="center">
  <sub>Made with ❤️ using Python</sub>
</div>
