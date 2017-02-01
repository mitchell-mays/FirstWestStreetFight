import threading
from tkinter import *

class Display(threading.Thread):

    WIDTH = 1000
    HEIGHT = 500

    def __init__(self, engine):
        threading.Thread.__init__(self)

        self.Engine = engine

        self.window = Tk()
        self.frame = Frame()
        self.frame.grid()

        self.canvas = Canvas(self.frame, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.grid(columnspan=3)

        self.start()

    def run(self):
        self.frame.bind("<KeyPress>", self.Engine.keydown)
        self.frame.bind("<KeyRelease>", self.Engine.keyup)
        self.frame.pack()
        self.canvas.focus_set()
        #self.window.after(1000, self.runLoop)
        #self.window.mainloop()

    def getCanvas(self):
        return self.canvas

    def getWindow(self):
        return self.window