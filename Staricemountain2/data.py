from enum import Enum
class Hot(Enum):
    kaitei = 3.0
	
    buthu = 21.0
    kaimin = 20.0
    taion = 36.0
    kion = 40.0
    zentya = 70.0

def hot(color):
	word = ''
	message = ''
	if color >= Hot.kaitei.value and color <= Hot.buthu.value:
		print('海底の温度')
		data = {
			"word" : '海底',
			"message" : '海底の温度です',
		}
		return data
	elif color <= Hot.buthu.value:
		print('ブーツ')
		data = {
			"word" : '海底',
			"message" : '海底の温度です',
		}
		return data
	elif color <= Hot.buthu.value:
		print('快眠')
		data = {
			"word" : '海底',
			"message" : '海底の温度です',
		}
		return data
	else:
		print('エルス')
		data = {
			"word" : '海底',
			"message" : '海底の温度です',
		}
		return data