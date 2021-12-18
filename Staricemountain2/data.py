from enum import Enum
class Hot(Enum):
    kaitei = 3.0 
    buthu = 21.0 #ブーツ
    kaimin = 20.0
    taion = 36.0 
    kion = 40.6
    keiyu = 50.0
    kansokusaikou = 58.8
    zentya = 70.0
    etanoru = 78.0 #エタノール
    sauna = 90.0
    mizu = 100.0
    tyuuka = 140.0
    agemono = 180.0
    ageru = 200.0
    suihanki = 220.0
    mokuzai = 250.0
    suigin = 357.0
    tabako = 700.0
    doutoke = 1075.0 #銅溶ける
    tetutoke = 1538.0 #鉄溶ける
    dou = 2571.0
    tetu = 2863.0
    bana = 3000.0
    arumi = 3700.0
    nitoro = 4000.0
    sun = 6000.0

def hot(total):
	word = ''
	message = ''
	if total >= Hot.kaitei.value and total <= Hot.buthu.value:
		print('海底の温度')
		data = {
			"word" : '海底',
			"message" : '海底の温度です',
		}
		return data
	elif total >= Hot.buthu.value and total <= Hot.kaimin.value:
		print('ブーツ')
		data = {
			"word" : 'ブーツ',
			"message" : 'ブーツが活躍する温度です',
		}
		return data
	elif total >= Hot.kaimin.value and total <= Hot.taion.value:
		print('快眠')
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.kaimin.value and total <= Hot.taion.value:
		data = {
            "word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.taion.value and total <= Hot.kion.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.kion.value and total <= Hot.keiyu.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.keiyu.value and total <= Hot.kansokusaikou.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.kansokusaikou.value and total <= Hot.zentya.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.zentya.value and total <= Hot.etanoru.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.etanoru.value and total <= Hot.sauna.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.sauna.value and total <= Hot.mizu.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.mizu.value and total <= Hot.tyuuka.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.tyuuka.value and total <= Hot.agemono.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.agemono.value and total <= Hot.ageru.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.ageru.value and total <= Hot.suihanki.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.suihanki.value and total <= Hot.mokuzai.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.mokuzai.value and total <= Hot.suigin.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.suigin.value and total <= Hot.tabako.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.tabako.value and total <= Hot.doutoke.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.doutoke.value and total <= Hot.tetutoke.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.tetutoke.value and total <= Hot.dou.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.dou.value and total <= Hot.tetu.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.tetu.value and total <= Hot.bana.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.bana.value and total <= Hot.arumi.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.arumi.value and total <= Hot.nitoro.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	elif total >= Hot.nitoro.value and total <= Hot.sun.value:
		data = {
			"word" : '快眠',
			"message" : '快眠に最適な温度です',
		}
		return data
	else:
		print('太陽')
		data = {
			"word" : '太陽',
			"message" : '太陽の表面温度です',
		}
		return data