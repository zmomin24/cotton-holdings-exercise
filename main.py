import datetime as dt
import requests as rq 
import sqlite3 as db
import pandas as pd
from database import create_db
from alerts_by_state import alerts_count_by_state
from all_alerts_data import all_alerts_data



def get_query_results():

    connection = db.connect("cotton.db")

    print()
    print()
    #Was going to use this but cant format the output so used pandas instead
    '''sqlCursor.execute("select state, sum(count_of_alerts) as total_alerts "\
                      "from alerts_by_state "\
                      "group by state "\
                      "order by total_alerts desc")'''
    
    #Query to return total alerts by state
    print("----- Total Alerts by State -----")
    print(pd.read_sql_query("select state, sum(count_of_alerts) as total_alerts "\
                            "from alerts_by_state "\
                            "group by state "\
                            "order by total_alerts desc",connection))
    print()
    print()

    #Query to return top 10 states by alerts
    #I could have used LIMIT 10 but using row_number to demonstrate window functions
    print("----- Top 10 States by Alerts -----")
    print(pd.read_sql_query("with alert_rank as "\
                            "(select state, "\
                            "sum(count_of_alerts)  as total_alerts, "\
                            "row_number () over (order by sum(count_of_alerts) desc) as row_num "\
                            "from alerts_by_state "\
                            "group by state "\
                            "order by total_alerts desc) "\
                            "select state, total_alerts "\
                            "from alert_rank "\
                            "where row_num <=10",connection))
    print()
    print()

    #Query to return alert count by state and event type
    print("----- Alert Count by State and Event Type -----")
    print(pd.read_sql_query("select state, "\
			                "event, "\
			                "count(*)  as alert_count "\
                            "from all_alerts_data "\
                            "group by state, event "\
                            "order by state desc",connection))
    print()
    print()

    #Query to return average duration (expiry minus sent) of alert by event type in minutes
    print("----- Average Alert Duration by Event Type in Minutes -----")
    print(pd.read_sql_query("select event, " \
                            "avg((julianday(expire_ts) - julianday(sent_ts))*24*60) "\
                            "as avg_alert_duration_in_minutes "\
                            "from all_alerts_data "\
                            "where expire_ts is not null and sent_ts is not null "\
                            "group by event "\
                            "order by avg_alert_duration_in_minutes desc",connection))
    
    

#get_query_results()
if __name__ == "__main__":
    create_db()
    alerts_count_by_state()
    all_alerts_data()
    get_query_results()
print("----- Program Completed -----")

