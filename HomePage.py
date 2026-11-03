# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🌿",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to the Houseplant Data Dashboard! 🌿")

# INTRODUCTORY TEXT
st.write("""
This application is designed to collect and visualize data about houseplant care schedules and growth heights.
You can navigate to the different pages using the sidebar on the left.

### How to use this app:
- **Survey Page**: Go here to input new plant data into our CSV file.
- **Visuals Page**: Go here to see the houseplant data visualized in static and dynamic graphs.

This project is part of CS 1301's Lab 2.
""")


