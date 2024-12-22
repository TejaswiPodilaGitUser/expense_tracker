import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from utils import DateUtils

def plot_category_spending(monthly_data, chart_type):
    """Visualizes spending by category."""
    category_spending = monthly_data.groupby('category')['amount_paid'].sum().sort_values(ascending=False)
    
    if chart_type == 'Bar Chart':
        st.subheader('📊 Total Spending by Category')
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=category_spending.index, y=category_spending.values, ax=ax)
        #ax.set_title('Total Spending by Category')
        ax.set_ylabel('Amount Paid', fontweight='bold')
        ax.set_xlabel('Category', fontweight='bold')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

    elif chart_type == 'Pie Chart':
        st.subheader('🥧 Spending Distribution by Category')
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(
            category_spending.values,
            labels=category_spending.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Paired.colors
        )
        #ax.set_title('Spending Distribution by Category')
        st.pyplot(fig)

def plot_monthly_trends(df, selected_month):
    """Displays category-wise spending for the selected month using a line chart."""
    
    # Filter data for the selected month
    monthly_data = df[df['month'] == selected_month]
    
    # Section 1: Total Spending for the Selected Month
    total_spending = monthly_data['amount_paid'].sum()
    st.subheader(f"💰 Total Spending for Month {selected_month}: ${total_spending:.2f}")

    # Section 2: Spending by Category for the Selected Month
    category_spending = monthly_data.groupby('category')['amount_paid'].sum()

    # Display Line Chart for category spending in the selected month
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(category_spending.index, category_spending.values, marker='o', color='royalblue')
   # ax.set_title(f'Spending Distribution by Category in Month {selected_month}')
    ax.set_xlabel('Category', fontweight='bold')
    ax.set_ylabel('Amount Paid ($)', fontweight='bold')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig)

    # Section 3: Max and Min Spending Categories for the selected month
    max_category = category_spending.idxmax()
    max_category_spending = category_spending.max()
    min_category = category_spending.idxmin()
    min_category_spending = category_spending.min()

    # Display the insights for the selected month

    # Month name mapping
    month_names = DateUtils.get_month_names()
    month_name = month_names[selected_month]

    st.write(f"Max Spending Category in {month_name}: {max_category} with ${max_category_spending:.2f}")
    st.write(f"Min Spending Category in {month_name}: {min_category} with ${min_category_spending:.2f}")