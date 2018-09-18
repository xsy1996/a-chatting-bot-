import json
target = open('market_date_data.json', 'w')

# patterns = ['Give me the INTENT of the market whose PROPERTY is VALUE.',"Give me it's INTENT.",
# 'Could you please tell me about the INTENT of the market whose PROPERTY is VALUE?',"Could you please tell me about it's INTENT?",
# 'I wanna know the INTENT of the market whose PROPERTY is VALUE.',"I wanna know it's INTENT.",
# 'Do you know the INTENT of the market whose PROPERTY is VALUE?',"Do you know it's INTENT?'",
# 'How about the INTENT of the market whose PROPERTY is VALUE?',"How about the INTENT?"]

patterns = ['Give me the INTENT of the market whose PROPERTY is VALUE on DATE.',"Give me it's INTENT on DATE.",
'Could you please tell me about the INTENT of the market whose PROPERTY is VALUE on DATE?',"Could you please tell me about it's INTENT on DATE?",
'I wanna know the INTENT of the market whose PROPERTY is VALUE on DATE.',"I wanna know it's INTENT on DATE.",
'Do you know the INTENT of the market whose PROPERTY is VALUE on DATE?',"Do you know it's INTENT on DATE?'",
'How about the INTENT of the market whose PROPERTY is VALUE on DATE?',"How about the INTENT on DATE?"]

intents_dict = {
	# 'website':'website',
	# 'city':'city',
	# 'name':'name',
	# 'url':'url',
	# 'country':'country',
	# "today's hours":'todays_hours',
	# 'operating mic':'operating_mic',
	# 'acronym':'acronym',
	# 'timezone':'timezone',
	# 'mic':'mic'

	'closes at':'closes_at',
	'extended opens at':'extended_opens_at',
	'next open hours':'next_open_hours',
	'previous open hours':'previous_open_hours',
	'is open':'is_open',
	'extended closes at':'extended_closes_at',
	'date':'date',
	'opens at':'opens_at'
	}

append_func = [('mic', 'XNYS')]

json_data = {"rasa_nlu_data":{"common_examples":[]}}
for s in patterns:
	for (key, value) in intents_dict.items():
		text = s.replace("INTENT", key)
		if(text.find('PROPERTY')==-1):
			# to_append = {"text": text, "intent": "market.%s"%(value), "entities":[]}
			
			start = text.find('DATE')
			end = start + len(en_value)
			text_tmp = text.replace('DATE','2018-09-19')
			to_append = {
				"text":text_tmp,
				"intent":"market.%s"%(value),
				"entities":[
					{
						"start":start,
						"end":end,
						"value":'2018-09-19',
						"entity": 'date'
					}
				]
			}
			json_data['rasa_nlu_data']['common_examples'].append(to_append)
			continue	
		for (entity, en_value) in append_func:
			# text_tmp = text.replace('PROPERTY',entity)
			# start = text_tmp.find("VALUE")
			# end = start + len(en_value)
			# text_tmp = text_tmp.replace('VALUE',en_value)
			# to_append = {
			# 	"text":text_tmp,
			# 	"intent":"market.%s"%(value),
			# 	"entities":[
			# 		{
			# 			"start":start,
			# 			"end":end,
			# 			"value":en_value,
			# 			"entity": entity
			# 		}
			# 	]
			# }

			text_tmp = text.replace('PROPERTY',entity)
			start1 = text_tmp.find("VALUE")
			end1 = start1 + len(en_value)
			text_tmp = text_tmp.replace('VALUE',en_value)
			start2 = text_tmp.find("DATE")
			end2 = start2 + len('2018-09-09')
			text_tmp = text_tmp.replace('DATE','2018-09-19')
			to_append = {
				"text":text_tmp,
				"intent":"market.%s"%(value),
				"entities":[
					{
						"start":start1,
						"end":end1,
						"value":en_value,
						"entity": entity
					},
					{
						"start":start2,
						"end":end2,
						"value":'2018-09-19',
						"entity": 'date'
					}
				]
			}

			json_data['rasa_nlu_data']['common_examples'].append(to_append)
json.dump(json_data, target, indent=2)
