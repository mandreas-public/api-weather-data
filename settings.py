# Settings


# Time interval in seconds for the API to calls a new record during scheduled pull
# 10 minutes (600 seconds); 60 minutes (3600 seconds)
# Not recommended to be less than 30 minutes since data refreshes on OpenWeather server only every ~30 minutes.
check_interval = 3600

# API URL to pull from
# This is required!
apiURL = 'http://api.openweathermap.org/data/2.5/weather'

#City ID for the API to pull data from.  For more info: http://bulk.openweathermap.org/sample/ and enter file 'city.list.json.gz'
#Fort McMurray = 5955895; Lac La Biche = 6028050
apiCityId = '6028050'

# API response units
# Can be standard, metric or imperial
apiUnits = 'metric'