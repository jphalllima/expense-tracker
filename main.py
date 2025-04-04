import json
import os

def add_expense():
    # Get expense details from user
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter a brief description: ")

    # Expense dictionary
    expense = {
        "date": date, 
        "amount": amount, 
        "category": category,
        "description": description,
    }

    # To load data we have or to initialize an empty list
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            try:
                expenses = json.load(file)
            except json.JSONDecodeError:
                expenses = []
    else:
        expenses = []

    expenses.append(expense)

    # Now we save it back to JSON after adding the expense
    with open("expenses.json", "w")as file:
        json.dump(expenses, file, indent=4)

    print("Expense was added successfully!\n")
          
def main():
    while True:
        print("Welcome to your Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("Feature soon")
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Not valid - Pick a number between 1 and 3.\n")

if __name__ == "__main__":
    main()