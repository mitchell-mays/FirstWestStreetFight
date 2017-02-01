import GameObject
import HitBox

class Player(GameObject.GameObject):
    health = 100
    damage = 10
    name = ""
    myMove = []
    moveState = -1
    jump = False
    frameDict = {}
    framePlace = {}


    def __init__(self, n, h, loc, il, drawItem, pHeight):
        myHitbox = HitBox.HitBox(0, 0, 25, 25)
        GameObject.GameObject.__init__(self, loc, il, myHitbox)

        self.canvasDrawItem = drawItem
        self.name = n
        self.health = h
        self.pHeight = pHeight

    def defineFrames(self, frames):
        self.frameDict = frames
        for key in frames:
            self.framePlace[key] = 0

    def doCollision(self, dam):
        self.health = self.health - dam

    def getDamage(self):
        return self.damage

    def setMove(self, currMove):
        self.myMove = currMove

    def move(self):
        #0: left, 1: right, 2: up, 3: down, 4: punch, 5: kick
        if len(self.myMove) == 0:
            moveState = -1
        elif len(self.myMove) == 1:
            vals = self.myMove[0].split("-")
            if vals[0] == "D":
                moveState = vals[1]

        if moveState == 0:
            self.location[0] -= 5



    def isAlive(self):
        return super(Player, self).isAlive()

    def draw(self, canvas):
        canvas.itemconfig(self.canvasDrawItem, image= self.frameDict[str(self.moveState)][self.framePlace[str(self.moveState)]])
        if self.framePlace[str(self.moveState)] == len(self.frameDict[str(self.moveState)])-1:
            self.framePlace[str(self.moveState)] = 0
        else:
            self.framePlace[str(self.moveState)] += 1
