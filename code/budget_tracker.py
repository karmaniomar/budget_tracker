import sqlite3


def create_tables():
    """
    Create database tables for the budget tracker application.

    Tables created:
        - **expenses**: Stores expense records.
        - **income**: Stores income records.
        - **budgets**: Stores budget records for specific categories.
        - **goals**: Stores financial goal records.
    """
    try:
        connection = sqlite3.connect("budget_tracker.db")
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY,
                category TEXT NOT NULL,
                budget REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY,
                goal_name TEXT NOT NULL,
                target_amount REAL NOT NULL,
                current_amount REAL DEFAULT 0
            )
        """)

        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()


def connect_db():
    """
    Establish a connection to the database.

    :return: A `sqlite3.Connection` object.
    """
    return sqlite3.connect("budget_tracker.db")


def add_expense():
    """
    Add a new expense to the database.

    Prompts the user for the following input:
        - **category**: The category of the expense.
        - **amount**: The amount of the expense.
        - **description**: (Optional) A description of the expense.

    Adds the expense record to the `expenses` table.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()

        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        description = input("Enter description (optional): ")

        cursor.execute(
            "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
            (category, amount, description),
        )
        connection.commit()
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_expenses():
    """
    Display all expense records from the database.

    Features:
        - View all expenses.
        - Update an expense amount.
        - Delete an expense. If linked to a financial goal, adjusts the goal's current amount.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        if not rows:
            print("No expenses found.")
            return

        print("Expenses:")
        for row in rows:
            print(
                f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}"
            )

        choice = input(
            "Do you want to (U)pdate an amount, (D)elete an expense, or (Q)uit? "
        ).lower()
        if choice == "u":
            expense_id = int(input("Enter the ID of the expense to update: "))
            new_amount = float(input("Enter the new amount: "))
            cursor.execute(
                "UPDATE expenses SET amount = ? WHERE id = ?",
                (new_amount, expense_id),
            )
            connection.commit()
            print("Expense amount updated successfully!")
        elif choice == "d":
            expense_id = int(input("Enter the ID of the expense to delete: "))

            # Retrieve the expense details before deletion
            cursor.execute(
                "SELECT category, amount FROM expenses WHERE id = ?", (expense_id,)
            )
            expense_details = cursor.fetchone()

            if expense_details:
                expense_category, expense_amount = expense_details

                # Delete the expense
                cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
                connection.commit()
                print("Expense deleted successfully!")

                # Check if the expense category matches any financial goal
                cursor.execute(
                    "SELECT id, current_amount FROM goals WHERE goal_name = ?",
                    (expense_category,),
                )
                goal = cursor.fetchone()

                if goal:
                    goal_id, current_amount = goal

                    # Deduct the expense amount from the financial goal's current amount
                    updated_amount = max(0, current_amount - expense_amount)
                    cursor.execute(
                        "UPDATE goals SET current_amount = ? WHERE id = ?",
                        (updated_amount, goal_id),
                    )
                    connection.commit()
                    print(
                        f"Adjusted financial goal '{expense_category}' due to expense deletion."
                    )
        elif choice == "q":
            print("Returning to the main menu.")
    except ValueError:
        print("Invalid input. Please try again.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_expenses_by_category():
    """
    Display expenses filtered by a specific category.

    Prompts the user for a category and displays matching expenses.
    Features:
        - Update an expense amount.
        - Delete an expense. If linked to a financial goal, adjusts the goal's current amount.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        category = input("Enter category: ")
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
        rows = cursor.fetchall()
        if not rows:
            print(f"No expenses found in category '{category}'.")
            return

        print(f"Expenses in category '{category}':")
        for row in rows:
            print(
                f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}"
            )

        choice = input(
            "Do you want to (U)pdate an amount, (D)elete an expense, or (Q)uit? "
        ).lower()
        if choice == "u":
            expense_id = int(input("Enter the ID of the expense to update: "))
            new_amount = float(input("Enter the new amount: "))
            cursor.execute(
                "UPDATE expenses SET amount = ? WHERE id = ?",
                (new_amount, expense_id),
            )
            connection.commit()
            print("Expense amount updated successfully!")
        elif choice == "d":
            expense_id = int(input("Enter the ID of the expense to delete: "))

            # Retrieve the expense details before deletion
            cursor.execute(
                "SELECT category, amount FROM expenses WHERE id = ?", (expense_id,)
            )
            expense_details = cursor.fetchone()

            if expense_details:
                expense_category, expense_amount = expense_details

                # Delete the expense
                cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
                connection.commit()
                print("Expense deleted successfully!")

                # Check if the expense category matches any financial goal
                cursor.execute(
                    "SELECT id, current_amount FROM goals WHERE goal_name = ?",
                    (expense_category,),
                )
                goal = cursor.fetchone()

                if goal:
                    goal_id, current_amount = goal

                    # Deduct the expense amount from the financial goal's current amount
                    updated_amount = max(0, current_amount - expense_amount)
                    cursor.execute(
                        "UPDATE goals SET current_amount = ? WHERE id = ?",
                        (updated_amount, goal_id),
                    )
                    connection.commit()
                    print(
                        f"Adjusted financial goal '{expense_category}' due to expense deletion."
                    )
        elif choice == "q":
            print("Returning to the main menu.")
    except ValueError:
        print("Invalid input. Please try again.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def add_income():
    """
    Add a new income record to the database.

    Prompts the user for the following input:
        - **category**: The category of the income.
        - **amount**: The amount of the income.
        - **description**: (Optional) A description of the income.

    Adds the income record to the `income` table.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()

        category = input("Enter income category: ")
        amount = float(input("Enter income amount: "))
        description = input("Enter description (optional): ")

        cursor.execute(
            "INSERT INTO income (category, amount, description) VALUES (?, ?, ?)",
            (category, amount, description),
        )
        connection.commit()
        print("Income added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_income():
    """
    Display all income records from the database.

    Features:
        - View all income records.
        - Delete an income record.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM income")
        rows = cursor.fetchall()
        if not rows:
            print("No income records found.")
        else:
            print("Income:")
            for row in rows:
                print(
                    f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}"
                )

            choice = input("Do you want to (D)elete an income or (Q)uit? ").lower()
            if choice == "d":
                income_id = int(input("Enter the ID of the income to delete: "))
                cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))
                connection.commit()
                print("Income record deleted successfully!")
            elif choice == "q":
                print("Returning to the main menu.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_income_by_category():
    """
    Display income records filtered by a specific category.

    Prompts the user for a category and displays matching income records.
    Features:
        - Delete all income records for a specific category.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        category = input("Enter category: ")
        cursor.execute("SELECT * FROM income WHERE category = ?", (category,))
        rows = cursor.fetchall()
        if not rows:
            print(f"No income records found in category '{category}'.")
        else:
            print(f"Income in category '{category}':")
            for row in rows:
                print(
                    f"ID: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}"
                )

            choice = input("Do you want to (D)elete this category or (Q)uit? ").lower()
            if choice == "d":
                cursor.execute("DELETE FROM income WHERE category = ?", (category,))
                connection.commit()
                print(
                    f"Category '{category}' and associated income records deleted successfully!"
                )
            elif choice == "q":
                print("Returning to the main menu.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def set_budget():
    """
    Set or update the budget for a specific category.

    Prompts the user for the following input:
        - **category**: The category for which the budget will be set.
        - **budget**: The budget amount.

    If the category exists, updates the budget amount.
    Otherwise, creates a new budget record for the category.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        category = input("Enter category: ")
        budget = float(input("Enter budget amount: "))

        # Check if category exists
        cursor.execute("SELECT id FROM budgets WHERE category = ?", (category,))
        existing_record = cursor.fetchone()

        if existing_record:
            # Update the budget if the category exists
            cursor.execute(
                "UPDATE budgets SET budget = ? WHERE category = ?", (budget, category)
            )
        else:
            # Insert a new budget record if the category does not exist
            cursor.execute(
                "INSERT INTO budgets (category, budget) VALUES (?, ?)",
                (category, budget),
            )

        connection.commit()
        print("Budget set successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_budget():
    """
    View the budget for a specific category.

    Prompts the user to select a category by its ID and displays its budget amount.

    Features:
        - Lists all available categories with their IDs.
        - Fetches and displays the budget for the selected category.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Fetch and display all available categories with their IDs
        cursor.execute("SELECT id, category FROM budgets")
        categories = cursor.fetchall()

        if not categories:
            print("No categories found. Please set a budget first.")
            return

        print("Available categories:")
        for category in categories:
            print(f"ID: {category[0]}, Category: {category[1]}")

        # Prompt the user to select a category by ID
        category_id = int(input("Enter the ID of the category: "))

        # Fetch and display the budget for the selected category
        cursor.execute(
            "SELECT category, budget FROM budgets WHERE id = ?", (category_id,)
        )
        row = cursor.fetchone()
        if row:
            print(f"Budget for {row[0]}: {row[1]}")
        else:
            print("No budget found for this ID.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def set_financial_goal():
    """
    Set a new financial goal.

    Prompts the user for the following input:
        - **goal_name**: The name of the financial goal.
        - **target_amount**: The target amount for the financial goal.

    Adds the financial goal record to the `goals` table.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()
        goal_name = input("Enter financial goal name: ")
        target_amount = float(input("Enter target amount for the goal: "))

        cursor.execute(
            "INSERT INTO goals (goal_name, target_amount) VALUES (?, ?)",
            (goal_name, target_amount),
        )
        connection.commit()
        print("Financial goal set successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def view_financial_goal_progress():
    """
    View progress toward all financial goals.

    Features:
        - Display progress for all financial goals.
        - Contribute to a financial goal by adding funds.
        - Delete a financial goal by its ID, with optional deletion of linked expenses.
    """
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Fetch financial goals
        cursor.execute("SELECT id, goal_name, target_amount, current_amount FROM goals")
        rows = cursor.fetchall()

        if not rows:
            print("No financial goals set.")
            return

        print("Financial Goals Progress:")
        for row in rows:
            progress = (row[3] / row[2]) * 100 if row[2] != 0 else 0
            print(
                f"ID: {row[0]}, Goal: {row[1]}, Target: {row[2]}, Current: {row[3]}, Progress: {progress:.2f}%"
            )

        choice = input(
            "Do you want to (C)ontribute to a goal, (D)elete a goal, or (Q)uit? "
        ).lower()

        if choice == "c":
            goal_id = int(input("Enter the ID of the goal you want to contribute to: "))
            contribution_amount = float(input("Enter the amount to contribute: "))

            cursor.execute(
                "UPDATE goals SET current_amount = current_amount + ? WHERE id = ?",
                (contribution_amount, goal_id),
            )

            cursor.execute("SELECT goal_name FROM goals WHERE id = ?", (goal_id,))
            goal_name = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
                (goal_name, contribution_amount, "Contribution to financial goal"),
            )
            connection.commit()
            print("Contribution added successfully and logged as an expense!")

        elif choice == "d":
            goal_id = int(input("Enter the ID of the goal you want to delete: "))

            # Fetch the goal details before deletion
            cursor.execute(
                "SELECT goal_name, current_amount FROM goals WHERE id = ?", (goal_id,)
            )
            goal_details = cursor.fetchone()

            if goal_details:
                goal_name, current_amount = goal_details

                # Confirm deletion
                confirm = input(
                    f"Are you sure you want to delete the goal '{goal_name}'? This action cannot be undone. (Y/N): "
                ).lower()

                if confirm == "y":
                    # Delete the goal
                    cursor.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
                    connection.commit()

                    print(f"Financial goal '{goal_name}' deleted successfully!")

                    # Optionally, delete related expenses (if applicable)
                    related_expense_delete = input(
                        "Do you want to delete all expenses linked to this goal? (Y/N): "
                    ).lower()
                    if related_expense_delete == "y":
                        cursor.execute(
                            "DELETE FROM expenses WHERE category = ?", (goal_name,)
                        )
                        connection.commit()
                        print(
                            f"All expenses related to '{goal_name}' have been deleted."
                        )
                else:
                    print("Deletion canceled.")
            else:
                print("No financial goal found with the given ID.")

        elif choice == "q":
            print("Returning to the main menu.")

    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def main_menu():
    """
    Display the main menu and handle user input.

    Features:
        - Provides options for managing expenses, income, budgets, and financial goals.
        - Executes corresponding functions based on user input.
        - Allows the user to exit the application.
    """
    create_tables()
    while True:
        print("""
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
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses_by_category()
        elif choice == "4":
            add_income()
        elif choice == "5":
            view_income()
        elif choice == "6":
            view_income_by_category()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            view_budget()
        elif choice == "9":
            set_financial_goal()
        elif choice == "10":
            view_financial_goal_progress()
        elif choice == "11":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()
