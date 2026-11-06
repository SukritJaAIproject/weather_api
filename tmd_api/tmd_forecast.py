import json
import requests
import pandas as pd

# YOUR_API_KEY
# YOUR_API_KEY

def tmd_forecast(Bearer, lat, lon, fields):
  url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly"
  headers = { 'accept': "application/json", 'authorization': Bearer,}
  response = requests.request("GET", url, headers=headers)
  r = json.loads(response.text); # print(r['hourly_data'])
  startd = r['hourly_data']['min'][11:-12] # print(startd)
  url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/at"
  date, hour, duration = "2022-04-20", startd, 8
  querystring = {"lat":lat, "lon":lon, "fields":fields, "date":date, "hour":hour, "duration":duration}
  headers = {'accept': "application/json", 'authorization': Bearer,}
  response = requests.request("GET", url, headers=headers, params=querystring)
  # print(response.text)
  return response.text

# lat, lon, fields = "13.917", "100.600", "tc,rh"
# Bearer = "Bearer YOUR_TOKEN"
# result = tmd_forecast(Bearer, lat, lon, fields)
# print(result)
