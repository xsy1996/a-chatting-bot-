import requests
import json
import get_api

last_entity = None

def get_input():
	return str(input("HI~: "))

def curl_input_text(text):
	headers = {'Accept': 'application/json'}
	url = "http://localhost:5000/parse?q=%s"%(text)
	r = requests.get(url=url, timeout=3, headers=headers).json()
	return r

def get_data_from_api(cut_json):
	global last_entity
	entity = cut_json['entities']
	# print (last_entity)
	if len(entity) == 0:
		entity = last_entity
	if entity is None:
		return "Sorry I don't know"
	if(entity[0]['entity'] == 'date'):
		if(last_entity[0]['entity'] == 'mic'):
			last_entity.append(entity[0])
			last_entity[1]=entity[0]
			entity = last_entity
		else:
			return "Sorry I don't know"
	last_entity = entity
	# print(entity)
	if(entity[0]['entity'] == 'symbol' or entity[0]['entity'] == 'url'):
		if(cut_json['intent']['name'].split('.')[0]=='market'):
			return "Sorry I don't know"

		if entity[0]['entity'] == 'symbol':
			stock_instrument = get_api.get_instrument_info(typ='symbol',symbol=entity[0]['value'],url='')
		else:
			stock_instrument = get_api.get_instrument_info(typ='url',symbol='',url=entity[0]['value'])

		try:
			stock = stock_instrument
			result = [eval(cut_json['intent']['name'])]
			return result
		except:
			pass

		try:
			stocks = get_api.get_fundamentals_info([stock_instrument.symbol])
			result = [eval(cut_json['intent']['name']) for stock in stocks]
			return result
		except:
			pass

		try:
			stocks = get_api.get_quote_info([stock_instrument.symbol])
			result = [eval(cut_json['intent']['name']) for stock in stocks]
			return result
		except:
			pass

		return "Sorry I don't know"

	elif(len(entity) == 1 and entity[0]['entity'] == 'mic'):
		if(cut_json['intent']['name'].split('.')[0] == 'stock'):
			return "Sorry I don't know"

		market = get_api.get_market_info(typ='mic',mic=entity[0]['value'])
		try:
			result = [eval(cut_json['intent']['name'])]
			return result
		except:
			pass
		return "Sorry I don't know"
	elif(len(entity) >= 2):
		if(cut_json['intent']['name'].split('.')[0]=='stock'):
			return "Sorry I don't know"

		market = get_api.get_market_info(typ='hours',mic=entity[0]['value'],date=entity[1]['value'])
		try:
			result = [eval(cut_json['intent']['name'])]
			return result
		except:
			pass
		return "Sorry I don't know"


if __name__ == "__main__":
	
	while True:
		nlu_json = curl_input_text(get_input())
		resopnse = get_data_from_api(nlu_json)[0]
		print(resopnse)
