from db_connection import MySQLDatabase
from expense_data_generator import generate_expense_report

# Create Monthly Tables and Load Data
def create_and_load_data():
    db = MySQLDatabase()
    conn = db.connect()
    if not conn:
        print("❌ Failed to connect to the database.")
        return
    
    cursor = conn.cursor()
    
    try:
        for month in range(1, 13):
            table_name = f'expenses_month_{month}'
            print(f"📊 Creating table: {table_name}")
            
            # Create Table
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE,
                    category VARCHAR(50),
                    payment_mode VARCHAR(50),
                    description VARCHAR(255),
                    amount_paid FLOAT,
                    cashback FLOAT
                )
            ''')
            
            # Generate and Insert Data
            expenses = generate_expense_report(month)
            cursor.executemany(f'''
                INSERT INTO {table_name} (date, category, payment_mode, description, amount_paid, cashback)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', expenses)
            conn.commit()
            print(f"✅ Data inserted into table: {table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to update an expense in a specific month table
def update_expense(month, expense_id, date, category, payment_mode, description, amount_paid, cashback):
    db = MySQLDatabase()
    conn = db.connect()
    if not conn:
        print("❌ Failed to connect to the database.")
        return
    
    cursor = conn.cursor()
    table_name = f'expenses_month_{month}'
    
    try:
        query = f"""
        UPDATE {table_name}
        SET date = %s, category = %s, payment_mode = %s, description = %s, amount_paid = %s, cashback = %s
        WHERE id = %s
        """
        cursor.execute(query, (date, category, payment_mode, description, amount_paid, cashback, expense_id))
        conn.commit()
        print(f"✅ Expense with ID {expense_id} updated in table {table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


# Function to delete an expense in a specific month table
def delete_expense(month, expense_id):
    db = MySQLDatabase()
    conn = db.connect()
    if not conn:
        print("❌ Failed to connect to the database.")
        return
    
    cursor = conn.cursor()
    table_name = f'expenses_month_{month}'
    
    try:
        query = f"DELETE FROM {table_name} WHERE id = %s"
        cursor.execute(query, (expense_id,))
        conn.commit()
        print(f"✅ Expense with ID {expense_id} deleted from table {table_name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
