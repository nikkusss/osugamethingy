class Pointhandler:
    def __init__(self):
        self.combo = 0
        self.score = 0
        self.history = []
        
    
    
    def miss(self):
        self.combo = 0
    
    
    def okay(self):
        self.combo += 1
        self.score += 100 * max(self.combo / 8,100)
        self.history.append(100)
    
    def good(self):
        self.combo += 1
        self.score += 200 * max(self.combo / 8,200)
        self.history.append(200)
        
    def perfect(self):
        self.combo += 1
        self.score += 300 * max(self.combo / 8,300)
        self.history.append(300)
    
    
    def reset(self):
        self.combo = 0
        self.score = 0
        self.history = []