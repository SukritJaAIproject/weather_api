import os
import json
import datetime
import requests
import pandas as pd
from wwo_hist import retrieve_hist_data

def wwo_by_date(lat, lon, date, apikey):
  datel, timel, templ, rhl = [], [], [], []
  url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?q="+str(lat)+", "+str(lon) +"&date="+str(start_date)+"&key="+str(apikey)+" &tp=1&format=json"
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

lat, lon = "13.989478999999996", "100.616387" 
date = "2022-01-01"
apikey = "842ff68cf9ba4d5c86c115928222303"
df = wwo_by_date(lat, lon, date, apikey)
df