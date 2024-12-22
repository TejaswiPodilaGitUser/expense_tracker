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
            combined_df = pd.concat(dataframes, ignore_index=True)
            return combined_df
        else:
            return None
    return None

def get_top_expenses(df, top_n=10):
    """Returns the top N expenses from the combined data."""
    if df is not None and not df.empty:
        top_expenses = df.sort_values(by='amount_paid', ascending=False).head(top_n)
        return top_expenses
    return None
