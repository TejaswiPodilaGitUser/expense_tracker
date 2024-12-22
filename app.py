import streamlit as st
from data_loader import load_data
from components import month_selector, chart_selector
from query_executor import custom_query_executor
from data_visualization import plot_category_spending, plot_monthly_trends
from update_expense_ui import update_expense_ui
from delete_expense_ui import delete_expense_ui

# ---------------------------
# Streamlit App
# ---------------------------
st.title('📊 Expense Tracker Dashboard')

# Load data
df = load_data()

if df is not None and not df.empty:
    #st.success("✅ Data loaded successfully!")
    st.write(df.head())  # Display first few rows for verification

    # Month Selection
    selected_month = month_selector()

    # Filter data by selected month
    monthly_data = df[df['month'] == selected_month]

    st.subheader(f'📅 Insights for Month {selected_month}')
    st.write(monthly_data.head())

    # Chart Selection and Visualization
    chart_type = chart_selector()
    plot_category_spending(monthly_data, chart_type)
    plot_monthly_trends(df)

    # Custom SQL Query
    custom_query_executor()

   # Update and Delete Expense Sections (With Dropdown Toggle)
    st.subheader("⚙️ Expense Management")

    selected_action = st.selectbox(
        "Select an Action:",
        ["None", "Update Expense", "Delete Expense"],
        index=0,
        key="expense_action"
    )

    if selected_action == "Update Expense":
        update_expense_ui(selected_month)  # Pass selected_month

    if selected_action == "Delete Expense":
        delete_expense_ui(selected_month)  # Pass selected_month


else:
    st.warning("⚠️ No data available in the database. Please run `main.py` to populate data.")
