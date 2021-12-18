from pydantic.types import Json
import config
import requests
from django.http.response import JsonResponse

from Staricemountain2.models import Temperatures

# types
from pydantic import BaseModel
from typing import List

def tweet(request):
	# DBに登録する。
	temp_data = get_weather()
	total = calculate_total(temp_data["max_temp"])
	Temperatures.objects.create(
		city=temp_data["city_name"],
		max_temp = temp_data["max_temp"],
		min_temp = temp_data["min_temp"],
		total=total
	)

	# 温度のデータをとってくる

	return JsonResponse({
		"city": temp_data["city_name"],
		"max_temp": temp_data["max_temp"],
		"min_temp": temp_data["min_temp"],
		"total": total
	})

class Weather(BaseModel):
	max_temp: float
	min_temp: float
	datetime: str
class Response(BaseModel):
	data: List[Weather]
	city_name: str


def get_weather():
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
		"min_temp": res.data[0].min_temp,
	}

def calculate_total(add_temp):
	current_total = Temperatures.objects.latest('created_at').total

	return current_total + add_temp
