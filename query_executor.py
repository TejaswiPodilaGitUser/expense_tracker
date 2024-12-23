import streamlit as st
import pandas as pd
from db_connection import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

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
                if query_result.empty:
                    st.warning("⚠️ No data present in the table.")
                else:
                    st.session_state.query_result = query_result  # Store in session state
            except pd.io.sql.DatabaseError as e:
                if "1146" in str(e):
                    st.error("❌ Table does not exist.")
                else:
                    st.error(f"❌ Error executing query: {e}")
            except SQLAlchemyError as e:
                st.error(f"❌ SQLAlchemy error: {e}")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")
            finally:
                db.close()  # Close connection after use
        else:
            st.error("❌ Failed to execute query. Check your database connection.")
    
    # Display the stored result, if available
    if 'query_result' in st.session_state:
        st.write(st.session_state.query_result)