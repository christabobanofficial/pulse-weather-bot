import requests
from datetime import datetime

url = "https://wttr.in/?format=j1"

data = requests.get(url).json()

temp = data["current_condition"][0]["temp_C"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]

report = f"""
Weather Report
Date: {datetime.now()}

Temperature: {temp}°C
Condition: {weather}
Humidity: {humidity}%
"""

print(report)

with open("weather_report.txt", "w") as file:
    file.write(report)
print("Report saved successfully!")