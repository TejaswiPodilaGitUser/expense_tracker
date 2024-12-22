import streamlit as st
import pandas as pd
from expense_manager import delete_expense
from db_connection import MySQLDatabase

# Function to fetch data for a specific month
def get_monthly_data(month):
    db = MySQLDatabase()
    conn = db.connect()
    if not conn:
        st.error("❌ Failed to connect to the database.")
        return pd.DataFrame()
    
    query = f"SELECT * FROM expenses_month_{month}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# UI Component for deleting an expense
def delete_expense_ui(selected_month):
    st.subheader('🗑️ Delete an Expense')
    
    # Display the selected month
    st.info(f"📅 Selected Month: **{selected_month}**")
    
    df = get_monthly_data(selected_month)
    if df.empty:
        st.warning("⚠️ No data available for the selected month.")
        return
    
    expense_id_to_delete = st.selectbox("Select Expense to Delete", df['id'])

    if st.button("Delete Expense"):
        try:
            delete_expense(selected_month, expense_id_to_delete)
            st.success(f"✅ Expense ID {expense_id_to_delete} deleted successfully from month {selected_month}!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
