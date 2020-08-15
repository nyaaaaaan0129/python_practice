import requests
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=250010'
data = requests.get(url).json()
print(data)