import time
import msvcrt
from PIL import *

from tkinter import *

from PIL import ImageTk, Image

WIDTH = 1000
HEIGHT = 500

window = Tk()
frame1 = Frame()
frame1.grid()

canvas = Canvas(frame1, width=WIDTH, height=HEIGHT, bg="grey")
canvas.grid(columnspan=3)
canvas.focus_set()

done = False
kens = []
photo = PhotoImage(file = 'Ken/Cody-Idle.png')
item = canvas.create_image(100, 200, image=photo, tag="ken")
#kens.append(photo)

im = Image.open('Ken/Cody-Idle.png')
resize = im.resize((4202,300),Image.ANTIALIAS)
cropped = resize.crop((300, 0, 600, 300))
for i in range(14):
    cropped = resize.crop((i*300, 0, (i+1)*300, 300))
    photo = ImageTk.PhotoImage(cropped)
    kens.append(photo)

kenVal = 0
while not done:
	time.sleep(0.1)
	canvas.itemconfig(item,image=kens[kenVal])
	window.update()
	kenVal += 1
	kenVal = kenVal % 14

