########## backup ##########
# print('total:', len(jsonData['days'])) #len = 15, 0-14:t to t+4
# print(len(jsonData['days'][0])) # len = 37 (features)
# print(jsonData['stations']) #รายละเอียดเกี่ยวกับ station
# print(jsonData['currentConditions'])

# print(jsonData['days'][0].keys()) 0-14
# print('datetime:', jsonData['days'][0]['datetime'])
# print('datetimeEpoch:', jsonData['days'][0]['datetimeEpoch'])
# print('tempmax:', jsonData['days'][0]['tempmax'])
# print('tempmin:', jsonData['days'][0]['tempmin'])
# print('temp:', jsonData['days'][0]['temp']) # average temp at day
# print('humidity:', jsonData['days'][0]['humidity'])
# print('solarradiation:', jsonData['days'][0]['solarradiation'])
# print('solarenergy:', jsonData['days'][0]['solarenergy'])
# print('conditions:', jsonData['days'][0]['conditions']) #Rain, Partially cloudy
# print('stations:', jsonData['days'][0]['stations']) # ['VTBS', 'VTBD']

# print(len(jsonData))
# print(jsonData.keys())
# print(jsonData['queryCost'])
# print(jsonData['latitude'], jsonData['longitude'])
# print(jsonData['resolvedAddress'])
# print(jsonData['address'])
# print(jsonData['timezone'])
# print(jsonData['tzoffset'])
# print(jsonData['days'])
# print(len(jsonData['days']))

# # url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
# 13.989478999999996%2C%20100.616387/2022-01-01/2022-01-31
# ?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Clatitude%2Clongitude%2Ctemp&include=obs%2Chours&key=
# Q82HADKP8VA46L5QNL2LJLC4Y&contentType=json"