import json
target = open('fundamentals_quote_data.json', 'w')

patterns = ['Give me the INTENT of the stock whose PROPERTY is VALUE.',"Give me it's INTENT.",
'Could you please tell me about the INTENT of the stock whose PROPERTY is VALUE?',"Could you please tell me about it's INTENT?",
'I wanna know the INTENT of the stock whose PROPERTY is VALUE.',"I wanna know it's INTENT.",
'Do you know the INTENT of the stock whose PROPERTY is VALUE?',"Do you know it's INTENT?'",
'How about the INTENT of the stock whose PROPERTY is VALUE?',"How about the INTENT?"]

intents_dict = {
	"open price":"open",
	"intraday high":"high",
	"intraday low":"low",
	"volume":"volume",
	"average volume in last 2 weeks":"average_volume_2_weeks",
	"average volume":"average_volume",
	"highest price in last 52 weeks":"high_52_weeks",
	"dividend yield":"dividend_yield",
	"lowest price in last 52 weeks":"low_52_weeks",
	"P/E ratio":"pe_rario",		
	"shares outstanding":"shares_outstanding",
	"description":"description",
	"instrument url":"instrument",
	"CEO":"ceo",
	"headquarter's city":"headquarters_city",
	"headquarter's state":"headquarters_state",
	"sector":"sector",
	"number of employees":"num_employees",
	"year of founding":"year_founded",
	"ask price":"ask_price",
	"ask size":"ask_size",
	"bid price":"bid_price",
	"bid size":"bid_size",
	"last trade price":"last_trade_price",
	"last extended hour's trade price":"last_extended_hours_trade_price",
	"previous close":"previous_close",
	"adjusted previous close":"adjusted_previous_close",
	"symbol":"symbol",
	"last trade price's source":"last_trade_price_source",
	"instrument":'instrument',
	"all informations":"all",
	'margin initial ratio':'margin_initial_ratio',
	'rhs tradability':'rhs_tradability',
	'id':'id',
	'market':'market',
	'simple name':'simple_name',
	'min tick size':'min_tick_size',
	'maintenance ratio':'maintenance_ratio',
	'tradability':'tradability',
	'state':'state',
	'type':'type',
	'tradeable':'tradeable',
	'fundamentals':'fundamentals',
	'quote':'quote',
	'day trade ratio':'day_trade_ratio',
	'name':'name',
	'tradable chain id':'tradable_chain_id',
	'splits':'splits',
	'url':'url',
	'country':'country',
	'bloomberg unique':'bloomberg_unique',
	'list date':'list_date'}

append_func = [('symbol', 'FB'),('symbol','MSFT'),
               ('url','https://api.robinhood.com/instruments/?symbol=MSFT'),
               ('url','https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/')]

json_data = {"rasa_nlu_data":{"common_examples":[]}}
for s in patterns:
	for (key, value) in intents_dict.items():
		text = s.replace("INTENT", key)
		if(text.find('PROPERTY')==-1):
			to_append = {"text": text, "intent": "stock.%s"%(value), "entities":[]}
			json_data['rasa_nlu_data']['common_examples'].append(to_append)
			continue	
		for (entity, en_value) in append_func:
			text_tmp = text.replace('PROPERTY',entity)
			start = text_tmp.find("VALUE")
			end = start + len(en_value)
			text_tmp = text_tmp.replace('VALUE',en_value)
			to_append = {
				"text":text_tmp,
				"intent":"stock.%s"%(value),
				"entities":[
					{
						"start":start,
						"end":end,
						"value":en_value,
						"entity": entity
					}
				]
			}
			json_data['rasa_nlu_data']['common_examples'].append(to_append)
json.dump(json_data, target, indent=2)
