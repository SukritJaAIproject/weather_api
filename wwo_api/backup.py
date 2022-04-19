# import os
# import json
# import datetime
# import requests
# import pandas as pd
# from wwo_hist import retrieve_hist_data

# frequency = 1
# start_date = '11-DEC-2021'
# end_date = '11-MAR-2021'
# api_key = '842ff68cf9ba4d5c86c115928222303'
# location_list = ['13.989478999999996/100.616387'] #Latitude/Longitude (decimal degree)
# hist_weather_data = retrieve_hist_data(api_key, location_list,
#                                 start_date, end_date, frequency, location_label = False, export_csv = True, store_df = True)
# print(hist_weather_data)

# print(data.keys())
# print(data['data'].keys())
# print(data['data']['request'][0])
# print(data['data']['weather'][0])
# print(data['data']['weather'][0]['date'])
# print(data['data']['weather'][0]['astronomy'])
# print(data['data']['weather'][0]['maxtempC'])
# print(data['data']['weather'][0]['mintempC'])
# print(data['data']['weather'][0]['avgtempC'])
# print(data['data']['weather'][0]['hourly'])