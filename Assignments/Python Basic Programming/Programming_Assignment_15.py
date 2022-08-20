import meteostat

city = 'Austin'

url = 'http://history.openweathermap.org/data/2.5/history/city?q={}&appid=868578b759351920249babe6fc715fc9'.format{city}

res= requests.get(url)

data =res.json()

print(data)

