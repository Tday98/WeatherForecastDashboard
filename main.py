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

data = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (F)"})
st.plotly_chart(figure)
