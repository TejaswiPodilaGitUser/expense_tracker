import streamlit as st
import pandas as pd
from db_connection import MySQLDatabase

def custom_query_executor():
    """Allows users to execute custom SQL queries."""
    st.subheader('🔍 Execute Custom SQL Query')
    query = st.text_area("Enter your SQL query below:", "SELECT * FROM expenses_month_1 LIMIT 5")
    
    if st.button('Execute Query'):
        db = MySQLDatabase()  # Create an instance of MySQLDatabase
        conn = db.connect()  # Connect to the database
        if conn:
            try:
                # Execute the query and display the result
                query_result = pd.read_sql(query, conn)
                st.write(query_result)
            except Exception as e:
                st.error(f"❌ Error executing query: {e}")
            finally:
                db.close()  # Close connection after use
        else:
            st.error("❌ Failed to execute query. Check your database connection.")
