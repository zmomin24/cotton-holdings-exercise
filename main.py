import datetime as dt
import requests as rq 
import pandas as pd


weatherAlertsUrl = "https://api.weather.gov/alerts"


response = rq.get(weatherAlertsUrl).json()
print(response)

#data = pd.json_normalize(response["features"],["properties","areasAffected"],["id","type","geometry.type","geometry.coordinates","properties.headline","properties.description","properties.instruction","properties.event","properties.severity","properties.urgency","properties.certainty","properties.expires"],record_prefix="area_")
#data = pd.json_normalize(response,"features",["properties","id","type"],errors="ignore")

#print(data.head(2))

#print(pd.json_normalize(response))

if 'features' in response and response['features']:
    df = pd.json_normalize(response['features'])

    print(df.head())

    properties_columns = [col for col in df.columns if col.startswith('properties.')]
    properties_df = df[properties_columns]

    print(properties_df.head())
else:
    print("no features found in response")
