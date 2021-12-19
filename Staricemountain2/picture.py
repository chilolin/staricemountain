import requests
import config
# types
from pydantic import BaseModel
from typing import List

class RequestParams(BaseModel):
	key: str
	cx: str
	q: str
	num: int
	start: int
	searchType: str
class Image(BaseModel):
	contextLink: str
class Info(BaseModel):
	image: Image
class Response(BaseModel):
	items: List[Info]

def get(query: str):
	url: str = 'https://www.googleapis.com/customsearch/v1'
	params: RequestParams = {
		"key": config.GOOGLE_SEARCH_API_KEY,
		"cx": config.GOOGLE_SEARCH_CSE_KEY,
		"q": query,
		"num": 1,
		"start": 1,
		"searchType": "image"
,	}

	req = requests.get(url, params)
	res = Response.parse_raw(req.text)

	return res.items[0].image.contextLink

class RequestPixabayParams(BaseModel):
	key: str
	q: str
	image_type: str
	lang: str
class Hit(BaseModel):
	webformatURL: str
class PixabayResponse(BaseModel):
	hits: List[Hit]
def get_from_pixabay(query):
	url: str = 'https://pixabay.com/api/'
	params: RequestPixabayParams = {
		"key": config.GOOGLE_SEARCH_API_KEY,
		"q": query,
		"image_type": "photo",
		"lang": "ja",
	}

	req = requests.get(url, params)
	res = PixabayResponse.parse_raw(req.text)

	return res.hits[0].webformatURL


