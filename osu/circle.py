import pygame
import math

def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class Circle:
    def __init__(self,time,x,y,img,ar,ph):
        self.time = time
        self.x = x
        self.y = y
        self.img = img
        self.ar = ar
        self.clicked = False
        self.done = False
        self.resx = 0
        self.resy = 0
        self.base = 60
        self.arwidth = 5 * (self.ar / self.base)
        self.ph = ph
        
    def isClose(self,time):
        # print(time)
        # print(self.time)
        # print(self.ar)
        if time - self.time - self.ar < (self.ar + 1) and time - self.time > -(self.ar * 2):
            return -(time - self.time)
        else:
            return(-(self.ar * 100))
        
    def render(self,window,resx,resy,s):
        self.resx = resx
        self.resy = resy
        if s >= 20 * (self.ar / self.base) and not self.clicked:
            # print(int(min(arduino_map(s + 5, 0, (self.ar * 2), 0, 65), 65)))
            pygame.draw.circle(window,(255,255,255), (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), float(min(arduino_map(s + self.arwidth, 0, (self.ar * 2), 0, (self.base + self.arwidth)), (self.base + self.arwidth))))
            pygame.draw.circle(window,self.img, (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), float(min(arduino_map(s + self.arwidth, 0, (self.ar * 2), 0, (self.base + self.arwidth)), (self.base + self.arwidth))))
            pygame.draw.circle(window,(255,255,255), (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), float(min(arduino_map(s, 0, (self.ar * 2), 0, self.base), self.base)))
            if s >= 44 * (self.ar / self.base):
                pygame.draw.circle(window,(0,255,0), (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), 20)
            else:
                pygame.draw.circle(window,(0,0,255), (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), 20)
        if s <= 20 * (self.ar / self.base) and not s == -(self.ar * self.base):
            pygame.draw.circle(window,(255,255,255), (arduino_map(self.x, 0,1,0,resx),arduino_map(self.y, 0,1,0,resy)), 20)
            self.ph.miss()
            self.done = True
        # if s == -(self.ar):
        #     self.done = True
            
    def hit(self,x,y):
        sqx = (x - arduino_map(self.x, 0,1,0,self.resx))**2
        sqy = (y - arduino_map(self.y, 0,1,0,self.resy))**2
        if math.sqrt(sqx + sqy) < 40:
            return True
        else: 
            return False
            
            
    def points(self,s):
        if s >= 10 * (self.ar / self.base) and s <= 50 * (self.ar / self.base) and not s <= 0 and not self.clicked:
            p = int((((45 * (self.ar / self.base)) - abs((45 * (self.ar / self.base) - s))) * 2.2) / (self.ar / self.base)) #point calc equasion shit
            print(p)
            self.clicked = True
            self.done = True
        else:
            self.ph.miss()
            self.clicked = True
            self.done = True
            
            
    def deleted(self):
        return self.done