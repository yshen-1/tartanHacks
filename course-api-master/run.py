#!/usr/bin/env/python3
import pygame

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
            self.timerFired()
            self.drawAll()
            pygame.display.update()
        pygame.quit()
if __name__=='__main__':
    testApp=mainApp()
    testApp.run()
