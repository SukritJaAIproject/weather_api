import json
import requests
import pandas as pd

# b6de4f8f620421cb97ce4fac6fd34180
# 545d49361c74fe17c54806410ef1a738

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

lat, lon, fields = "13.917", "100.600", "tc,rh"
Bearer = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImRhNmJmMGU5ZTBiZGU5ZWI2NjUzMzRjNGIzMjI2MjdkMzhlMDk4ZTIzZmQ5YTZhYTg5N2VmNjRhMjA1MzYzNWU1NTAyMTMxOGM5N2I0OGVhIn0.eyJhdWQiOiIyIiwianRpIjoiZGE2YmYwZTllMGJkZTllYjY2NTMzNGM0YjMyMjYyN2QzOGUwOThlMjNmZDlhNmFhODk3ZWY2NGEyMDUzNjM1ZTU1MDIxMzE4Yzk3YjQ4ZWEiLCJpYXQiOjE2NDk0MDE0MDcsIm5iZiI6MTY0OTQwMTQwNywiZXhwIjoxNjgwOTM3NDA3LCJzdWIiOiIzODkiLCJzY29wZXMiOltdfQ.vjoiRxPJwC3k-6NvDibqOcfN6R1TDvyjdW3B79inIVGIeJnghhKLedSTA-NLctcVJ4mP0eEY4pWfHyT5Ldn5DbdrTRrU-ATHsqHwLPhxwRG9ucx2494Gq1n2WDuKeBH8RsTzGedMOKSMgGtKYCbBZuOUPO8uDKXJzihOyYL08Z1XHvDegFG-nB_Yq24rWrAOHsL-hY0hrwexBjL6dXIXTGz_EgVlLnf57W-YuI08bOY7Gh2nqqwdtr3C1uv-v_SMp0XLuVzPwrEcbPXFxGby15QEoeKLfxlnNPX5tc0FO9Wglyswny5zqU_almZz_upgJB_Kj2Xw5M2O3IK6MFA6znXR1tQxZOCnsrI95ittzucbK5CoWVoIaoxOA-KA8d_gnXI-lCS0E-Fi-JYWrZZMKKyIu8fGNdUvYVgzUvRT3T2argyUa7xmnoDomlgDrPrN20yak7HGyLnrvFw0iD4X78uiphfw2etlWnkQPrTtd22cvTVUzyoVReGCqO4g1abmxEWrS8_glZnT_H9VG6pa1vThak3rwDJPm150UhE5rBHt5x_K8B56TkdAePRToAAwrOfIHNlRvQ4LtfC-5Tn7Go913A8H94fGge5sThZ17ELc-6q7plkPqFe2pjmK-sHEPMkLMu2lhXfz2QHUFAob7Q5qLdVUw-ykTouoz7XVoAM"
result = tmd_forecast(Bearer, lat, lon, fields)
print(result)