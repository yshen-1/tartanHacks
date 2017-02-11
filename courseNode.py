

class courseNode(object):
	def __init__(courseID, courseName):
		self.courseID = courseID
		self.courseName = courseName
		self.x = 0
		self.y = 0
		self.prereqsFor = []
		self.prereqsNeeded = []

	def setPosition(x,y):
		self.x = x
		self.y = y 

	def addPrereqsFor(L):
		self.prereqsFor.append(L)

	def addPrereqsNeeded(L):
		self.prereqsNeed.append(L)

	#Parses course id to get the department
	def getDepartmentColor():
		idPrefix = courseID[0:2]
		idCourseLevel = int(course[3]); #The course level ie 100-level, 200-level etc.

		csBaseColor = (204, 0, 0)
		eceBaseColor = (51, 204, 51)

		if(idPrefix == "15"):
			for i in csBaseColor:
				cs
			 
			return ()
		elif(idPrefix == "18")
			return ()
	