#!/usr/bin/env/python3
import pygame
from helpers import ScottyLabsHandler, lessCourses, zoom
from courseNode import courseNode
import math
import random

def getDepartmentColor(courseID):
    #courseID is string containing course number
    idPrefix=courseID.split('-')[0]
    idCourseLevel=int(courseID.split('-')[1][0])

    csBaseColor=[255,65,54]
    eceBaseColor=[1,244,112]
    mlBaseColor=[0,116,217]
    otherBaseColor=[176,196,222]
    
    mult = 20
    
    if idPrefix=="15":
        for i in range(len(csBaseColor)):
            csBaseColor[i]=max(0,csBaseColor[i]-min(100,idCourseLevel*mult))
        return csBaseColor
    elif idPrefix=="18":
        for i in range(len(eceBaseColor)):
            eceBaseColor[i]=max(0,eceBaseColor[i]-min(100,idCourseLevel*mult))
        return eceBaseColor
    elif idPrefix=="10":
        for i in range(len(mlBaseColor)):
            mlBaseColor[i]==max(0,mlBaseColor[i]-min(100,idCourseLevel*mult))
        return mlBaseColor
    else:
        for i in range(len(mlBaseColor)):
            otherBaseColor[i]==max(0,otherBaseColor[i])
        return otherBaseColor





#gets score of one course
#input : masterdictionary, one course
#output: score
def getScore(master_dict,courseName):
    currentNode = master_dict[courseName]
    prereqsFor = currentNode.getPrereqsFor()
    answer = len(prereqsFor)
    for prereq in prereqsFor:
        answer += getScore(master_dict,prereq)
    return answer



