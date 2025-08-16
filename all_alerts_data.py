import datetime as dt
import requests as rq 
import sqlite3 as db

def all_alerts_data():

    activeWeatherAlertUrl = "https://api.weather.gov/alerts/active"

    response = rq.get(activeWeatherAlertUrl).json()
    #print(response)

    weather_alerts = response.get('features',{})
    #print(weather_alerts)

    cleaned_alerts = []
    for alert in weather_alerts:
        properties = alert.get('properties',{})
        area_desc = properties.get('areaDesc','')

        #Split state from areaDesc and save it separately and assume is is always 2 characters and uppercase
        states = {word.strip() for word in area_desc.replace(';',' ').split() if len(word.strip())==2 and word.strip().isupper()}

        # if not state found then store as null
        if states:
            for state in states:
                cleaned_alerts.append({
                    'id': properties.get('id',''),
                    'event': properties.get('event',''),
                    'severity': properties.get('severity',''),
                    'urgency': properties.get('urgency',''),
                    'state': state,
                    'sent': properties.get('sent',''),
                    'expires': properties.get('expires','')
                })
        else:
            cleaned_alerts.append({
                'id': properties.get('id',''),
                'event': properties.get('event',''),
                'severity': properties.get('severity',''),
                'urgency': properties.get('urgency',''),
                'state': None,
                'sent': properties.get('sent',''),
                'expires': properties.get('expires','')
            })

    print(cleaned_alerts[10])  # Print keys of the first alert for verification

    current_timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    sqlCursor.execute("DELETE FROM all_alerts_data")

    for alert in cleaned_alerts:
        #print(alert['id'], alert['event'], alert['severity'], alert['urgency'], alert['state'], alert['sent'], alert['expires'])
        alert_id = alert['id']
        alert_event = alert['event']
        alert_severity = alert['severity']
        alert_urgency = alert['urgency']
        alert_state = alert['state']
        alert_sent = alert['sent']
        alert_expires = alert['expires']


        sqlCursor.execute(f"INSERT INTO all_alerts_data (id, event, severity, urgency, state,"\
                           "sent_ts, expire_ts, record_create_ts) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                          (alert_id, alert_event, alert_severity, alert_urgency, alert_state, alert_sent, alert_expires, current_timestamp))

    connection.commit()

    sqlCursor.execute("SELECT * FROM all_alerts_data")

    print(sqlCursor.fetchall())

    connection.close()

all_alerts_data()

