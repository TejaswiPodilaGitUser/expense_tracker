import streamlit as st
import pandas as pd
from expense_manager import update_expense
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

# UI Component for updating an expense
def update_expense_ui(selected_month):
    st.subheader('📝 Update an Expense')
    
    # Display the selected month
    st.info(f"📅 Selected Month: **{selected_month}**")
    
    df = get_monthly_data(selected_month)
    if df.empty:
        st.warning("⚠️ No data available for the selected month.")
        return
    
    expense_id_to_update = st.selectbox("Select Expense to Update", df['id'])

    if expense_id_to_update:
        expense_row = df[df['id'] == expense_id_to_update].iloc[0]
        
        # Pre-fill existing data in the update form
        date = st.date_input("Date", pd.to_datetime(expense_row['date']))
        category = st.text_input("Category", expense_row['category'])
        payment_mode = st.text_input("Payment Mode", expense_row['payment_mode'])
        description = st.text_area("Description", expense_row['description'])
        amount_paid = st.number_input("Amount Paid", value=float(expense_row['amount_paid']))
        cashback = st.number_input("Cashback", value=float(expense_row['cashback']))
        
        if st.button("Update Expense"):
            try:
                update_expense(selected_month, expense_id_to_update, date, category, payment_mode, description, amount_paid, cashback)
                st.success(f"✅ Expense ID {expense_id_to_update} updated successfully for month {selected_month}!")
            except Exception as e:
                st.error(f"❌ Error: {e}")
