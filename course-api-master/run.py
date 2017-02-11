#!/usr/bin/env/python3
import pygame
import helpers, courseNode
import math
import random

def getDepartmentColor():
    idPrefix=courseID[0:2]
    idCourseLevel=int(course[3])

    csBaseColor=(204,0,0)
    eceBaseColor=(51,204,51)
    divisor=max((4-idCourseLevel),1)
    
    if idPrefix=="15":
        for i in csBaseColor:
            i=i//divisor
            return csBaseColor
    elif idPrefix=="18":
        for i in eceBaseColor:
            i=i // divisor
            return eceBaseColor

def getMasterDict(courses):
    result_dict = dict()
    for course in courses:
        currentNode = courseNode()


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
    L= []
    for courseId, courseNode in courseDict.items():
        if(courseId[3] == 1 and (hasPrereqs == True or len(courseNode.prereqsNeeded) == 0)):
            L.extend(courseID)
    return L

def setNodePositions(courseDict, width, height):
    cx = width//2
    cy = height//2
    radiusScalingFactor = 20;
    for courseId, courseNode in courseDict.items():
        angle = random.uniform(0, 2*pi)
        radius = courseNode.superScore*radiusScalingFactor
        posX = radius*cos(angle)
        posY = radius*sin(angle)
        courseNode.setPosition(posX,posY)
    

if __name__=='__main__':
    testApp=mainApp()
    testApp.run()
