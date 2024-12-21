import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def plot_category_spending(monthly_data, chart_type):
    """Visualizes spending by category."""
    category_spending = monthly_data.groupby('category')['amount_paid'].sum().sort_values(ascending=False)
    
    if chart_type == 'Bar Chart':
        st.subheader('📊 Total Spending by Category')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=category_spending.index, y=category_spending.values, ax=ax)
        ax.set_title('Total Spending by Category')
        ax.set_ylabel('Amount Paid')
        ax.set_xlabel('Category')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)

    elif chart_type == 'Pie Chart':
        st.subheader('🥧 Spending Distribution by Category')
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            category_spending.values,
            labels=category_spending.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=sns.color_palette('pastel')
        )
        ax.set_title('Spending Distribution by Category')
        st.pyplot(fig)


def plot_monthly_trends(df):
    """Visualizes monthly spending trends."""
    st.subheader('📈 Monthly Spending Trends')
    monthly_trends = df.groupby('month')['amount_paid'].sum().reset_index()
    max_month = monthly_trends.loc[monthly_trends['amount_paid'].idxmax()]
    min_month = monthly_trends.loc[monthly_trends['amount_paid'].idxmin()]

    fig = px.line(
        monthly_trends,
        x='month',
        y='amount_paid',
        markers=True,
        title='Monthly Spending Trends',
        labels={'month': 'Month', 'amount_paid': 'Total Amount Paid ($)'}
    )
    fig.update_traces(line=dict(color='royalblue', width=2), marker=dict(size=8))
    fig.add_annotation(
        x=0.5, y=1.15, xref='paper', yref='paper',
        text=f"📈 Max Spending: Month {int(max_month['month'])} - ${max_month['amount_paid']:.2f}",
        showarrow=False, font=dict(size=12, color='black')
    )
    fig.add_annotation(
        x=0.5, y=1.08, xref='paper', yref='paper',
        text=f"📉 Min Spending: Month {int(min_month['month'])} - ${min_month['amount_paid']:.2f}",
        showarrow=False, font=dict(size=12, color='black')
    )
    st.plotly_chart(fig, use_container_width=True)
