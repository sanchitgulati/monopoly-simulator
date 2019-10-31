#Seprate Classes for PSD Reader
#No dependancy on PyGame

class Sprite:
	def __init__(self, name = "Unnamed"):
		self.name = name
	def Set(self,path,size = (0,0),bbox = (0,0,0,0)):
		self.path = path
		self.size = size
		self.bbox = bbox
	def __str__(self):
		return "\nName: {0}\tPath: {1} Size: {2} Bbox: {3} \n".format(self.name,self.path,self.size,self.bbox)
	def __repr__(self):
		return "\nName: {0}\tPath: {1} Size: {2} Bbox: {3} \n".format(self.name,self.path,self.size,self.bbox)

class Text:
	def __init__(self, name = "Unnamed"):
		self.name = name
	def Set(self,bbox = (0,0,0,0)):
		self.bbox = bbox
	def __str__(self):
		return "\nName: {0}\t Bbox: {3} \n".format(self.name,self.bbox)
	def __repr__(self):
		return "\nName: {0}\t Bbox: {3} \n".format(self.name,self.bbox)