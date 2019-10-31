import pygame, sys
import argparse
from pygame.locals import *
from PSDReader import *
from MySprite import *
from GameCode import *

#Turns per game
#Try reading value from cmd
turn_per_round = 100
try:
	parser = argparse.ArgumentParser()
	parser.add_argument("turn_per_round", help="How many dice roll per 1 Game",type=int)
	args = parser.parse_args()
	turn_per_round = args.turn_per_round
	print("Using user-defined turn_per_round value {0}".format(turn_per_round))
except:
	print("Using default turn_per_round value {0}".format(turn_per_round))


# set up pygame
pygame.init()

# set up the window
screenSize = Initialize_UI_From_PSD("UI.psd")
UIelements = ExtractUI()
TextElements = ExtractTextPosition()
windowSurface = pygame.display.set_mode(screenSize, 0, 32)
pygame.display.set_caption('Mono Simulator!')


#PyGame groups to bulk draw and update
all_sprites_list = pygame.sprite.Group()
all_text_list = pygame.sprite.Group()

for x in UIelements:
	t = MySprite(x.path)
	t.setPosition((x.bbox[0],x.bbox[1]))
	all_sprites_list.add(t)

textHash = {}
for x in TextElements:
	t = MyText(x.name,x.bbox)
	textHash[x.name.lower()] = t
	all_text_list.add(t)

clock=pygame.time.Clock()
resetBoard()


#Counter to track games finished
games_finished = 0


#Initilizing the empty array
collated_result = []
while len(collated_result) < 40:
	collated_result.append(0)


GameNumberCounter = MyText(x.name,(5,5,0,0))
all_text_list.add(GameNumberCounter)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	#Simulate 1 game
	result = simulateBoard(turn_per_round)
	games_finished+=1
	GameNumberCounter.updateText("Game No {0}".format(games_finished))

	#Draw the white background onto the surface
	windowSurface.fill(WHITE)
	
	#Now let's draw all the sprites in one go.
	all_sprites_list.draw(windowSurface)

	#Updating collated results
	for index, e in enumerate(result):
		collated_result[index] += e

	#Updating text elements from collated results
	sums = sum(collated_result)
	for index, e in enumerate(collated_result):
		try:
			textHash["{0}".format(index)].updateText("{0}%".format(round((e/sums)*100,2)))
		except:
			print("{0} hash key not found".format(i))
	#Now let's draw all the text in one go.
	all_text_list.draw(windowSurface)
	#Refresh Screen
	pygame.display.flip()
	#Number of frames per second e.g. 60
	clock.tick(60)