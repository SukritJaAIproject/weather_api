import os
import json
import datetime
import requests
import pandas as pd
from wwo_hist import retrieve_hist_data

def wwo_his_data(lat, lon, start_day, end_day, apikey):
  datel, timel, templ, rhl, days = [], [], [], [], []
  for i in range(start_day, end_day):
    days.append(datetime.date(2021, 1, i).strftime('%Y-%m-%d')) 
  for start_hisdate in days:
    url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?q="+str(lat)+", "+str(lon) +"&date="+str(start_hisdate)+"&key="+str(apikey)+" &tp=1&format=json"
    payload, headers={}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    dates = data['data']['weather'][0]['date']
    ts = data['data']['weather'][0]['hourly']
    for i in range(len(ts)):
      time = data['data']['weather'][0]['hourly'][i]['time']
      tempC = data['data']['weather'][0]['hourly'][i]['tempC']
      rh = data['data']['weather'][0]['hourly'][i]['humidity']
      datel.append(dates); timel.append(time);
      templ.append(tempC); rhl.append(rh);
    df = pd.DataFrame({'date':datel, 'time':timel, 'temp':templ, 'rh':rhl})
  return df

start_day, end_day = 1, 16
lat, lon = "13.989478999999996", "100.616387" 
apikey = "842ff68cf9ba4d5c86c115928222303"
df = wwo_his_data(lat, lon, start_day, end_day, apikey)
df