import config
import requests
from django.http.response import JsonResponse

from Staricemountain2.models import Temperatures

# types
from pydantic import BaseModel
from typing import List

class Weather(BaseModel):
	max_temp: float
	datetime: str

class Response(BaseModel):
	data: List[Weather]
	city_name: str

def get(request):
	url = 'https://api.weatherbit.io/v2.0/forecast/daily'
	params = {		
		"city": 'Fukuoka,JP',
		"lang": "ja",
		"key": config.WEATHER_API_KEY
	}

	req = requests.get(url, params)
	res = Response.parse_raw(req.text)

	return {
		"city_name": res.city_name,
		"max_temp": res.data[0].max_temp,
		"datetime": res.data[0].datetime,
	}