class mainApp(object):
    def __init__(self):
        pygame.init()
        self.resolution=2
        self.height=(1080)*3//4
        self.width=(1920)*3//4
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.background=pygame.Surface((self.width,self.height))
        self.backgroundImage=pygame.image.load("blurdark.png")
        self.backgroundColor=(150,50,140)
        self.backgroundImage=self.backgroundImage.convert()
        self.backgroundX,self.backgroundY=-self.backgroundImage.get_width()//4,-self.backgroundImage.get_height()//4
        self.background.fill(self.backgroundColor)
        self.background.blit(self.backgroundImage,(self.backgroundX,self.backgroundY))
        self.isRunning=True
        self.masterDict=dict()
        self.updateMasterDictionary()
        self.addSuperScores()
        self.mousePress=False
        self.cx,self.cy=self.width//2,self.height//2
        setNodePositions(self.masterDict,self.cx,self.cy) 
        self.font_list = list()
        #creating font library
        for i in range(1,51):
            self.font_list.append(pygame.font.SysFont(None,i))
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.center_distance = dict()

    def updateMasterDictionary(self):
        self.courseHandler = ScottyLabsHandler()
        courses = lessCourses(self.courseHandler.courses)
        for course in courses:
            currentNode = courseNode(courses[course]["name"])
            currentNode.addPrereqsFor(self.courseHandler.getPreFor(courses,course))
            currentNode.addPrereqsNeeded(self.courseHandler.getPreNeeded(courses,course))
            self.masterDict[course] = currentNode

    def addSuperScores(self):
        for nodeIDs in self.masterDict:
            self.masterDict[nodeIDs].setSuperScore(getScore(self.masterDict,nodeIDs))


    def keyPressed(self):
        pass

    def mousePressed(self,x,y):
        self.cx=x
        self.cy=y

    def timerFired(self):
        setNodePositions(self.masterDict,self.cx,self.cy,True)

    def drawNodes(self):
        for nodeID in self.masterDict.keys():
            nodeColor=getDepartmentColor(nodeID)
            nodeColor=nodeColor  
            scaling = zoom(self.masterDict[nodeID].x,self.masterDict[nodeID].y,self.width,self.height)
            newRadius = self.masterDict[nodeID].r*scaling
            pygame.draw.circle(self.background,nodeColor,(self.masterDict[nodeID].x,self.masterDict[nodeID].y),int(newRadius))
            self.addText(nodeID, scaling)
            #draw course name
            courseDistance = ((self.width//2-self.masterDict[nodeID].x)**2 + (self.height//2-self.masterDict[nodeID].y)**2)**0.5
            self.center_distance[nodeID] = courseDistance
        self.drawCenterCourse()
        self.drawCenterLines()

    def drawCenterLines(self):
        course = min(self.center_distance, key=self.center_distance.get)
        prereqsFor = self.masterDict[course].getPrereqsFor()
        for prereq in prereqsFor:
            pos1,pos2 = self.masterDict[course].getPosition(),self.masterDict[prereq].getPosition()
            self.drawLine(pos1,pos2)
            #enlarge prereqs
            color=getDepartmentColor(prereq)
            pygame.draw.circle(self.background,color,(self.masterDict[prereq].x,self.masterDict[prereq].y),25)
            self.addText(prereq, 1)

    def drawLine(self,pos1,pos2):
        pygame.draw.aaline(self.background,(255,255,255),pos1,pos2,1)

    def drawCenterCourse(self):
        font = self.font_list[30]
        course = min(self.center_distance, key=self.center_distance.get)
        text = font.render(self.masterDict[course].getCourseName(),True,(250,250,250))
        super_text = font.render("Prereq for: " + str(self.masterDict[course].getSuperScore()) + " courses",True,(250,250,250))
        x, y = self.width//2,30
        newX=x-text.get_width()//2
        newY=y-text.get_height()//2
        secondLineX = x - super_text.get_width()//2
        secondLineY = y - super_text.get_height()//2 + 30
        self.background.blit(text,(newX,newY))
        self.background.blit(super_text,(secondLineX,secondLineY))
            
    def addText(self,nodeID, scaling):
        x, y = self.masterDict[nodeID].x,self.masterDict[nodeID].y
        text = nodeID
        font = self.font_list[int(20*scaling)]
        text=font.render(nodeID, True, (0,0,0))
        newX=x-text.get_width()//2
        newY=y-text.get_height()//2
        self.background.blit(text, (newX,newY))

    def drawAll(self):
        self.background.fill(self.backgroundColor)
        self.backgroundImage=self.backgroundImage.convert()
        self.background.blit(self.backgroundImage,(int(self.backgroundX),int(self.backgroundY)))
        self.drawNodes()
        self.background=self.background.convert()
        self.screen.blit(self.background,(0,0))

    def run(self):
        while self.isRunning:
            (mouseX,mouseY)=pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.isRunning=False
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                    self.isRunning=False
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.xSpeed = 12
                    elif event.key == pygame.K_RIGHT:
                        self.xSpeed = -12
                    elif event.key == pygame.K_UP:
                        self.ySpeed = -12
                    elif event.key == pygame.K_DOWN:
                        self.ySpeed = 12
                elif event.type==pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.xSpeed = 0
                    elif event.key == pygame.K_RIGHT:
                        self.xSpeed = 0
                    elif event.key == pygame.K_UP:
                        self.ySpeed = 0
                    elif event.key == pygame.K_DOWN:
                        self.ySpeed = 0
                elif event.type==pygame.MOUSEBUTTONUP:
                    self.mousePress=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    self.mousePress=True
            self.cx += self.xSpeed
            self.cy -= self.ySpeed
            self.backgroundX+=self.xSpeed/20
            self.backgroundY-=self.ySpeed/20
            if self.mousePress:
                self.mousePressed(mouseX,mouseY)
            self.timerFired()
            self.drawAll()
            pygame.display.update()
        pygame.quit()

def largestSuperScore(courseDict):
        currentLarge = -1

        for nodeIDs in courseDict:
            score = courseDict[nodeIDs].getSuperScore()
            if score > currentLarge:
                currentLarge = score

        return currentLarge

def getAllNLevelCourse(courseDict,n,hasPrereqs):
    L = []
    for courseId, courseNode in courseDict.items():
        if(courseId[3] == 1 and (hasPrereqs == True or len(courseNode.prereqsNeeded) == 0)):
            L.extend(courseID)
    return L

def setNodePositions(courseDict, cx, cy,randomizeAngles=False):
    largest = largestSuperScore(courseDict)
    if not randomizeAngles:
        radiusScalingFactor = 1000;
        for courseId, courseNode in courseDict.items():
            angle = 10*int(courseId[0:2])+ int(courseId[3:6])*2;
            #angle = random.uniform(0, 2*math.pi)
            radius = radiusScalingFactor/(courseNode.superScore+1)
            posX = radius*math.cos(angle)+cx
            posY = cy-radius*math.sin(angle)
            courseNode.setPosition(int(posX),int(posY))
            courseNode.setAngle(angle)
    else:
        radiusScalingFactor=2000
        for courseId, courseNode in courseDict.items():
            factor = 0
            breakPoint = 5
            if courseNode.superScore < breakPoint:
                factor = (breakPoint - courseNode.superScore)*100
            if courseNode.superScore == 0:
                factor += int(courseId[0:2])*10
            radius=((largest-courseNode.superScore) + factor)/2#radiusScalingFactor/(courseNode.superScore+1)+50
            posX=radius*math.cos(courseNode.angle)+cx
            posY=cy-radius*math.sin(courseNode.angle)
            posX,posY=int(posX),int(posY)
            courseNode.setPosition(posX,posY)

if __name__=='__main__':
    testApp=mainApp()
    testApp.run()

