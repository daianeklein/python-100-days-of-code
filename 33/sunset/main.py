import requests
from datetime import datetime

time_now = datetime.now()

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

#your position is within +5 or -5 degrees of the ISS position

parameters = {
    'lat' : MY_LAT,
    'log' : MY_LONG,
    'formatted' : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(iss_latitude, iss_longitude, sunrise, sunset, time_now)
