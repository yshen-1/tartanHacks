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

    csBaseColor=[204,0,0]
    eceBaseColor=[51,204,51]
    divisor=max((4-idCourseLevel),1)
    
    if idPrefix=="15":
        for i in range(len(csBaseColor)):
            csBaseColor[i]=csBaseColor[i]//divisor
        return csBaseColor
    elif idPrefix=="18":
        for i in range(len(eceBaseColor)):
            eceBaseColor[i]=eceBaseColor[i]//divisor
        return eceBaseColor

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
        self.backgroundColor=(255,25,255)
        self.background.fill(self.backgroundColor)
        self.background=self.background.convert()
        self.isRunning=True
        self.masterDict=dict()
        self.updateMasterDictionary()
        self.addSuperScores()
        self.mousePress=False
        self.cx,self.cy=self.width//2,self.height//2
        setNodePositions(self.masterDict,self.cx,self.cy) 
        self.font_list = list()
        for i in range(1,51):
            self.font_list.append(pygame.font.SysFont(None,i))
        self.xSpeed = 0;
        self.ySpeed = 0;

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
            nodeColor=nodeColor if nodeColor!=None else [150,30,150]
            scaling = zoom(self.masterDict[nodeID].x,self.masterDict[nodeID].y,self.width,self.height)
            newRadius = self.masterDict[nodeID].r*scaling
            pygame.draw.circle(self.background,nodeColor,(self.masterDict[nodeID].x,self.masterDict[nodeID].y),int(newRadius))
            self.addText(nodeID, scaling)
            
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
                        self.xSpeed = 8
                    elif event.key == pygame.K_RIGHT:
                        self.xSpeed = -8
                    elif event.key == pygame.K_UP:
                        self.ySpeed = -8
                    elif event.key == pygame.K_DOWN:
                        self.ySpeed = 8
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
            radius=((largest-courseNode.superScore) + factor)#radiusScalingFactor/(courseNode.superScore+1)+50
            posX=radius*math.cos(courseNode.angle)+cx
            posY=cy-radius*math.sin(courseNode.angle)
            posX,posY=int(posX),int(posY)
            courseNode.setPosition(posX,posY)

if __name__=='__main__':
    testApp=mainApp()
    testApp.run()

