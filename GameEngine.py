import Player
import GameObject
import time
from tkinter import *
from PIL import ImageTk, Image

class GameEngine:

    WIDTH = 1000
    HEIGHT = 500

    objects = []
    xLocEnd = 200
    yLocEnd = 200
    frameLen = 0.05

    keyQueue = []

    p1StartX = 100
    p2StartX = 800

    currDir = "C:/Users/napster/PycharmProjects/FirstWestStreetFight/"

    def __init__(self, windowEndX, windowEndY, player1Name, player2Name, playerSize):
        self.xLocEnd = windowEndX
        self.yLocEnd = windowEndY

        self.window = Tk()
        self.frame = Frame(self.window)
        self.frame.grid()


        self.canvas = Canvas(self.frame, width=self.WIDTH, height=self.HEIGHT, bg="grey")
        self.canvas.grid(columnspan=3)


        self.preload(player1Name, player2Name, playerSize)


    def preload(self, player1, player2, pSize):
        idles = []
        im = Image.open(player1 + "/Idle.png")
        resize = im.resize((4202,300), Image.ANTIALIAS)
        for i in range(14):
            cropped = resize.crop((i*300, 0, (i+1)*300, 300))
            photo = ImageTk.PhotoImage(cropped)
            idles.append(photo)

        item = self.canvas.create_image(self.p1StartX, self.HEIGHT/2, image=idles[0], tag="ken")
        item2 = self.canvas.create_image(self.p2StartX, self.HEIGHT/2, image=idles[0], tag="ken")


        self.Player1 = Player.Player("Player1", 100, [self.p1StartX, self.HEIGHT/2], item)
        self.Player2 = Player.Player("Player2", 100, [self.p2StartX, self.HEIGHT/2], item2)

        frames = {}
        frames["-1"] = idles
        frames["0"] = idles
        frames["1"] = idles
        frames["2"] = idles
        frames["3"] = idles
        frames["4"] = idles
        frames["5"] = idles

        self.Player1.defineFrames(frames)
        self.Player2.defineFrames(frames)

        self.objects.append(self.Player1)
        self.objects.append(self.Player2)

    def start(self):
        self.frame.bind("<KeyPress>", self.keydown)
        self.frame.bind("<KeyRelease>", self.keyup)
        self.frame.pack()
        self.frame.focus_set()
        self.runLoop()
        self.window.mainloop()
        #self.window.after(10, self.captureKeys)


    def runLoop(self):

        done = False

        #while not done:
        if not done:
            time.sleep(self.frameLen)
            self.updatePlayerMovementState(self.Player1, "a", "d", "w", "s", "g", "h")
            self.updatePlayerMovementState(self.Player2, "Left", "Right", "Up", "Down", "/", ".")

            #Movement
            for obj in self.objects:

                #check if player has died
                if isinstance(obj, Player.Player):
                    if obj.health <= 0:
                        done = True
                        break

                obj.move()
                #if obj.location[0] < 0 or obj.location[1] < 0 or obj.location[0] > self.xLocEnd or obj.location[1] > self.xLocEnd:
                #    obj.setAlive(False)


            #Collision
            for obj in self.objects:
                for obj2 in self.objects:
                    if not obj is obj2:
                        if obj.isAlive() and obj2.isAlive():
                            if doesCollide(obj.getHitBox(), obj2.getHitBox()):
                                self.doCollision(obj, obj2)

            #Draw
            for obj in self.objects:
                if obj.isAlive():
                    obj.draw(self.canvas)

            #refresh what is shown
            self.window.update()


            self.window.after(0, self.runLoop)

    def doCollision(self, obj, obj2):
        #run what happens when objects collide
        obj.doCollision(obj2.getDamage())
        obj2.doCollision(obj.getDamage())

    def updatePlayerMovementState(self, player, left, right, up, down, punch, kick):
        keyTotal = [left, right, up, down, punch, kick]

        move = []
        if len(self.keyQueue) > 0:
            distort = 0
            for key in range(len(self.keyQueue)):
                if self.keyQueue[key-distort].split("-")[1] in keyTotal:
                    move.append(self.keyQueue[key-distort].split("-")[0] + "-" + str(keyTotal.index(self.keyQueue[key-distort].split("-")[1])))
                    del self.keyQueue[key-distort]
                    distort += 1

        player.setMove(move)

    def keydown(self, e):
        if e.char == '':
            val = e.keysym
        else:
            val = e.char

        self.keyQueue.append("D-" + val)

    def keyup(self, e):
        if e.char == '':
            val = e.keysym
        else:
            val = e.char

        self.keyQueue.append("U-" + val)

def doesCollide(hitbox1, hitbox2):
    h1Start = hitbox1.getStart()
    h2Start = hitbox2.getStart()

    h1End = hitbox1.getEnd()
    h2End = hitbox2.getEnd()

    if h1Start[0] > h2Start[0] and h1Start[0] < h2End[0] and h1Start[1] > h2Start[1] and h1Start[1] < h2End[1]:
        return True
    else:
        return False


