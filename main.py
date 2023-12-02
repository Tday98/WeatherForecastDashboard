import streamlit as st
import plotly.express as px
from backend import get_data

# Creating widgets with streamlit for dashboard
st.title("Weather Forecast for the Selected Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days (up to 5)")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Creating chart which will pull data from the API and show to user
if place:
    try:
        filtered_data = get_data(place, days, option)
        if option == "Temperature":
            # Temperature data is in Kelvin converted it to Fahrenheit in list comprehension
            temperatures = [((dict["main"]["temp"] - 273.15) * (9/5) + 32) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Create temperature graph
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Create dictionary with weather type images from folder and display to webpage
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=120)
    except KeyError:
        st.text("Place either does not exist or there was a typo.")