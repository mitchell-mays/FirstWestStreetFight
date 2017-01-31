import time
import threading
import sys

class keyThreading:
    keyQueue = []
    running = True

    def kill(self):
        self.running = False

    def startMain(self):
        #reads all input from standard in and places on queue
        while self.running:
            try:
                val = sys.stdin.read(1)
            except :
                #do nothing
                val = ''

            self.keyQueue.append(val)

    def updatePlayerMovementState(self, frameLen, player, left, right, up, down, punch, kick):
        keyTotal = [left, right, up, down, punch, kick]
        while self.running:
            time.sleep(frameLen)
            move = []
            if len(self.keyQueue) > 0:
                distort = 0
                for key in range(len(self.keyQueue)):
                    if self.keyQueue[key-distort] in keyTotal:
                        move.append(keyTotal.index(self.keyQueue[key-distort]))
                        del self.keyQueue[key-distort]
                        distort += 1

            player.setMove(move)