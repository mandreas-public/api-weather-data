# libraries
import pandas as pd 
from sqlalchemy import create_engine
import sqlite3

def saveCsv(df):
    # Function edits a CSV file and saves it with the data
    try:
        dfOld = pd.read_csv('data/weatherdata.csv', index_col=False)
        print('Opened CSV.')
    except:
        print('CSV does not exist.')
        dfOld = pd.DataFrame()

    dfNew = dfOld.append(df, ignore_index=True)
    dfNew.to_csv('data/weatherdata.csv', index=False)

def appendDB(df):
    # Function to append the database entries
    engine = create_engine('sqlite:///data/weatherdata.db', echo=False)
    sqlite_connection = engine.connect()
    
    sqlite_table = 'weather'
    df.to_sql(sqlite_table, sqlite_connection, if_exists='append')
