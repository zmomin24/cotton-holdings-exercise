import datetime as dt
import requests as rq 
import sqlite3 as db

def alerts_count_by_state():

    print("/*** begin function to load data from active alerts count API ***/")

    weatherAlertsUrl = "https://api.weather.gov/alerts/active/count"


    response = rq.get(weatherAlertsUrl).json()
    #print(response)

    areas_counts = response.get('areas',{})
    #print(areas_counts)


    #Set current_timestamp variable so we can insert it into the DB for record creation time
    current_timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    #delete all records from the table so we can load fresh, can remove in future to keep historical data
    sqlCursor.execute("DELETE FROM alerts_by_state")

    for area, count in areas_counts.items():
        '''insert_query = f"INSERT INTO alerts_by_state (state, count_of_alerts, create_ts)"\
        "VALUES ( '{area}','{count}', '{current_timestamp}');"
        print(insert_query)'''

        sqlCursor.execute(f"INSERT INTO alerts_by_state (state, count_of_alerts, create_ts) VALUES (?, ?, ?)", 
                          (area, count, current_timestamp))
    


    connection.commit()

    #sqlCursor.execute("SELECT * FROM alerts_by_state")

    #print(sqlCursor.fetchall())

    connection.close()

    print("/*** end of function to load data from active alerts count API ***/")



#alerts_count_by_state()