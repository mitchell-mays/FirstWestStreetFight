import GameObject
import HitBox

class Player:
    health = 100
    damage = 10
    name = ""
    move = []
    moveState = -1
    jump = False

    def __init__(self, n, h, loc, il):
        myHitbox = HitBox(0, 0, 25, 25)
        GameObject.__init__(self, loc, il, myHitbox)

        self.name = n
        self.health = h

    def doCollision(self, dam):
        self.health = self.health - dam

    def getDamage(self):
        return self.damage

    def setMove(self, currMove):
        self.move = currMove

    def move(self):
        #0: left, 1: right, 2: up, 3: down, 4: punch, 5: kick
        if len(self.move) == 0:
            moveState = -1
        elif len(self.move) == 1:
            vals = self.move[0].split("-")
            if vals[0] == "D":
                moveState = vals[1]



    def draw(self):
        x=1
