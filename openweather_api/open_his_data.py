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

start_date, end_date = datetime(2022, 4, 17, 00, 00), datetime(2022, 4, 21, 00, 00)
start2end = gen_utc_time(start_date, end_date)
lat, lon, appid = "13.917", "100.600", "8381cc3e55e90efdcc62d73fa8fc5d3a"
df = open_his_data(lat, lon, appid, start2end)
df