#!/usr/bin/env/python3
import pygame
from helpers import ScottyLabsHandler
from courseNode import courseNode
import math

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

#put in init
def getMasterDict():
    result_dict = dict()
    course_handler = ScottyLabsHandler()
    for course in course_handler.courses:
        currentNode = courseNode(course_handler.courses[course]["name"])
        currentNode.addPrereqsFor(course_handler.getPreFor(course_handler.courses,course))
        currentNode.addPrereqsNeeded(course_handler.getPreNeeded(course_handler.courses,course))
        result_dict[course] = courseNode
    return result_dict

dict_example = getMasterDict()
print(dict_example['15-112'].prereqsFor)


# class mainApp(object):
#     def __init__(self):
#         pygame.init()
#         self.resolution=2
#         self.height=(1080)//2
#         self.width=(1920)//2
#         self.screen=pygame.display.set_mode((self.width,self.height))
#         self.background=pygame.Surface((self.width,self.height))
#         self.background.fill((255,25,255))
#         self.background=self.background.convert()
#         self.isRunning=True
#     def keyPressed(self):
#         pass
#     def mousePressed(self):
#         pass
#     def timerFired(self):
#         pass
#     def drawAll(self):
#         self.background=self.background.convert()
#         self.screen.blit(self.background,(0,0))
#     def run(self):
#         while self.isRunning:
#             (mouseX,mouseY)=pygame.mouse.get_pos()
#             for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                     self.isRunning=False
#                 elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
#                     self.isRunning=False
#                 elif event.type==pygame.KEYDOWN:
#                     self.keyPressed()
#                 elif event.type==pygame.MOUSEBUTTONUP:
#                     seslf.mousePressed()
#             self.timerFired()
#             self.drawAll()
#             pygame.display.update()
#         pygame.quit()
# def getAllNLevelNoPrereqs(courseDict,n):
#     L = []
#     for courseId, courseNode in courseDict.items():
#         if(courseId[3] == 1 and len(courseNode.prereqsNeeded) == 0):
#             L.extend(courseNode)
#     return L
# def setNodePositions(courseDict, width, height):
#     cx = width//2
#     cy = height//2
#     rInterval = 50
#     #Step 1, get 100-level course with no preqs
#     L1 = getAllNLevelNoPrereqs(courseDict)
   
#     angle = 2*math.pi/len(L1)
#     for i in range(len(L1)):
#         xPos = rInterval*math.cos(angle*i)
#         yPos = rInterval*math.sin(angle*i)
#         L1[i].setPosition(xPos,yPos)

# if __name__=='__main__':
#     testApp=mainApp()
#     testApp.run()
