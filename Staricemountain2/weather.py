import requests
import config
# types
from pydantic import BaseModel
from typing import List

class RequestParams(BaseModel):
	city: str
	lang: str
	key: str
class Weather(BaseModel):
	max_temp: float
	min_temp: float
	datetime: str
class Response(BaseModel):
	data: List[Weather]
	city_name: str
class TempData(BaseModel):
	city_name: str
	max_temp: float
	min_temp: float

def get():
	url: str = 'https://api.weatherbit.io/v2.0/forecast/daily'
	params: RequestParams = {		
		"city": 'Fukuoka,JP',
		"lang": "ja",
		"key": config.WEATHER_API_KEY
	}

	req = requests.get(url, params)
	res = Response.parse_raw(req.text)

	return TempData(**{
		"city_name": res.city_name,
		"max_temp": res.data[0].max_temp,
		"min_temp": res.data[0].min_temp,
	})


