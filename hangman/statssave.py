import json
import struct
from os import name, stat

##how to write json found from https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/


data = {}


statfile = open('playerstats.json', 'r')
jsondata = json.load(statfile)
statfile.close()

if "players" not in jsondata:
	print("players not in json")
	jsondata['players'] = []
def deletePlayer(name):
	for playerobj in jsondata['players']:
		for player in playerobj:
			if player == name:
				jsondata['players'].remove(playerobj)
				with open('playerstats.json', 'w') as outfile:
					json.dump(jsondata,outfile)
def updatePlayer(name, winpercent, gamesplayed, wins):
	for playerobj in jsondata['players']:
		for player in playerobj:
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
		for player in playerobj:
			if player == name :
				return playerobj[player]
	return -1
				
				
def addPlayerGame(name, win):
    
	if (win):
		 print("You Won!")
	else:
		print("You Failed!")

	player = getPlayer(name)
	gamesplayed = int(player['games played']) 
	gamesplayed += 1
	wins = player['wins'] 
	if win:
		wins +=1
	winratio = wins/gamesplayed
	updatePlayer(name, winratio, gamesplayed, wins)
	input("Enter to continue")
	return
if (not getPlayer("jack")):
	print("error")
def addPlayer(name):
	for playerobj in jsondata['players']:
		for player in playerobj:
			if player == name:
				print("error: player already exists")
				return 0
	jsondata['players'].append({
		name : {
			'name' : name,
			'winpercent' : 0,
			'games played' : 0,
			'wins' : 0,
			'ties' : 0
			}
		})
	with open('playerstats.json', 'w') as outfile:
		json.dump(jsondata,outfile)
	return True

