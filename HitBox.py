class HitBox:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, xStart, yStart, xEnd, yEnd):
        self.x1 = xStart
        self.y1 = yStart
        self.x2 = xEnd
        self.y2 = yEnd

    def setStart(self, x, y):
        self.x1 = x
        self.y1 = y

    def setEnd(self, x, y):
        self.x2 = x
        self.y2 = y

    def getStart(self):
        return [self.x1, self.y1]

    def getEnd(self):
        return [self.x1, self.y1]

    def moveX(self, change):
        self.x1 += change
        self.x2 += change

    def moveY(self, change):
        self.y1 += change
        self.y2 += change