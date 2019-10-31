import pygame
import os
from Colors import *

class MySprite(pygame.sprite.Sprite):
	#This class represents a car. It derives from the "Sprite" class in Pygame.
	
	def __init__(self,filename,color = WHITE):
		# Call the parent class (Sprite) constructor
		super().__init__()
		self.pos = (0,0)
		if os.path.isfile(filename):
			self.image = pygame.image.load(filename).convert_alpha()
		else:
			print("{0} not found".format(filename))
		self.rect = self.image.get_rect()

	def setPosition(self,pos = (0,0)):
		self.rect.left = pos[0]
		self.rect.top = pos[1]



myfont = None
class MyText(pygame.sprite.Sprite):
	#This class represents a car. It derives from the "Sprite" class in Pygame.
	
	def __init__(self,name,bbox,color = WHITE):
		global myfont
		if myfont is None:
			myfont = pygame.font.SysFont(None, 21)
		# Call the parent class (Sprite) constructor
		super().__init__()
		self.pos = (0,0)
		self.image = myfont.render("",True,BLUE,WHITE)
		self.rect = self.image.get_rect()
		self.rect = bbox

	def setPosition(self,pos = (0,0)):
		self.rect.left = pos[0]
		self.rect.top = pos[1]
		
	def updateText(self,text):
		self.image = myfont.render(text,True,BLUE,WHITE)