import streamlit as st
from utils import DateUtils  # Import the utility class

def month_selector():
    """Provides a dropdown to select a month."""
    month_names = DateUtils.get_month_names()
    return st.selectbox(
        'Choose a Month for Detailed View:',
        options=list(month_names.keys()),
        format_func=lambda x: month_names[x]
    )

def chart_selector(heading, key, default_value):
    """Provides a dropdown to select chart type."""
    return st.selectbox(
        heading,
        ['Bar Chart', 'Pie Chart'],
        index=['Bar Chart', 'Pie Chart'].index(default_value),
        key=key
    )