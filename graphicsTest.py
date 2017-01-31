import time
import msvcrt

from tkinter import *

WIDTH = 1000
HEIGHT = 500

window = Tk()
frame1 = Frame()
frame1.grid()

canvas = Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(columnspan=3)
canvas.focus_set()

done = False
kens = []
photo = PhotoImage(file = 'Ken/1.gif')
photo1 = PhotoImage(file = 'Ken/2.gif')
photo2 = PhotoImage(file = 'Ken/3.gif')
photo3 = PhotoImage(file = 'Ken/4.gif')
photo4 = PhotoImage(file = 'Ken/5.gif')
kens.append(photo)
kens.append(photo1)
kens.append(photo2)
kens.append(photo3)
kens.append(photo4)


item = canvas.create_image(WIDTH/2, HEIGHT/2, image=photo, tag="ken")



kenVal = 0
while not done:
	time.sleep(0.15)
	canvas.itemconfig(item,image=kens[4-kenVal])
	window.update()
	kenVal += 1
	kenVal = kenVal % 5

