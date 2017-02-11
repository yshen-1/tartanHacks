#!/usr/bin/env/python3
import pygame
from helpers import ScottyLabsHandler, lessCourses
from courseNode import courseNode
import math
import random

def getDepartmentColor(courseID):
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

#put in init
def getMasterDict():
    result_dict = dict()
    course_handler = ScottyLabsHandler()
    course_dict = lessCourses(course_handler.courses)
    courses = course_dict
    for course in courses:
        currentNode = courseNode(courses[course]["name"])
        currentNode.addPrereqsFor(course_handler.getPreFor(courses,course))
        currentNode.addPrereqsNeeded(course_handler.getPreNeeded(courses,course))
        result_dict[course] = currentNode
    return result_dict

master = getMasterDict()
print(master['15-112'].getPrereqsNeeded())
print(master['15-112'].getPrereqsFor())

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

print(getScore(master,'15-122'))


class mainApp(object):
    def __init__(self):
        pygame.init()
        self.resolution=2
        self.height=(1080)//2
        self.width=(1920)//2
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.background=pygame.Surface((self.width,self.height))
        self.background.fill((255,25,255))
        self.background=self.background.convert()
        self.isRunning=True
    def keyPressed(self):
        pass
    def mousePressed(self):
        pass
    def timerFired(self):
        pass
    def drawAll(self):
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
                    seslf.mousePressed()
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

def setNodePositions(courseDict, width, height):
    cx = width//2
    cy = height//2
    radiusScalingFactor = 1000;
    for courseId, courseNode in courseDict.items():
        angle = random.uniform(0, 2*pi)
        radius = radiusScalingFactor/courseNode.superScore
        posX = radius*cos(angle)
        posY = radius*sin(angle)
        courseNode.setPosition(posX,posY)

    
# if __name__=='__main__':
#      testApp=mainApp()
#      testApp.run()
