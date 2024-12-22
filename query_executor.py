import streamlit as st
import pandas as pd
from db_connection import MySQLDatabase

def custom_query_executor(selected_month):
    """Allows users to execute custom SQL queries with a default month parameter."""
    st.subheader('🔍 Execute Custom SQL Query')
    
    # Default query using selected_month
    default_query = f"SELECT * FROM expenses_month_{selected_month} LIMIT 5"
    query = st.text_area("Provide Your Custom SQL Query:", default_query)
    
    # Button to execute query
    if st.button('Execute Query'):
        db = MySQLDatabase()  # Create an instance of MySQLDatabase
        conn = db.connect()  # Connect to the database
        if conn:
            try:
                # Execute the query and store the result in session_state
                query_result = pd.read_sql(query, conn)
                st.session_state.query_result = query_result  # Store in session state
            except Exception as e:
                st.error(f"❌ Error executing query: {e}")
            finally:
                db.close()  # Close connection after use
        else:
            st.error("❌ Failed to execute query. Check your database connection.")
    
    # Display the stored result, if available
    if 'query_result' in st.session_state:
        st.write(st.session_state.query_result)
