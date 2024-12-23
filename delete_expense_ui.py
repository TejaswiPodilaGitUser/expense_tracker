import streamlit as st
import pandas as pd
from expense_manager import delete_expense
from db_connection import MySQLDatabase
from sqlalchemy.exc import SQLAlchemyError

# Function to fetch data for a specific month
def get_monthly_data(month):
    db = MySQLDatabase()
    conn = db.connect()
    if not conn:
        st.error("❌ Failed to connect to the database.")
        return pd.DataFrame(), "connection_error"
    
    query = f"SELECT * FROM expenses_month_{month}"
    try:
        df = pd.read_sql(query, conn)
    except pd.io.sql.DatabaseError as e:
        if "1146" in str(e):
            return pd.DataFrame(), "table_not_exist"
        else:
            st.error(f"❌ Error executing query: {e}")
            return pd.DataFrame(), "query_error"
    finally:
        conn.close()
    
    return df, None

# UI Component for deleting an expense
def delete_expense_ui(selected_month):
    st.subheader('🗑️ Delete an Expense')
    
    # Display the selected month
    st.info(f"📅 Selected Month: **{selected_month}**")
    
    df, error = get_monthly_data(selected_month)
    if error == "table_not_exist":
        st.error(f"❌ Table expenses_month_{selected_month} does not exist.")
        return
    elif df.empty:
        st.warning("⚠️ No data available for the selected month.")
        return
    
    expense_id_to_delete = st.selectbox("Select Expense to Delete", df['id'])

    if expense_id_to_delete:
        expense_row = df[df['id'] == expense_id_to_delete].iloc[0]
        
        # Display existing data for confirmation
        st.write(f"**Date:** {expense_row['date']}")
        st.write(f"**Category:** {expense_row['category']}")
        st.write(f"**Payment Mode:** {expense_row['payment_mode']}")
        st.write(f"**Description:** {expense_row['description']}")
        st.write(f"**Amount Paid:** {expense_row['amount_paid']}")
        st.write(f"**Cashback:** {expense_row['cashback']}")
        
        if st.button("Delete Expense"):
            try:
                delete_expense(selected_month, expense_id_to_delete)
                st.success(f"✅ Expense ID {expense_id_to_delete} deleted successfully for month {selected_month}!")
            except Exception as e:
                st.error(f"❌ Error: {e}")