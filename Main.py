import pygame as pg
import numpy as np
import time
from math import radians, cos, sin, asin, sqrt
from osu.circle import Circle
from osu.framecounter import FrameCounter
from osu.points import Pointhandler
def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def loadmap(m,aa,ph):
    with np.load(f"maps/{m}.npz") as data:
        mdata = []
        a = data['arr_0']
        b = data['arr_1']
        c = data['arr_3']
        n = 0
        for i in data['arr_2']:
            mdata.append(Circle(i,a[n],b[n],c[n], aa,ph))
            n += 1
            
        return(mdata)
            







def Gameloop():
    clock = pg.time.Clock()
    running = True
    window = pg.display.set_mode((640, 480))
    window.fill((255, 255, 255))
    btn = pg.Rect(0, 0, 100, 30)
    
    loadedmap = []
    counter = FrameCounter()
    closeframes = 0
    ar = 60
    pointhandler = Pointhandler()
    while running:

        for e in pg.event.get():
            if e.type == pg.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pg.mouse.get_pos()
                if(btn.collidepoint((mouseX, mouseY))):
                    loadedmap = loadmap("1",ar,pointhandler)
                    counter.reset()
                    closeframes = int(len(loadedmap) / 3)
                    counter.scount(True)
                if loadedmap != []:
                    ll = loadedmap[0]
                    # pg.draw.circle(window,(0,255,0), (arduino_map(ll.x, 0,1,0,640),arduino_map(ll.y, 0,1,0,480)), 5)
                    if ll.hit(mouseX,mouseY):
                        
                        print(f"hit -- {ll.isClose(counter.nframes())}")
                        ll.points(ll.isClose(counter.nframes()))
                        
            if e.type == pg.QUIT:
                running = False
        #end event handling
        if loadedmap != []:
            window.fill((255, 255, 255))
            frame = counter.nframes()
            l = loadedmap[:closeframes]
            l.reverse()
            for i in l:
                if i.isClose(frame) != -(ar * 100):
                    i.render(window,640,480,i.isClose(frame))
                    
                if i.deleted():
                    loadedmap.remove(i)
                    
                
        pg.draw.rect(window, (0, 255, 255), btn)
        
        clock.tick(60)
        pg.display.flip()
        counter.count()

    #end main loop

def init():
    pg.init()
def Main():
    Gameloop()
    pg.quit()
    
init()
Main()
