import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data, get_top_expenses
from components import month_selector, chart_selector
from query_executor import custom_query_executor
from update_expense_ui import update_expense_ui
from delete_expense_ui import delete_expense_ui
from yearly_data_visualization import plot_yearly_spending_bar_chart, plot_top_10_category_pie_chart
from monthly_data_visualization import plot_category_spending, plot_monthly_trends

# ---------------------------
# Streamlit App
# ---------------------------
st.set_page_config(layout="wide")
st.title('📊 Expense Tracker Dashboard')

# Load data
df = load_data()

if df is not None and not df.empty:

    # ------------------------
    # Section 1: Yearly Chart Type (Right side)
    # ------------------------
    col1, spacer, col2 = st.columns([2, 0.2, 2])
    with col1:  
        st.subheader("📅 Annual Spending Insights")
        
    with col2:
        # Yearly Chart Type Selection (Pie/Bar)
        chart_type = chart_selector("Select Yearly Data Chart Type:", "yearly_chart_type", "Pie Chart")
        st.session_state.chart_type = chart_type

    # ------------------------
    # Section 2: Top 10 Expenditures and Yearly Charts
    # ------------------------
    col1, spacer, col2 = st.columns([2, 0.2, 2])

    with col1:
        top_expenses = get_top_expenses(df)
        if top_expenses is not None:
            st.subheader("💰 Yearly Top 10 Expenditures:")
            st.write(top_expenses)
        else:
            st.write("❌ No valid data found.")
    
    with col2:
        chart_type = st.session_state.chart_type
        if chart_type == "Bar Chart":
            st.subheader("Total Spending Per Month:")
            bar_chart_fig = plot_yearly_spending_bar_chart(df)
          
        elif chart_type == "Pie Chart":
            st.subheader("🗂️ Annual Top 10 Spending Categories:")
            fig = plot_top_10_category_pie_chart(df)

    # ------------------------
    # Section 3: Month Selection & Monthly Chart Type
    # ------------------------
    st.subheader("📅 Monthly Data Visualization")
    col1, spacer, col2 = st.columns([2, 0.2, 2])

    with col1:
        selected_month = month_selector()
    
    with col2: 
        monthly_chart_type = chart_selector("Select Monthly Chart Type:", "monthly_chart_type", "Bar Chart")

    # ------------------------
    # Section 4: Monthly Data Visualization
    # ------------------------
    #st.subheader("📊 Monthly Spending Insights")
    col1, spacer, col2 = st.columns([2, 0.2, 2])

    monthly_data = df[df['month'] == selected_month]
    
    with col1:
        plot_monthly_trends(df, selected_month)
    
    with col2:
        plot_category_spending(monthly_data, monthly_chart_type)

    # ------------------------
    # Section 5: Execute Custom SQL Query
    # ------------------------
    custom_query_executor(selected_month)

    # ------------------------
    # Section 6: Expense Management (Update/Delete)
    # ------------------------
    st.subheader("⚙️ Expense Management")
    selected_action = st.selectbox(
        "Select an Action:",
        ["None", "Update Expense", "Delete Expense"],
        index=0,
        key="expense_action"
    )

    if selected_action == "Update Expense":
        update_expense_ui(selected_month)

    if selected_action == "Delete Expense":
        delete_expense_ui(selected_month)

else:
    st.warning("⚠️ No data available in the database. Please run `main.py` to populate data.")
