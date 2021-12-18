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
	link: str
class Response(BaseModel):
	items: List[Image]

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

	return res.items[0].link


