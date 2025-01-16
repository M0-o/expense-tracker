# Expense Tracker

## u can see changes now

## Introduction

This is a command-line based expense tracking application. It allows you to create budget categories, deposit and withdraw amounts, and visualize spending in a simple chart.

## Features in expenseTracker.py

1. **Category Class**

   - Manages a category's ledger.
   - Allows deposits and withdrawals.
   - Supports checking available funds to prevent overdrafts.
   - Enables transferring amounts to other categories while maintaining accurate ledgers.

2. **create_spend_chart Function**
   - Aggregates the total spending across all categories.
   - Generates a vertical bar chart showing each category's percentage of overall expenses.
   - Provides a simple visual snapshot of where your money goes.

## How the Program Works

1. **Main Menu**
   - The application (`main.py`) presents a menu of options for creating categories, depositing, withdrawing, transferring, or viewing category details.
2. **Interacting with Categories**
   - Each transaction updates the associated category’s ledger.
   - You can transfer funds between categories to keep budgets in sync.
3. **Viewing Results**
   - Print the category instance to see its ledger and current balance.
   - Use the spend chart menu option to visualize spending across all available categories.

## Example Usage

1. **Starting the Program**
   - On Windows:
     ```bash
     python main.py
     ```
   - On macOS/Linux:
     ```bash
     python3 main.py
     ```
2. **Creating a Category**
   - Choose the option to create a new category and enter its name.
3. **Deposit / Withdraw**
   - Select the respective options to deposit or withdraw from a chosen category.
4. **Generate a Spend Chart**
   - View a textual bar chart illustrating your spending percentages for all defined categories.

## Additional Notes

- Keep descriptions short and precise when prompted in the main menu to maintain clear records in the ledgers.
- You may further extend the `Category` class or add new features to reflect your specific budgeting needs.
