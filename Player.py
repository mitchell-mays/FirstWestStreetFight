import GameObject
import HitBox

class Player(GameObject.GameObject):

    def __init__(self, n, h, loc, drawItem):
        myHitbox = HitBox.HitBox(0, 0, 25, 25)
        GameObject.GameObject.__init__(self, loc, myHitbox)

        self.canvasDrawItem = drawItem
        self.name = n
        self.health = h
        #0: left, 1: right, 2: up, 3: down, 4: punch, 5: kick
        self.keysPressed = [False, False, False, False, False, False]

        self.moveState = -1
        self.jump = False

        self.moveFrame = 0

        self.health = 100
        self.damage = 10
        self.name = ""
        self.myMove = []

        self.frameDict = {}
        self.framePlace = {}

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
            kPress = False
            keyIndex = 0
            for key in range(len(self.keysPressed)):
                if self.keysPressed[key]:
                    kPress = True
                    keyIndex = key

            if not kPress:
                #refresh frame for switch
                if not (self.moveState == -1):
                    self.framePlace[str(-1)] = 0
                self.moveState = -1

            else:
                self.moveState = keyIndex

        elif len(self.myMove) == 1:
            vals = self.myMove[0].split("-")
            if vals[0] == "D":
                self.keysPressed[int(vals[1])] = True

                #refresh frame for switch
                if not (self.moveState == int(vals[1])):
                    self.framePlace[vals[1]] = 0

                self.moveState = int(vals[1])
            else:
                #key release
                self.keysPressed[int(vals[1])] = False

        elif len(self.myMove) > 1:
            for move in self.myMove:
                vals = move.split("-")
                if vals[0] == "D":
                    self.keysPressed[int(vals[1])] = True

                    #refresh frame for switch
                    if not (self.moveState == int(vals[1])):
                        self.framePlace[vals[1]] = 0

                    self.moveState = int(vals[1])
                else:
                    #key release
                    self.keysPressed[int(vals[1])] = False


        if self.moveState == 0:
            self.location[0] -= 10
        elif self.moveState == 1:
            self.location[0] += 10
        elif self.moveState == 2:
            if self.jump == False:
                #for key in range(len(self.keysPressed)):
                #    if key != 2:
                #        kPress = False
                self.jump = True
                self.moveFrame = 0



        if self.jump:
            if self.moveFrame <= 10:
                self.location[1] += self.calcJump(self.moveFrame)
                self.moveFrame += 1
            else:
                self.jump = False

    def isAlive(self):
        return super(Player, self).isAlive()

    def draw(self, canvas):
        canvas.itemconfig(self.canvasDrawItem, image= self.frameDict[str(self.moveState)][self.framePlace[str(self.moveState)]])
        canvas.coords(self.canvasDrawItem, self.location)
        if self.framePlace[str(self.moveState)] == len(self.frameDict[str(self.moveState)])-1:
            self.framePlace[str(self.moveState)] = 0
        else:
            self.framePlace[str(self.moveState)] += 1

    def calcJump(self, moveFrame):
        val = (moveFrame - 5)
        speed = 2*pow(val,2)
        direction = -1
        if val > 0:
            direction = 1

        return speed * direction
