import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import mplcursors
from utils import DateUtils

def plot_yearly_spending_bar_chart(df, amount_column='amount_paid'):
    """
    Plots a bar chart of total spending per month for a given year.

    Args:
    - df (DataFrame): The data containing monthly expense information.
    - amount_column (str): The name of the column containing expense amounts (default is 'amount_paid').
    """
    # Group data by month and sum the expenses
    total_spending_per_month = df.groupby('month')[amount_column].sum()

    # Create the bar chart with a larger figure size for clarity
    fig, ax = plt.subplots(figsize=(8, 4))  # Adjusted to a larger size (12x6)
    
    # Plot the bar chart with a color palette
    sns.barplot(x=total_spending_per_month.index, y=total_spending_per_month.values, ax=ax, palette='viridis')

    # Add titles and labels with appropriate font sizes and bold font weight
    #ax.set_title('Total Spending Per Month (Year-wise)', fontsize=16, pad=20)
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Total Spending ($)', fontsize=14)

    # Customize x-axis labels (Rotate them for better readability)
    ax.set_xticks(range(12))
    ax.set_xticklabels(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        rotation=45, ha="right", fontsize=12
    )

    # Add gridlines for better readability
    # ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add interactive tooltips
    cursor = mplcursors.cursor(ax, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'Total: ${sel.target[1]:.2f}'))

    # Display the bar chart
    st.pyplot(fig)
    
    # Add data insights - Max spending month
    max_spending_month = total_spending_per_month.idxmax()
    max_spending_amount = total_spending_per_month.max()
    month_names = DateUtils.get_month_names()
    max_spending_month_name = month_names[max_spending_month]
    st.write(f"🏅 Max Spending Month: {max_spending_month_name} with ${max_spending_amount:.2f}")

    return fig

def plot_top_10_category_pie_chart(df, category_column='category', amount_column='amount_paid'):
    """
    Plots a pie chart of the top 10 spending categories for a given year.

    Args:
    - df (DataFrame): The data containing monthly expense information.
    - category_column (str): The name of the column containing categories (default is 'category').
    - amount_column (str): The name of the column containing expense amounts (default is 'amount_paid').
    """
    # Group data by category and sum the expenses
    category_spending = df.groupby(category_column)[amount_column].sum().sort_values(ascending=False).head(10)

    # Create the pie chart with a reduced figure size
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(
        category_spending.values,
        labels=category_spending.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    #ax.set_title('Top 10 Spending Categories for the Year', fontsize=14, fontweight='bold')
    
    # Display the pie chart
    st.pyplot(fig)
    
    # Add data insights
    top_category = category_spending.idxmax()
    top_category_amount = category_spending.max()
    st.write(f"🏅 Top Spending Category: {top_category} (${top_category_amount:.2f})")
    min_category = category_spending.idxmin()
    min_category_amount = category_spending.min()
    st.write(f"⬇️ Lowest Spending Category: {min_category} (${min_category_amount:.2f})")


    # Display the pie chart
    return fig