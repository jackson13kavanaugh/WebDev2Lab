import os
import json
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.title("Houseplant Visualizations 🪴")

# ==========================================
# PART 1: JSON VISUALIZATIONS
# ==========================================
st.header("Part 1: JSON Data (Pre-existing Plants)")

# Must use data from JSON file[span_9](start_span)[span_9](end_span)
try:
    with open("data.json", "r") as infile:
        plant_data = json.load(infile)
    df_json = pd.DataFrame(plant_data)

    # Static Visualisation[span_10](start_span)[span_10](end_span)
    st.subheader("Static Chart: Days Between Watering")
    st.bar_chart(df_json, x="Plant", y="Watering_Days")

    # Dynamic Visualisation[span_11](start_span)[span_11](end_span)
    st.subheader("Dynamic Chart: Plant Height Filter")
    
    # Session States[span_12](start_span)[span_12](end_span)
    if "max_height_json" not in st.session_state:
        st.session_state.max_height_json = 50.0
    if "prev_mean" not in st.session_state:
        st.session_state.prev_mean = 0.0
    if "prev_median" not in st.session_state:
        st.session_state.prev_median = 0.0

    # User input/interaction[span_13](start_span)[span_13](end_span)
    st.session_state.max_height_json = st.slider(
        "Select maximum plant height (inches):",
        min_value=0.0,
        max_value=100.0,
        value=float(st.session_state.max_height_json)
    )

    filtered_json = df_json[df_json["Max_Height_Inches"] <= st.session_state.max_height_json]

    # Extra Credit: Display how summary statistics update as visualization changes[span_14](start_span)[span_14](end_span)
    if len(filtered_json) > 0:
        current_mean = round(float(filtered_json["Max_Height_Inches"].mean()), 1)
        current_median = round(float(filtered_json["Max_Height_Inches"].median()), 1)
        
        col1, col2 = st.columns(2)
        col1.metric("Mean Height", current_mean, round(current_mean - st.session_state.prev_mean, 1))
        col2.metric("Median Height", current_median, round(current_median - st.session_state.prev_median, 1))
        
        st.session_state.prev_mean = current_mean
        st.session_state.prev_median = current_median

    # Advanced visualization with title and labeled axes[span_15](start_span)[span_15](end_span)
    scatter_chart = alt.Chart(filtered_json).mark_circle(size=100).encode(
        x=alt.X("Watering_Days", title="Watering Interval (Days)"),
        y=alt.Y("Max_Height_Inches", title="Max Height (Inches)"),
        tooltip=["Plant", "Category"]
    ).properties(title="Watering Interval vs Height")
    st.altair_chart(scatter_chart, use_container_width=True)

except FileNotFoundError:
    st.error("data.json not found. Please ensure it exists in the main folder.")

# ==========================================
# PART 2: CSV VISUALIZATIONS
# ==========================================
st.divider()
st.header("Part 2: CSV Data (User Submitted Plants)")

# Must use data from CSV file[span_16](start_span)[span_16](end_span)
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    df_csv = pd.read_csv("data.csv")
    df_csv.columns = df_csv.columns.str.strip()
    
    if "Height_cm" in df_csv.columns:
        df_csv["Height_cm"] = pd.to_numeric(df_csv["Height_cm"], errors="coerce").fillna(0)

        # Static Visualisation (Advanced Element)[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span)
        st.subheader("Static Chart: Height by Plant Name")
        fig, ax = plt.subplots()
        ax.bar(df_csv["Plant_Name"], df_csv["Height_cm"], color="forestgreen")
        
        # Include a title and labeled axes[span_19](start_span)[span_19](end_span)
        ax.set_title("Reported Plant Heights")
        ax.set_xlabel("Plant Name")
        ax.set_ylabel("Height (cm)")
        st.pyplot(fig)

        # Dynamic Visualisation
        st.subheader("Dynamic Chart: Filter by Minimum Height")
        
        # Session States for Slider and Extra Credit metrics[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span)
        if "min_height_csv" not in st.session_state:
            st.session_state.min_height_csv = 0.0
        if "prev_mean_csv" not in st.session_state:
            st.session_state.prev_mean_csv = 0.0
        if "prev_median_csv" not in st.session_state:
            st.session_state.prev_median_csv = 0.0
            
        # User input/interaction
        st.session_state.min_height_csv = st.slider(
            "Select minimum plant height (cm):",
            min_value=0.0,
            max_value=200.0,
            value=float(st.session_state.min_height_csv)
        )

        filtered_csv = df_csv[df_csv["Height_cm"] >= st.session_state.min_height_csv]
        
        # Extra Credit: Display how summary statistics update as visualization changes[span_4](start_span)[span_4](end_span)
        if len(filtered_csv) > 0:
            current_mean = round(float(filtered_csv["Height_cm"].mean()), 1)
            current_median = round(float(filtered_csv["Height_cm"].median()), 1)
            
            col1, col2 = st.columns(2)
            col1.metric("Mean Height (cm)", current_mean, round(current_mean - st.session_state.prev_mean_csv, 1))
            col2.metric("Median Height (cm)", current_median, round(current_median - st.session_state.prev_median_csv, 1))
            
            st.session_state.prev_mean_csv = current_mean
            st.session_state.prev_median_csv = current_median
        else:
            st.write("No plants match the selected filter.")

        st.scatter_chart(filtered_csv, x="Plant_Name", y="Height_cm")
    else:
        st.warning("Please submit data using the Survey page.")
else:
    st.info("No survey data found. Please complete the Survey first.")

