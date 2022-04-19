import os
import json
import datetime
import requests
import pandas as pd
from datetime import datetime
from datetime import date
from wwo_hist import retrieve_hist_data

current_date = datetime.today().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
# print("current_date =", current_date, "Current Time =", current_time)

def wwo_curr_data(lat, lon, date, apikey):
  datel, timel, templ, rhl = [], [], [], []
  url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?q="+str(lat)+", "+str(lon) +"&date="+str(date)+"&key="+str(apikey)+" &tp=1&format=json"
  payload, headers={}, {}
  response = requests.request("GET", url, headers=headers, data=payload)
  data = json.loads(response.text)
  dates = data['data']['weather'][0]['date']
  ts = data['data']['weather'][0]['hourly']
  for i in range(len(ts)):
    time = data['data']['weather'][0]['hourly'][i]['time']
    if time[0:2] == current_time[0:2]: 
      tempC = data['data']['weather'][0]['hourly'][i]['tempC']
      rh = data['data']['weather'][0]['hourly'][i]['humidity']
  df = {'date':dates, 'time':current_time, 'temp':tempC, 'rh':rh}   
  return df

lat, lon = "13.989478999999996", "100.616387" 
date = "2022-01-01"
apikey = "842ff68cf9ba4d5c86c115928222303"
df = wwo_curr_data(lat, lon, date, apikey)
df