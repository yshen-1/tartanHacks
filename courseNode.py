

class courseNode(object):
	#Constructor functions:
	def __init__(self,courseID, courseName):
		self.courseID = courseID
		self.courseName = courseName
		self.x = 0
		self.y = 0
		self.prereqsFor = []
		self.prereqsNeeded = []
	def setPosition(self,x,y):
		self.x = x
		self.y = y 

	def addPrereqsFor(self,L):
		self.prereqsFor.append(L)

	def addPrereqsNeeded(self,L):
		self.prereqsNeed.append(L)


	#Functions called by pygame (Alan)
	#Parses course id to get the department
	def getDepartmentColor(self):
		idPrefix = self.courseID[0:2]
		idCourseLevel = int(self.courseID[3]); #The course level ie 100-level, 200-level etc.

		csBaseColor = (204, 0, 0)
		eceBaseColor = (51, 204, 51)
		divisor = max((5-idCourseLevel),1)

		if(idPrefix == "15"):
			for i in csBaseColor:
				i = i // divisor
			return csBaseColor
		elif(idPrefix == "18"):
			for i in eceBaseColor:
				i = i // divisor
			return eceBaseColor



