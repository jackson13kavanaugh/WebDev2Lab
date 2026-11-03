import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Plant Survey", page_icon="🌿")
st.title("Plant Data Collection 🌿")
st.write("Please fill out the form below to add your plant data to our dataset.")

with st.form("survey_form"):
    # Accept user input in the form of a string[span_1](start_span)[span_1](end_span)
    plant_name = st.text_input("What is the name of your plant? (e.g., Monstera, Fern):")
    plant_height = st.text_input("What is the height of your plant in cm? (Enter a number):")

    submitted = st.form_submit_button("Submit Data")

    if submitted:
        if plant_name.strip() and plant_height.strip():
            file_exists = os.path.exists("data.csv") and os.path.getsize("data.csv") > 0
            
            new_data = pd.DataFrame([{
                "Plant_Name": plant_name.strip(), 
                "Height_cm": plant_height.strip()
            }])
            
            # Write all collected data to the provided CSV file data.csv[span_2](start_span)[span_2](end_span)
            new_data.to_csv("data.csv", mode="a", header=not file_exists, index=False)
            
            st.success("Your plant data has been submitted!")
        else:
            st.warning("Please fill out both fields before submitting.")

st.divider()
st.header("Current Data in CSV")

if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    current_data_df = pd.read_csv("data.csv")
    st.dataframe(current_data_df)
else:
    st.info("The 'data.csv' file is empty or does not exist yet.")
