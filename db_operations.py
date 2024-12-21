from expense_tracker_project.db_connection import get_db_connection
from expense_data_generator import generate_expense_report

# Create Monthly Tables and Load Data
def create_and_load_data():
    conn = get_db_connection()
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
            print(f"📊 Inserting data into table: {table_name}")
            expenses = generate_expense_report(50)  # 50 records per month
            
            for expense in expenses:
                cursor.execute(f'''
                    INSERT INTO {table_name} (date, category, payment_mode, description, amount_paid, cashback)
                    VALUES (%s, %s, %s, %s, %s, %s)
                ''', (
                    expense['date'],
                    expense['category'],
                    expense['payment_mode'],
                    expense['description'],
                    expense['amount_paid'],
                    expense['cashback']
                ))
        
        conn.commit()
        print("✅ Data inserted successfully into all monthly tables.")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
        print("🔌 Connection closed.")
