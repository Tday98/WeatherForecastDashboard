import pandas as pd
import requests

API_KEY = SECRET_KEY
def get_data(place, forecast_days, kind):
    """
    get_data runs a request on the OpenWeather API
    with that it pulls the weather data from the JSON
    and returns that data to the graph to be displayed on the webpage
    :param place:
    :param forecast_days:
    :param kind:
    :return filtered_data:
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
