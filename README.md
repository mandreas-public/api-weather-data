# api-weather-data
Pulls data from a public weather API on a timer schedule - no CRON job required!


Pulls data from the OpenWeatherMap API and saves it to a database

# How to use
## First
1. Clone the repo 
2. Obtain a free API key from OpenWeatherMap
3. Create a file called secret.py
4. Add the line apiKey = '[yourAPIKey here]'
5. Edit settings.py - change apiCityId to the city you would like data for (instructions in the file)

## Then
1. run the file main.py in a console window: "python main.py"
2. Either do a single API pull (Option 1) or set it onto a schedule and put the app into the background (Option 2)
