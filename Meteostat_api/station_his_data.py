import json
import requests
import pandas as pd

def station_his_data(station, start, end, tz, api_key):
  '''
  Historical data, Station Data, hourly
  '''
  url = "https://meteostat.p.rapidapi.com/stations/hourly"
  querystring, headers = {"station":station, "start":start, "end":end, "tz":tz, "model":"true"}, { "X-RapidAPI-Host": "meteostat.p.rapidapi.com", "X-RapidAPI-Key": api_key }
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  times, temps, rhs, idx = [], [], [], []
  for i in range(len(data['data'])):
    time, temp, rh = data['data'][i]['time'], data['data'][i]['temp'], data['data'][i]['rhum']
    times.append(time)
    temps.append(temp); rhs.append(rh);
    idx.append(i)
  df = pd.DataFrame({'idx':idx, 'datetime':times, 'temp':temps, 'rh':rhs })
  return df

station = "48456"
start, end, tz = "2021-01-01", "2021-01-15", "Asia/Bangkok"
api_key = "a949fee7f6mshf15640e97c60b31p1a6549jsn36e6b0350757"
df = station_his_data(station, start, end, tz, api_key)
print(df)