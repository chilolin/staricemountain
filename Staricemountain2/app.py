import json
from django.http.response import JsonResponse
from Staricemountain2.models import Temperatures
from Staricemountain2 import data
from Staricemountain2 import weather

def tweet(request):
	temp_data = weather.get()
	total = calculate_total(temp_data.max_temp)

	# DBに登録する。
	Temperatures.objects.create(
		city=temp_data.city_name,
		max_temp = temp_data.max_temp,
		min_temp = temp_data.min_temp,
		total=total
	)

	# 温度のデータをとってくる
	hotdata = data.hot(total)

	# 画像のURLを取ってくる
	picture_keyword = hotdata.word

	# レスポンス
	response = JsonResponse({})
	response.headers = {"Content-Type": "application/json; charset=utf-8"}
	response.content = json.dumps({
		"city": temp_data.city_name,
		"max_temp": temp_data.max_temp,
		"min_temp": temp_data.min_temp,
		"total": total,
		"message": hotdata.message,
		# "picture": ,
	}, ensure_ascii=False)

	return response

def calculate_total(add_temp):
	if (Temperatures.objects.exists == False):
		return add_temp

	current_total = Temperatures.objects.latest('created_at').total
	return current_total + add_temp