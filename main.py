import datetime as dt
import requests as rq 
import sqlite3 as db
import pandas as pd



def get_query_results():

    connection = db.connect("cotton.db")

    sqlCursor = connection.cursor()

    
    '''sqlCursor.execute("select state, sum(count_of_alerts) as total_alerts "\
                      "from alerts_by_state "\
                      "group by state "\
                      "order by total_alerts desc")'''
    
    #Query to return total alerts by state
    print(pd.read_sql_query("select state, sum(count_of_alerts) as total_alerts "\
                      "from alerts_by_state "\
                      "group by state "\
                      "order by total_alerts desc",connection))
    
    

get_query_results()
