import json
import requests
import pandas as pd
from datetime import datetime, date

current_date = datetime.today().strftime("%Y-%m-%d")
current_time = datetime.now(pytz.timezone('Asia/Bangkok')).strftime("%H:%M:%S")
# print("current_date =", current_date, "Current Time =", current_time)

lat, lon = "13.989478999999996", "100.616387"
apikey ="a949fee7f6mshf15640e97c60b31p1a6549jsn36e6b0350757"

def nearby_stations_get_data(lat, lon, apikey, current_date, current_time):
  '''
  Nearby Stations, Current data
  '''
  url = "https://meteostat.p.rapidapi.com/stations/nearby"
  querystring, headers = {"lat":lat,"lon":lon}, { "X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": apikey}
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  id, name, dis = data['data'][0]['id'], data['data'][0]['name']['en'], data['data'][0]['distance']/1000

  today = str(date.today())
  url1 = "https://meteostat.p.rapidapi.com/stations/hourly"
  querystring = {"station": str(id),"start": today,"end":today,"tz":"Asia/Bangkok","model":"true"}
  headers = { "X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": apikey}
  response = requests.request("GET", url1, headers=headers, params=querystring)
  data = json.loads(response.text)
  for i in range(len(data['data'])):
    time, temp, rh = data['data'][i]['time'], data['data'][i]['temp'], data['data'][i]['rhum']
    if time[-8:-6] == current_time[0:2]:
        # print('time', time[-8:-6], 'current_time', current_time[0:2])
        print('datetime: ', time, 'current_time: ', current_time , 'Temp: ', temp, 'humidity: ', rh)
        # result = {'datetime':datetimes, 'current_time':current_time , 'Temp':temp, 'humidity':rh}  
        result = {'time':time, 'temp':temp, 'rh':rh}
  return result

lat, lon = 13.989478999999996, 100.616387
result = nearby_stations_get_data(lat, lon, apikey, current_date, current_time)
result