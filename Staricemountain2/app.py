import json
from django.http.response import JsonResponse
from Staricemountain2.models import Temperatures
from Staricemountain2 import azure_blob, data
from Staricemountain2 import weather
from Staricemountain2 import picture

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

	# 画像のURLをアップロードする
	picture_keyword = hotdata.word
	azure_blob.upload_from_url(picture.get_from_pixabay(picture_keyword))

	# レスポンス
	response = JsonResponse({})
	response.headers = {"Content-Type": "application/json; charset=utf-8"}
	response.content = json.dumps({
		"city": temp_data.city_name,
		"max_temp": temp_data.max_temp,
		"min_temp": temp_data.min_temp,
		"total": round(total, 2),
		"message": hotdata.message,
		"thumnail_url": picture.get(picture_keyword),
	}, ensure_ascii=False)

	return response

def calculate_total(add_temp):
	if (Temperatures.objects.exists == False):
		return add_temp

	current_total = Temperatures.objects.latest('created_at').total
	return current_total + add_temp