# libraries
import requests
import pandas as pd
import io
from datetime import datetime
import json
import pytz
import time

# app files
import settings
import connections
import secret


def apiCall():
    #API communication to the service
    print('\nRunning API Call\n')
    url = settings.apiURL

    querystring = {
        "appid":secret.apiKey,
        "id":settings.apiCityId,
        "units":settings.apiUnits
        }

    response = requests.request("GET", url, params=querystring)
    modifyData(response)

def modifyData(response):
    # Formats data into a cleaner string
    urlData = response.json()
    df = pd.json_normalize(urlData)

    df.rename(columns={'id': 'city-id'}, inplace=True)

    df = pd.concat([pd.DataFrame([y for x in df['weather'].values.tolist() for y in x]), df], axis=1)
    df.drop('weather', axis=1, inplace=True)

    dtcol = ['dt','sys.sunrise','sys.sunset']
    for col in dtcol:
        df[col] = datetime.utcfromtimestamp(int(df[col])).strftime('%Y-%m-%d %H:%M:%S')
        df[col] = pd.to_datetime(df[col]).dt.tz_localize(pytz.utc).dt.tz_convert('America/Edmonton')
        df[col] = df[col].astype(str).str[:-6].astype('datetime64')
        
    dt = df['dt']
    df.drop(labels=['dt'], axis=1,inplace = True)
    df.insert(0, 'dt', dt)

    cols = ['dt','main','description','visibility','city-id','name','cod','coord.lon','coord.lat','main.temp','main.feels_like',
            'main.pressure','main.humidity','wind.speed','wind.deg','wind.gust','clouds.all','rain.1h','snow.1h','sys.sunrise','sys.sunset']
    newdf = pd.DataFrame(columns=cols)
    newdf = newdf.append(df)
    df = newdf[cols]

    print('Success.  Database record: \n')
    print(df.iloc[0])

    connections.saveCsv(df)
    connections.appendDB(df)


def apiLoop():
    # The loop to call the API on a schedule
    while True:

        try:
            apiCall()
            
            print('\nSleeping for '+str(settings.check_interval/60)+' minutes')
            time.sleep(settings.check_interval)
        except Exception as e:
            print(e, '\nError! Trying again in 30 seconds..')
            time.sleep(30)
            continue


def mainLoop():
    # Initiailized menu loop
    while True:
        option = input("""

         Weather API Data Pull by: Mark Andreas
                                                  
         1. Pull Current Weather                           
         2. Set Pulls Into Background on a Schedule                          
         3. Exit                                                                                   
        
             Option: """)                             

        if option == '1':
            apiCall()

        elif option == '2':
            apiLoop()

        elif option == '3':
            exit()
        
        else:
            print('\nThis is not an option!')
if __name__ == '__main__':
    mainLoop()

