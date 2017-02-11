class courseNode(object):
    def __init__(self,courseName):
        self.courseName=courseName
        self.x = 0
        self.y = 0
        self.r = 30
        self.prereqsFor = list()
        self.prereqsNeeded = list()

    def setPosition(self,x,y):
        self.x = x
        self.y = y 

    def addPrereqsFor(self,L):
        self.prereqsFor=self.prereqsFor.extend(L)

    def addPrereqsNeeded(self,L):
        self.prereqsNeeded=self.prereqsNeeded.extend(L)


