from db_connection import MySQLDatabase
import pandas as pd

def load_data():
    """Fetches data from all 12 monthly tables and combines them."""
    db = MySQLDatabase()  # Create an instance of MySQLDatabase
    conn = db.connect()  # Connect to the database
    if conn:
        dataframes = []
        for i in range(1, 13):  # Loop through months 1 to 12
            query = f"SELECT * FROM expenses_month_{i}"
            try:
                monthly_df = pd.read_sql(query, conn)
                monthly_df['month'] = i  # Add a 'month' column to each table's data
                dataframes.append(monthly_df)
            except Exception as e:
                print(f"❌ Error fetching data for month {i}: {e}")
        
        db.close()  # Close connection
        
        # Combine all monthly data into a single DataFrame
        if dataframes:
            return pd.concat(dataframes, ignore_index=True)
        else:
            return None
    return None
