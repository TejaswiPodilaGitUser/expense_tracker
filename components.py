import streamlit as st

def month_selector():
    """Provides a dropdown to select a month."""
    return st.selectbox(
        'Select a Month to Filter Data:',
        options=list(range(1, 13)),
        format_func=lambda x: f"Month {x}"
    )

def chart_selector():
    """Provides a dropdown to select chart type."""
    return st.selectbox(
        "Choose a chart type:",
        ('Bar Chart', 'Pie Chart')
    )
