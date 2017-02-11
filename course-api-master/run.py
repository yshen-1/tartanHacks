#!/usr/bin/env/python3
import pygame
from helpers import ScottyLabsHandler
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
'''
#put in init
def getMasterDict():
    result_dict = dict()
    course_handler = ScottyLabsHandler()
    for course in course_handler.courses:
        currentNode = courseNode(course_handler.courses[course]["name"])
        currentNode.addPrereqsFor(course_handler.getPreFor(course_handler.courses,course))
        currentNode.addPrereqsNeeded(course_handler.getPreNeeded(course_handler.courses,course))
        result_dict[course] = currentNode
    return result_dict
'''
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
#        pygame.init()
        self.resolution=2
        self.height=(1080)//2
        self.width=(1920)//2
#        self.screen=pygame.display.set_mode((self.width,self.height))
#        self.background=pygame.Surface((self.width,self.height))
        self.backgroundColor=(255,25,255)
#        self.background.fill(self.backgroundColor)
#        self.background=self.background.convert()
        self.isRunning=True
        self.masterDict=dict()
        self.updateMasterDictionary()
        print("Dict updated!")
        self.addSuperScores()
#        self.mousePressed=False
        self.cx,self.cy=self.width//2,self.height//2
    def updateMasterDictionary(self):
        self.courseHandler=ScottyLabsHandler()
        for course in self.courseHandler.courses:
            currentNode=courseNode(self.courseHandler.courses[course]['name'])
            currentNode.addPrereqsFor(self.courseHandler.getPreFor(self.courseHandler.courses,course))
            currentNode.addPrereqsNeeded(self.courseHandler.getPreNeeded(self.courseHandler.courses,course))
            self.masterDict[course]=currentNode
    def addSuperScores(self):
        for nodeIDs in self.masterDict:
            print(nodeIDs)
            self.masterDict[nodeIDs].setSuperScore(getScore(self.masterDict,nodeIDs))
    def keyPressed(self):
        pass
    def mousePressed(self,x,y):
        self.cx=x
        self.cy=y
    def timerFired(self):
        setNodePositions(self.masterDict,self.cx,self.cy)
    def drawNodes(self):
        for nodeID in self.masterDict.keys():
            nodeColor=getDepartmentColor(nodeID)
            nodeColor=nodeColor if nodeColor!=None else [150,30,150]
            pygame.draw.circle(self.background,nodeColor,(self.masterDict[nodeID].x,self.masterDict[nodeID].y),self.masterDict[nodeID].r)
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
                    self.keyPressed()
                elif event.type==pygame.MOUSEBUTTONUP:
                    self.mousePressed=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    self.mousePressed=True
            if self.mousePressed:
                self.mousePressed(mouseX,mouseY)
            self.timerFired()
            self.drawAll()
            pygame.display.update()
        pygame.quit()


def getAllNLevelCourse(courseDict,n,hasPrereqs):
    L = []
    for courseId, courseNode in courseDict.items():
        if(courseId[3] == 1 and (hasPrereqs == True or len(courseNode.prereqsNeeded) == 0)):
            L.extend(courseID)
    return L

def setNodePositions(courseDict, cx, cy):
    radiusScalingFactor = 1000;
    for courseId, courseNode in courseDict.items():
        angle = random.uniform(0, 2*pi)
        radius = radiusScalingFactor/courseNode.superScore
        posX = radius*cos(angle)+cx
        posY = cy-radius*sin(angle)
        courseNode.setPosition(posX,posY)

    
if __name__=='__main__':
     testApp=mainApp()
#     testApp.run()
