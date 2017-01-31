import HitBox

class GameObject:

    location = [0, 0]
    #image location is going to be formatted like so
    #imageLocation will hold folder name
    #the draw function will access files that are named in these convention IDLE-1.gif
    #iterating through the sprite will update the number

    imageLocation = ""
    hitbox = HitBox(0, 0, 0, 0)
    alive = True

    def __init__(self, l, il, hb):
        self.location = l
        self.imageLocation = il
        self.hitbox = hb

    def move(self):
        #Generic move function
        self.location = self.location + 1
        self.hitbox.moveX(1)

    def getLocation(self):
        return self.location

    def getHitBox(self):
        return self.hitbox

    def setAlive(self, al):
        self.alive = al

    def isAlive(self):
        return self.alive

    def draw(self):
        #Draw method -- to implement
        x = 1

    def doCollision(self, dam):
        self.alive = False

    def getDamage(self):
        return 0