import json
import time as timesleep
import requests
import datetime
import pandas as pd
from datetime import datetime, timedelta

def his_data_point(lat, lon, start, end, api_key):
  '''
  Data point, Historical data, hourly
  '''
  url = "https://meteostat.p.rapidapi.com/point/hourly"
  querystring, headers = {"lat":lat, "lon":lon, "start":start, "end":end, "tz":"Asia/Bangkok","model":"true"}, {"X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": api_key}
  timesleep.sleep(60)
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  #print(data)
  times, temps, idx, rhs = [], [], [], []
  for i in range(len(data['data'])):
    time, temp, rh = data['data'][i]['time'], data['data'][i]['temp'], data['data'][i]['rhum']
    times.append(time); temps.append(temp); rhs.append(rh);  idx.append(i);
  df = pd.DataFrame({'idx':idx, 'datetime':times, 'temp':temps, 'rh':rhs})
  return df
  
def current_data_point(lat, lon, start, end, api_key, cur_date, cur_time):
  '''
  Data point, Historical data, hourly
  '''
  url = "https://meteostat.p.rapidapi.com/point/hourly"
  querystring, headers = {"lat":lat, "lon":lon, "start":start, "end":end, "tz":"Asia/Bangkok","model":"true"}, {"X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": api_key}
  timesleep.sleep(60)
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  #print(data)
  times, temps, idx, rhs = [], [], [], []
  for i in range(len(data['data'])):
    time, temp, rh = data['data'][i]['time'], data['data'][i]['temp'], data['data'][i]['rhum']
    times.append(time); temps.append(temp); rhs.append(rh);  idx.append(i);
  df = pd.DataFrame({'idx':idx, 'datetime':times, 'temp':temps, 'rh':rhs})
  for i in range(df.shape[0]):
    if df['datetime'][i][11:-6] == cur_time:
      temp, rh = df['temp'][i], df['rh'][i]
    else:
      pass
  return temp, rh

lat, lon = "13.989478999999996", "100.616387"
start, end = "2021-01-01", "2021-01-15"
api_key = "a949fee7f6mshf15640e97c60b31p1a6549jsn36e6b0350757"

cur_date, cur_time = datetime.today().strftime("%Y-%m-%d"), datetime.now().strftime("%H")
print("current_date =", cur_date, "Current Time =", cur_time)

df = his_data_point(lat, lon, start, end, api_key)
print(df)

temp, rh = current_data_point(lat, lon, start, end, api_key, cur_date, cur_time)
print(temp, rh)