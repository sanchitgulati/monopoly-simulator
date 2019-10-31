from psd_tools import PSDImage
import os
from PSDTypes import *

psd = None
sprites = []
texts = []


def Initialize_UI_From_PSD(fileName):
	global psd
	psd = PSDImage.open(fileName)
	screenSize = (0,0)
	for layer in psd:
		if layer.name.lower() == 'ScreenSize'.lower():
			screenSize = layer.size
	return screenSize


def ExtractTextPosition(dirName = "UI"):
	global texts
	if psd is None:
		texts
	for layer in psd:
		if layer.kind == 'type':
			bbox = layer.bbox
			text = Text(layer.name)
			text.Set(bbox)
			texts.append(text)
	return texts


def ExtractUI(dirName = "UI"):
	global sprites
	if psd is None:
		return sprites
	if not os.path.exists(dirName):
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ")
	else:
		print("Directory " , dirName ,  " already exists")

	for layer in psd:
		if not layer.kind == 'type':
			filePath =  os.path.join(dirName,layer.name+'.png')
			try:
				layer.compose().save(filePath)
			except:
				print("Error exporting "+layer.name)
			else:
				size = layer.size
				bbox = layer.bbox
				sprite = Sprite(layer.name)
				sprite.Set(filePath,size,bbox)
				sprites.append(sprite)
	return sprites


