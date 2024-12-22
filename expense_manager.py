# expense_manager.py
from db_operations import update_expense, delete_expense

class ExpenseManager:
    def __init__(self, expenses_df):
        self.expenses_df = expenses_df

    def update_expense(self, expense_id, date, category, payment_mode, description, amount_paid, cashback):
        # Call the update_expense method from db_operations
        update_expense(expense_id, date, category, payment_mode, description, amount_paid, cashback)

    def delete_expense(self, expense_id):
        # Call the delete_expense method from db_operations
        delete_expense(expense_id)
