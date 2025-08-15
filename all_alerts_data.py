import datetime as dt
import requests as rq 
import pandas as pd
import sqlite3 as db

def all_alerts_data():

    activeWeatherAlertUrl = "https://api.weather.gov/alerts/active"

    response = rq.get(activeWeatherAlertUrl).json()
    #print(response)

    weather_alerts = response.get('features',{})
    print(areas_counts)