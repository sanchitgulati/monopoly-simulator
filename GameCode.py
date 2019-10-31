import json
import random
from random import shuffle
import time
import threading
from Colors import *

debug = False
collated_result = []
BOARD_SIZE = 40
GOTO_JAIL_INDEX = 30
JAIL_INDEX = 10
COMMUNITY_CHEST_INDEXES = [2,17]
CHANCE_INDEXES = [7,22,33]
UTILITY_BOXES = [12,28]
RAILWAY_BOXES = [5,15,25,35]
#Roll values are values from a six by six grid for all dice rolls
ROLL_VALUES = [2,3,4,5,6,7,3,4,5,6,7,8,4,5,6,7,8,9,5,6,7,8,9,10,6,7,8,9,10,11,7,8,9,10,11,12]

#Simulation code
def simulateBoard(turn_per_round=100):
	local_squares = []
	while len(local_squares) < BOARD_SIZE:
		local_squares.append(0)
	#-1 is money related so ignored in logic
	master_chest = [0,-1,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
	chest = [i for i in master_chest]
	shuffle(chest)
	#-1 is money related so ignored in logic
	#B is go to 3 places
	#R is 'GOTO nearest railroad'
	#U is 'GOTO nearest utility'
	master_chance = [0,24,11,'U','R',-1,-1,'B',10,-1,-1,5,39,-1,-1,-1]
	chance = [i for i in master_chance]
	shuffle(chance)
	doubles = 0
	position = 0
	turn = 0
	while turn < turn_per_round:
		diceroll = int(36*random.random())
		#Dice index values for double rolls # REROLL
		if diceroll in [0,7,14,21,28,35]:
			doubles += 1
		else:
			doubles = 0
		if doubles >= 3:
			position = 10
		else:
			position = (position + ROLL_VALUES[diceroll])%BOARD_SIZE
			if position in CHANCE_INDEXES:
				chance_card = chance.pop(0)
				if len(chance) == 0:
					chance = [i for i in master_chance]
					shuffle(chance)
				if chance_card != -1:
					if isinstance(chance_card,int):
						position = chance_card
					elif chance_card == 'U':
						while position not in UTILITY_BOXES:
							position = (position + 1)%BOARD_SIZE 
					elif chance_card == 'R':
						while position not in RAILWAY_BOXES:
							position = (position + 1)%BOARD_SIZE
					elif chance_card == 'B':
						position = position - 3
			elif position in COMMUNITY_CHEST_INDEXES:
				chest_card = chest.pop(0)
				if len(chest) == 0:
					chest = [i for i in master_chest]
					shuffle(chest)
				if chest_card != -1:
					position = chest_card
			if position == GOTO_JAIL_INDEX:
				position = JAIL_INDEX
			local_squares.insert(position,(local_squares.pop(position)+1))
			turn += 1

	return local_squares

def resetBoard():
	global collated_result
	collated_result = []
	while len(collated_result) < BOARD_SIZE:
		collated_result.append(0)

def runSimulation(turn_per_round=100, games_order=3):
	games = 10**games_order
	games_finished = 0
	while games_finished < games:
		result = simulateBoard(turn_per_round)
		for index, e in enumerate(result):
			collated_result[index] += e
		if debug:
			printResult(collated_result)
		games_finished += 1

def printResult(result):
	total = sum(result)
	i = 0
	print("\nNew Run")
	for index, e in enumerate(result):
		print("{0} {1} {2:.2f} %".format(index,board[index]["name"],round((e/total)*100,2)))


	collated_total = sum(collated_result)
	print("\nCollated Results")
	for index, e in enumerate(collated_result):
		print("{0} {1} {2:.2f} %".format(index,board[index]["name"],round((e/collated_total)*100,2)))
		i+= 1

if __name__ == "__main__":
	debug = True
	start_time = time.time()
	resetBoard()
	board = json.loads(open('board.json').read())
	turn_per_round = 100
	games_order = 5
	print("Rolls per game {0}".format(turn_per_round))
	print("Total Games {0}".format(10**games_order))
	runSimulation(turn_per_round,games_order)
	print("--- %s seconds ---" % (time.time() - start_time))



