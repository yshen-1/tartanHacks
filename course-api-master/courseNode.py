class courseNode(object):
    def __init__(self,courseName):
        self.courseName=courseName
        self.x = 0
        self.y = 0
        self.r = 30
        self.prereqsFor = set()
        self.prereqsNeeded = set()

    def setPosition(self,x,y):
        self.x = x
        self.y = y 

    def addPrereqsFor(self,L):
        self.prereqsFor=self.prereqsFor.union(set(L))
                
    def addPrereqsNeeded(self,L):
        self.prereqsNeeded=self.prereqsNeeded.union(set(L))

