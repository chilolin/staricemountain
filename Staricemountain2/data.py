from enum import Enum
from pydantic.main import BaseModel

class Hot(Enum):
	kaitei = 3.0 
	boots = 10.0
	kaimin = 20.0
	taion = 36.0 
	kion = 40.6
	keiyu = 50.0
	kansokusaikou = 58.8
	sentya = 70.0
	etanoru = 78.0 #エタノール
	sauna = 90.0
	mizu = 100.0
	tyuuka = 140.0
	yasai = 160.0
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

class HotData(BaseModel):
	word: str
	message: str

def hot(total):
	hot_data = HotData(**{
		"word": "",
		"message": "",
	})
	if total <= Hot.kaitei.value:
		hot_data = create_hot_data("海底", "海底の温度", total, Hot.kaitei.value)
	elif total <= Hot.boots.value:
		hot_data = create_hot_data("ブーツ", "ブーツが活躍する温度", total, Hot.boots.value)
	elif total <= Hot.kaimin.value:
		hot_data = create_hot_data("快眠", "快眠に最適な温度", total, Hot.kaimin.value)
	elif total <= Hot.taion.value:
		hot_data = create_hot_data("体温", "人間の体温", total, Hot.taion.value)
	elif total <= Hot.kion.value:
		hot_data = create_hot_data("2021年の日本の最高気温", "2021年の日本の最高気温", total, Hot.kion.value)
	elif total <= Hot.keiyu.value:
		hot_data = create_hot_data("軽油", "軽油が引火する温度", total, Hot.keiyu.value)
	elif total <= Hot.kansokusaikou.value:
		hot_data = create_hot_data("地球で観測された最高気温", "地球で観測された最高気温", total, Hot.kansokusaikou.value)
	elif total <= Hot.sentya.value:
		hot_data = create_hot_data("煎茶", "煎茶がおいしい温度", total, Hot.sentya.value)
	elif total <= Hot.etanoru.value:
		hot_data = create_hot_data("エタノール", "エタノールが沸騰する温度", total, Hot.etanoru.value)
	elif total <= Hot.sauna.value:
		hot_data = create_hot_data("サウナ", "レベルの高いサウナの温度", total, Hot.sauna.value)
	elif total <= Hot.mizu.value:
		hot_data = create_hot_data("沸騰", "水が沸騰する温度", total, Hot.mizu.value)
	elif total <= Hot.tyuuka.value:
		hot_data = create_hot_data("中華料理", "中華料理の油通しに最適な温度", total, Hot.tyuuka.value)
	elif total <= Hot.yasai.value:
		hot_data = create_hot_data("香味野菜", "香味野菜を揚げるのに最適な温度", total, Hot.yasai.value)
	elif total <= Hot.agemono.value:
		hot_data = create_hot_data("揚げ物", "揚げ物全般を揚げるときに最適な温度", total, Hot.agemono.value)
	elif total <= Hot.ageru.value:
		hot_data = create_hot_data("ブロッコリー", "水気を多く含むものを上げるときに最適な温度", total, Hot.ageru.value)
	elif total <= Hot.suihanki.value:
		hot_data = create_hot_data("炊飯器", "いい炊飯器の高温スチーマーの温度", total, Hot.suihanki.value)
	elif total <= Hot.mokuzai.value:
		hot_data = create_hot_data("木材", "木材が燃える温度", total, Hot.mokuzai.value)
	elif total <= Hot.suigin.value:
		hot_data = create_hot_data("水銀", "水銀が沸騰する温度", total, Hot.suigin.value)
	elif total <= Hot.tabako.value:
		hot_data = create_hot_data("タバコ", "タバコの温度", total, Hot.tabako.value)
	elif total <= Hot.doutoke.value:
		hot_data = create_hot_data("銅", "銅が溶ける温度", total, Hot.doutoke.value)
	elif total <= Hot.tetutoke.value:
		hot_data = create_hot_data("鉄", "鉄が溶ける温度", total, Hot.tetutoke.value)
	elif total <= Hot.dou.value:
		hot_data = create_hot_data("銅", "銅が沸騰する温度", total, Hot.dou.value)
	elif total <= Hot.tetu.value:
		hot_data = create_hot_data("鉄", "鉄が沸騰する温度", total, Hot.tetu.value)
	elif total <= Hot.baanaa.value:
		hot_data = create_hot_data("酸素バーナー", "酸素バーナーの温度", total, Hot.baanaa.value)
	elif total <= Hot.arumi.value:
		hot_data = create_hot_data("アルミニウム", "アルミニウム粉末燃焼温度", total, Hot.arumi.value)
	elif total <= Hot.nitoro.value:
		hot_data = create_hot_data("ニトログリセリン爆発", "ニトログリセリン爆発する温度", total, Hot.nitoro.value)
	elif total <= Hot.sun.value:
		hot_data = create_hot_data("太陽", "太陽表面温度", total, Hot.sun.value)
	else:
		hot_data = HotData(**{
			"word": "高すぎ",
			"message": "高すぎる温度です!"
		})
	return hot_data

def create_hot_data(word: str, desc: str, total: float, hot_temp: float):
	if (total == hot_temp):
		return HotData(**{
			"word": word,
			"message": equal_message(desc)
		})
	else:
		return HotData(**{
			"word": word,
			"message": diff_message(desc, hot_temp-total)
		})

def equal_message(desc: str):
	return desc + 'です!'

def diff_message(desc: str, diff: float):
	return desc + 'まであと' + str(diff) + '℃です!'