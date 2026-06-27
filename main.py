import sqlite3
import database

def connect():
    return sqlite3.connect("expenses.db")


def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses(date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )

    conn.commit()
    conn.close()

    print("Expense Added Successfully!\n")


def view_expenses():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()

    print("\n------ Expenses ------")
    for row in rows:
        print(row)

    conn.close()


def total_expense():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT SUM(amount) FROM expenses")
    total = cur.fetchone()[0]

    print("\nTotal Expense:", total if total else 0)

    conn.close()


def delete_expense():
    expense_id = int(input("Enter Expense ID to delete: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()

    conn.close()

    print("Expense Deleted Successfully")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank You!")
        break
    
    else:
        print("Invalid Choice")