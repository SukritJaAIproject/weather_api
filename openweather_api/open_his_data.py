import json
import datetime
import calendar
import requests
import pandas as pd
from google.colab import files
from datetime import datetime, timedelta

'''
requested time is out of allowed range of 5 days back
'''

def daterange(start_date, end_date):
    delta = timedelta(hours=1)
    while start_date < end_date:
        yield start_date
        start_date += delta

def gen_utc_time(start_date, end_date):
  days, datetime_str = [], []
  for single_date in daterange(start_date, end_date):
      time_str = single_date.strftime("%Y-%m-%d %H:%M")
      utc_time = calendar.timegm(single_date.utctimetuple())
      # print('datetime:', time_str, ' UTC:', utc_time)
      days.append(utc_time); datetime_str.append(time_str);
      result = pd.DataFrame({'datetime': datetime_str, 'UTC': days})
  return result

def open_his_data(lat, lon, appid, start2end):
  items, temps, humiditys = [], [], []
  for item in start2end['UTC'].tolist():
    url = "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+str(lat)+"&lon="+str(lon)+"&dt="+str(item)+"&appid="+str(appid)
    payload, headers={}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)   # print(data); print(len(data['hourly']));
    temp, humidity = data['current']['temp'], data['current']['humidity']
    items.append(item); temps.append(temp); humiditys.append(humidity);
    # for i in range(len(data['hourly'])):
    #   temp, humidity = data['hourly'][i]['temp'], data['hourly'][i]['humidity']
    #   items.append(item); temps.append(temp); humiditys.append(humidity);
  df = pd.DataFrame({'datetime':start2end['datetime'].tolist(),'utc':items, 'humidity':humiditys, 'temp':temps })
  return df

def current(lat, lon, appid, time_str, utc_time):
  url = "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+str(lat)+"&lon="+str(lon)+"&dt="+str(utc_time)+"&appid="+str(appid)
  payload, headers={}, {}
  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)  
  temp, rh = data['current']['temp'], data['current']['humidity']
  result = {'datetime':time_str, 'utc':utc_time, 'humidity':rh, 'temp':temp }
  return result


# api_key = "8381cc3e55e90efdcc62d73fa8fc5d3a"'
# api_key = "b6710939254546da2f0de859db4c44d4"'
# api_key = "283019a4b61eafae7824e4d94b8f1926"'

start_date, end_date = datetime(2022, 4, 17, 00, 00), datetime(2022, 4, 21, 00, 00)
start2end = gen_utc_time(start_date, end_date)
lat, lon, appid = "13.917", "100.600", "b6710939254546da2f0de859db4c44d4"

## Historical data
# df = open_his_data(lat, lon, appid, start2end)
# print(df)

## Current data
dtime = datetime(2022, 4, 21, 00, 00).strftime("%Y-%m-%d %H:%M")
utc = calendar.timegm(datetime(2022, 4, 21, 00, 00).utctimetuple())
result = current(lat, lon, appid, dtime, utc)
print('result', result)