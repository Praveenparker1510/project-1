import streamlit as st
import pandas as pd
import mysql.connector

# MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="RED_BUS_DETAILS"
    )

# Function to load data from the MySQL database
def load_data():
    conn = create_connection()
    query = "SELECT * FROM bus_details"
    return pd.read_sql(query, conn)

# Load data
data = load_data()

# Streamlit application
st.title("Redbus Information Dashboard")

# Add a video (you can use a YouTube link or local file)
st.video("https://youtu.be/eyAAUGhvZu8?si=U5PiwQkDpirTJaHO")  # Replace with actual Redbus video link

# Route filter (initial filter)
route_name = st.sidebar.selectbox("Select Route", options=data['Route_Name'].unique())

# Filter the data based on the selected route
filtered_data_by_route = data[data['Route_Name'] == route_name]

# Optional Bus name filter (only shows buses for the selected route, but can be skipped)
busname = st.sidebar.selectbox(
    "Bus Name (optional)", 
    options=["All"] + list(filtered_data_by_route['Bus_Name'].unique()), 
    index=0
)

# Optional Bus type filter (only shows bus types for the selected route and bus, can be skipped)
bustype = st.sidebar.selectbox(
    "Bus Type (optional)", 
    options=["All"] + list(filtered_data_by_route['Bus_Type'].unique()), 
    index=0
)

# Price filter
Price_range = st.sidebar.slider("Price Range", min_value=0, max_value=int(filtered_data_by_route['Price'].max()), value=(0, int(filtered_data_by_route['Price'].max())))

# Star rating slider
Star_Rating_Range = st.sidebar.slider(
    "Ratings",
    min_value=0.0,
    max_value=5.0,
    value=(0.0, 5.0),
    step=0.1
)

# Seat availability slider
Seat_availability_range = st.sidebar.slider(
    "Seats Available",
    min_value=0,
    max_value=int(filtered_data_by_route['Seats_Available'].max()),
    value=(0, int(filtered_data_by_route['Seats_Available'].max()))
)

# Apply filters based on selected route, and optionally selected bus name, bus type, price, star rating, and seat availability
filtered_data = filtered_data_by_route.copy()

if busname != "All":
    filtered_data = filtered_data[filtered_data['Bus_Name'] == busname]  # Filter by bus name if selected

if bustype != "All":
    filtered_data = filtered_data[filtered_data['Bus_Type'] == bustype]  # Filter by bus type if selected

# Filter by price range, star rating, and seat availability
filtered_data = filtered_data[
    (filtered_data['Price'] >= Price_range[0]) & (filtered_data['Price'] <= Price_range[1])
]
filtered_data = filtered_data[
    (filtered_data['Ratings'] >= Star_Rating_Range[0]) & (filtered_data['Ratings'] <= Star_Rating_Range[1])
]
filtered_data = filtered_data[
    (filtered_data['Seats_Available'] >= Seat_availability_range[0]) & (filtered_data['Seats_Available'] <= Seat_availability_range[1])
]

# Display filtered data
st.subheader(f"Bus Details for Route: {Route_Name}")
st.write(filtered_data)