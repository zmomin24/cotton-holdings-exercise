import datetime as dt
import requests as rq 
import pandas as pd
import sqlite3 as db

def alerts_count_by_state():

    weatherAlertsUrl = "https://api.weather.gov/alerts/active/count"


    response = rq.get(weatherAlertsUrl).json()
    #print(response)

    areas_counts = response.get('areas',{})
    print(areas_counts)

    #df_regions = pd.DataFrame(areas_counts.items(), columns=['Region','Active_Alerts'])
    #print(df_regions)

    current_timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    sqlCursor.execute("DELETE FROM alerts_by_state")
    #sqlCursor.execute("DELETE FROM 'sqlite_sequence' WHERE 'name'='alerts_by_state'")

    for area, count in areas_counts.items():
        insert_query = f"INSERT INTO alerts_by_state (state, count_of_alerts, create_ts)"\
        "VALUES ( '{area}','{count}', '{current_timestamp}');"
        print(insert_query)

        sqlCursor.execute(f"INSERT INTO alerts_by_state (state, count_of_alerts, create_ts) VALUES (?, ?, ?)", 
                          (area, count, current_timestamp))
    


    connection.commit()

    sqlCursor.execute("SELECT * FROM alerts_by_state")

    print(sqlCursor.fetchall())

    connection.close()


alerts_count_by_state()