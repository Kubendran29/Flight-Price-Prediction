import streamlit as st
import pickle
from datetime import datetime

# Load the pre-trained model
model = pickle.load(open("model.pkl", "rb"))

# Dictionaries for categorical variables
airline_dict = {
    "AirAsia": 0,
    "Indigo": 1,
    "GO FIRST": 2,
    "SpiceJet": 3,
    "Air India": 4,
    "Vistara": 5,
}
source_dict = {
    "Delhi": 0,
    "Hyderabad": 1,
    "Bangalore": 2,
    "Mumbai": 3,
    "Kolkata": 4,
    "Chennai": 5,
}
destination_dict = {
    "Delhi": 0,
    "Hyderabad": 1,
    "Mumbai": 2,
    "Bangalore": 3,
    "Chennai": 4,
    "Kolkata": 5,
}
departure_dict = {
    "Early Morning": 0,
    "Morning": 1,
    "Afternoon": 2,
    "Evening": 3,
    "Night": 4,
    "Late Night": 5,
}
arrival_dict = {
    "Early Morning": 0,
    "Morning": 1,
    "Afternoon": 2,
    "Evening": 3,
    "Night": 4,
    "Late Night": 5,
}
stops_dict = {"Zero": 0, "One": 1, "Two or More": 2}
class_dict = {"Economy": 0, "Business": 1}

st.title("Flight Price Prediction App")
st.write("Fill out the details below to predict the flight price.")

# Input Fields with Placeholder Defaults
airline_options = ["Select Airline"] + list(airline_dict.keys())
source_city_options = ["Select Source"] + list(source_dict.keys())
destination_city_options = ["Select Destination"] + list(destination_dict.keys())
departure_time_options = ["Select Departure Time"] + list(departure_dict.keys())
arrival_time_options = ["Select Arrival Time"] + list(arrival_dict.keys())
stops_options = ["Select Stops"] + list(stops_dict.keys())
class_options = ["Select Class"] + list(class_dict.keys())

airline = st.selectbox("Airline", airline_options, index=0)  # Default: "Select Airline"
source_city = st.selectbox(
    "Source City", source_city_options, index=0
)  # Default: "Select Source"
destination_city = st.selectbox(
    "Destination City", destination_city_options, index=0
)  # Default: "Select Destination"
departure_time = st.selectbox(
    "Departure Time", departure_time_options, index=0
)  # Default: "Select Departure Time"
arrival_time = st.selectbox(
    "Arrival Time", arrival_time_options, index=0
)  # Default: "Select Arrival Time"
stops = st.selectbox(
    "Number of Stops", stops_options, index=0
)  # Default: "Select Stops"
travel_class = st.selectbox("Class", class_options, index=0)  # Default: "Select Class"
departure_date = st.date_input(
    "Departure Date", min_value=datetime.today()
)  # Default: Today's date

# Predict Button
if st.button("Predict Price"):
    try:
        # Check for placeholder selections
        if (
            airline == "Select Airline"
            or source_city == "Select Source"
            or destination_city == "Select Destination"
            or departure_time == "Select Departure Time"
            or arrival_time == "Select Arrival Time"
            or stops == "Select Stops"
            or travel_class == "Select Class"
        ):
            st.error("Please fill out all fields before predicting.")
        else:
            # Calculate date difference
            date_diff = (departure_date - datetime.today().date()).days + 1

            # Prepare features
            features = [
                airline_dict[airline],
                source_dict[source_city],
                departure_dict[departure_time],
                stops_dict[stops],
                arrival_dict[arrival_time],
                destination_dict[destination_city],
                class_dict[travel_class],
                date_diff,
            ]

            # Predict the price
            prediction = model.predict([features])[0]
            st.success(f"The predicted flight price is ₹{round(prediction, 2)}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
