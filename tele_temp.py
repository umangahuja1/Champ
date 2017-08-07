import requests

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=ac7c75b9937a495021393024d0a90c44&units=metric');	
	return res.json();

def out_temp(result):
	temp = "{}'s temperature : {}°C ".format(result['name'],result['main']['temp'])
	wind = "Wind speed:{} m/s".format(result['wind']['speed'])
	weather = "Weather:{}".format(result['weather'][0]['main'])
	desc = "Description:{}".format(result['weather'][0]['description'])

	message = "\n".join([temp,wind,weather,desc])
	return message

def temp(lat,lon):
	query='lat='+lat+'&lon='+lon;
	data=weather_data(query);
	return out_temp(data)
