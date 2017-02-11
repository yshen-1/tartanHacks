class courseNode(object):
    def __init__(self,courseName):
        self.courseName=courseName
        self.x = 0
        self.y = 0
        self.r = 30
        self.prereqsFor = list()
        self.prereqsNeeded = list()
        self.superScore=0
        self.angle=0
        self.master_descrip = dict()

    def setSuperScore(self,superScore):
        self.superScore=superScore

    def setAngle(self,angle):
        self.angle=angle

    def setPosition(self,x,y):
        self.x = x
        self.y = y 

    def setMasterDescrip(self,descrip):
        self.master_descrip = descrip

    def getMasterDescrip(self):
        return self.master_descrip

    def addPrereqsFor(self,L):
        self.prereqsFor.extend(L)

    def addPrereqsNeeded(self,L):
        self.prereqsNeeded.extend(L)

    def getPrereqsFor(self):
        return self.prereqsFor

    def getPrereqsNeeded(self):
        return self.prereqsNeeded

    def getSuperScore(self):
        return self.superScore

    def getCourseName(self):
        return self.courseName

    def getPosition(self):
        return (self.x,self.y)