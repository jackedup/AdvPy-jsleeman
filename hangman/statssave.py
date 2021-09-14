import json
import struct
from os import name, stat

##how to write json found from https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


data = {}

#if file not found{
#data['players'] = []
#}
#else{
statfile = open('playerstats.json', 'r')
jsondata = json.load(statfile)
statfile.close()

if "players" not in jsondata:
	print("players not in json")
	jsondata['players'] = []
def updatePlayer(name, winpercent, gamesplayed, wins):
	for playerobj in jsondata['players']:
		for player in playerobj:
			print (player)
			if player == name:
				jsondata['players'].remove(playerobj)
				jsondata['players'].append({
				name : ({
					'name' : name,
					'winpercent' : winpercent,
					'games played' : gamesplayed,
					'wins' : wins
					})
				})
				with open('playerstats.json', 'w') as outfile:
					json.dump(jsondata,outfile)
				return

	print("error, player not found")
def getPlayer(name):
	for playerobj in jsondata['players']:
		for player in playerobj[name]:
			
			
				
				
getPlayer("jack")
def addPlayerGame(name, win):
	getPlayer()
	return
def addPlayer(name):
	for playerobj in jsondata['players']:
		for player in playerobj:
			#print (player)
			if player == name:
				return 0
	jsondata['players'].append({
		name : {
			'name' : name,
			'winpercent' : '0',
			'games played' : '0',
			'wins' : '0',
			'ties' : '0'
			}
		})
	with open('playerstats.json', 'w') as outfile:
		json.dump(jsondata,outfile)
	return True
#getPlayer('name')

