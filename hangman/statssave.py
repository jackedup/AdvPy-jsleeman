import json

##how to write json found from https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


data = {}

data['players'] = []
data['players'].append({
	'name' : 'Jack',
	'winpercent' : 0.5,
	'wins' : 10,
	'ties' : 0
	})
with open('playerstats.json', 'w') as outfile:
	json.dump(data,outfile)
