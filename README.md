# 🏦 Budget Tracker

A **command-line budget tracking application** built using Python and SQLite3. This tool allows users to **manage expenses, track income, set budgets, and monitor financial goals** in a structured and interactive way.

---

## 📜 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [Database Schema](#database-schema)
6. [Functions & Commands](#functions--commands)
7. [Error Handling](#error-handling)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

---

## 🎯 Overview

Managing personal finances can be challenging. This **Budget Tracker** provides a simple **command-line interface (CLI)** for users to:

- Record **expenses** and **income**.
- Set **budgets** for different categories.
- Define **financial goals** and track progress.
- Manage expenses efficiently by **updating or deleting** records.
- Store all financial data securely in a **SQLite database**.

---

## ✨ Features

✔ **Expense Tracking**:  
   - Add, view, update, and delete expenses.  
   - Categorize expenses for better tracking.  

✔ **Income Management**:  
   - Record income sources and amounts.  
   - Categorize income for clarity.  

✔ **Budgeting System**:  
   - Set budgets for specific categories.  
   - View budgets and ensure spending stays within limits.  

✔ **Financial Goals**:  
   - Set savings goals and contribute towards them.  
   - Monitor goal progress in real-time.  

✔ **Database Storage**:  
   - Uses **SQLite3** for structured financial record storage.  
   - Ensures data persistence even after exiting the application.  

✔ **Error Handling**:  
   - Prevents invalid inputs (e.g., non-numeric values for amounts).  
   - Catches database errors and provides user-friendly messages.  

---

## 🛠 Installation

### 1️⃣ Prerequisites

- **Python 3.x** installed on your system.
- **SQLite3**, which is included with Python.

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/karmaniomar/budget_tracker.git
cd budget-tracker
```

### 3️⃣ Run the Application

```sh
python budget_tracker.py
```

This will launch the **main menu**, where you can start tracking your budget.

---

## 📌 How to Use

Once the script runs, the **main menu** appears:

```plaintext
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. View progress towards financial goals
11. Quit
```

📌 **Select an option by entering the corresponding number.**  

For example, if you want to **add an expense**, type `1` and follow the prompts.

---

## 📊 Database Schema

The program stores data in **budget_tracker.db** using SQLite3. The following tables are created:

### 📍 `expenses`
| Column      | Type   | Description                 |
|-------------|--------|----------------------------|
| `id`        | INTEGER PRIMARY KEY | Unique identifier for each expense. |
| `category`  | TEXT   | The category of the expense (e.g., Food, Rent, Entertainment). |
| `amount`    | REAL   | The amount spent. |
| `description` | TEXT | Optional description of the expense. |

### 📍 `income`
| Column      | Type   | Description                 |
|-------------|--------|----------------------------|
| `id`        | INTEGER PRIMARY KEY | Unique identifier for each income record. |
| `category`  | TEXT   | The category of income (e.g., Salary, Freelancing). |
| `amount`    | REAL   | The amount earned. |
| `description` | TEXT | Optional description. |

### 📍 `budgets`
| Column      | Type   | Description                 |
|-------------|--------|----------------------------|
| `id`        | INTEGER PRIMARY KEY | Unique identifier for each budget. |
| `category`  | TEXT   | The category the budget applies to. |
| `budget`    | REAL   | The budgeted amount. |

### 📍 `goals`
| Column          | Type   | Description                      |
|----------------|--------|----------------------------------|
| `id`          | INTEGER PRIMARY KEY | Unique goal identifier. |
| `goal_name`   | TEXT   | Name of the financial goal. |
| `target_amount` | REAL | The total amount needed. |
| `current_amount` | REAL DEFAULT 0 | Amount saved towards the goal. |

---

## ⚡ Functions & Commands

### ✅ **Managing Expenses**
#### ➤ Add an Expense:
```plaintext
Enter expense category: Food
Enter expense amount: 50
Enter description (optional): Lunch
```
#### ➤ View Expenses:
- Lists all recorded expenses.
- Options to **update** or **delete** an entry.

### ✅ **Managing Income**
#### ➤ Add Income:
```plaintext
Enter income category: Salary
Enter income amount: 3000
Enter description (optional): Monthly Pay
```
#### ➤ View Income:
- Lists all recorded income sources.
- Options to **delete** an entry.

### ✅ **Setting a Budget**
#### ➤ Set a Budget:
```plaintext
Enter category: Groceries
Enter budget amount: 200
```
#### ➤ View Budgets:
- Displays all budgeted categories with their set amounts.

### ✅ **Setting Financial Goals**
#### ➤ Set a Goal:
```plaintext
Enter financial goal name: Vacation
Enter target amount for the goal: 5000
```
#### ➤ Contribute to a Goal:
```plaintext
Enter the ID of the goal you want to contribute to: 1
Enter the amount to contribute: 500
```
#### ➤ View Progress:
- Shows **goal name, target amount, current savings, and progress percentage**.

---

## 🛑 Error Handling

The program includes robust **error handling**:

- Prevents users from entering **non-numeric values** where numbers are required.
- Catches **database connection issues** and prints helpful error messages.
- Ensures **inputs are valid** before committing to the database.

Example:
```plaintext
Enter expense amount: abc
Invalid input. Please enter a valid number.
```

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:  
   ```sh
   git checkout -b feature-new-feature
   ```
3. **Make your changes and commit**:  
   ```sh
   git commit -m "Added a new feature"
   ```
4. **Push to your branch**:  
   ```sh
   git push origin feature-new-feature
   ```
5. **Submit a pull request** 🎉.

---

## 📜 License

This project is licensed under the **MIT License**.  

---

## 📬 Contact

If you have any questions, suggestions, or feedback, feel free to reach out!  

📧 **Email**: [omar.karmani93@gmail.com](mailto:omar.karmani93@gmail.com)

🚀 **Happy Budgeting!**
```
