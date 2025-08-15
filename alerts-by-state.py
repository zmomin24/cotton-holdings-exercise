import datetime as dt
import requests as rq 
import pandas as pd

def get_alert_counts():

    weatherAlertsUrl = "https://api.weather.gov/alerts/active/count"


    response = rq.get(weatherAlertsUrl).json()
    print(response)

    areas_counts = response['areas']

    df_regions = pd.DataFrame(areas_counts.items(), columns=['Region','Active_Alerts'])
    print(df_regions.head())

    

get_alert_counts()