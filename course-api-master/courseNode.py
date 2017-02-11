

class courseNode(object):
	def __init__(self):
		self.x = 0
		self.y = 0
                self.r=30
		self.prereqsFor = set()
		self.prereqsNeeded = set()

	def setPosition(self,x,y):
		self.x = x
		self.y = y 

	def addPrereqsFor(self,L):
		self.prereqsFor.extend(L)

	def addPrereqsNeeded(self,L):
		self.prereqsNeed.extend(L)
