class FrameCounter:
    def __init__(self):
        self.cframes = False
        self.frames = 0
        
    def count(self):
        if self.cframes == True: 
            self.frames += 1
        
    def reset(self):
        self.frames = 0
    
    def nframes(self):
        return self.frames
    
    
    def scount(self,b):
        self.cframes = b