import Player
import GameObject
import threading
import keyThreading
import time
from tkinter import *

class GameEngine:

    WIDTH = 1000
    HEIGHT = 500

    objects = []
    xLocEnd = 200
    yLocEnd = 200
    frameLen = 0.5

    keyQueue = []

    def __init__(self, windowEndX, windowEndY):
        self.xLocEnd = windowEndX
        self.yLocEnd = windowEndY



        window = Tk()
        frame = Frame()
        frame.grid()
        frame.bind("<KeyPress>", self.keydown)
        frame.bind("<KeyRelease>", self.keyup)

        self.canvas = Canvas(frame, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.grid(columnspan=3)

        self.preload()

        self.canvas.focus_set()

    def preload(self):
        photo = PhotoImage(file = 'Ken/1.gif')
        item = self.canvas.create_image(self.WIDTH/2, self.HEIGHT/2, image=photo, tag="ken")

        photo = PhotoImage(file = 'Ken/2.gif')
        item2 = self.canvas.create_image(self.WIDTH/2, self.HEIGHT/2, image=photo, tag="ken")

        self.Player1 = Player("Player1", 100, 25, "Ken/", item)
        self.Player2 = Player("Player2", 100, 75, "Ken/", item2)



        self.objects.append(self.Player1)
        self.objects.append(self.Player2)

    def start(self):
        done = False

        while not done:
            time.sleep(self.frameLen)
            self.updatePlayerMovementState(self.Player1, "a", "d", "w", "s", "g", "h")
            self.updatePlayerMovementState(self.Player2, "left", "right", "up", "down", "/", ".")

            #Movement
            for obj in self.objects:
                if isinstance(obj, Player):
                    if obj.health <= 0:
                        done = True
                        break

                obj.move()
                if obj.location[0] < 0 or obj.location[1] < 0 or obj.location[0] > self.xLocEnd or obj.location[1] > self.xLocEnd:
                    obj.setAlive(False)


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
                    obj.draw()

    def doCollision(self, obj, obj2):
        #run what happens when objects collide
        obj.doCollision(obj2.getDamage())
        obj2.doCollision(obj.getDamage())

    def updatePlayerMovementState(self, player, left, right, up, down, punch, kick):
        keyTotal = [left, right, up, down, punch, kick]
        while self.running:
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



