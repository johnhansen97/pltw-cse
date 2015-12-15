from tkinter import *	#Tkinter must have been renamed 'tkinter' in python 3
import os.path
from PIL import Image, ImageTk

root = Tk()

canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid()

checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4])
check = canvas.create_line(100, 250, 150, 300, 220, 150, fill='red', width=20)
message = canvas.create_text(380, 250, text='Try this!', font=('Arial', -100))
shadow = canvas.create_oval(100, 450, 500, 550, fill='#888888', outline='#888888')

circles = []
for r in range(10, 60, 10):
	circles.append(canvas.create_oval(300-r, 400-r, 300+r, 400+r, outline='red'))

canopy = canvas.create_arc(0, 50, 600, 650, start=30, extent=120, width=50, style=ARC)

canvas.itemconfig(circles[2], outline='black')
a, b, c, d = canvas.coords(circles[2])
canvas.coords(circles[2], a, b-5, c, d-5)

canvas.itemconfig(circles[0], fill='black', width=3)
a, b, c, d = canvas.coords(circles[0])
canvas.coords(circles[0], a+5, b, c+5, d)

# get a filename in the same directory as this program
 
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'canopyIcon.jpg')

# open the image file and convert to an ImageTk object

img = Image.open(filename) # create a PIL.Image from the jpg file
tkimg = ImageTk.PhotoImage(img) # convert the PIL.Image to a PIL.TkImage

#add the ImageTk object to the canvas
icon = canvas.create_image(150, 250, image=tkimg)

canvas.tag_lower(icon, check)

root.mainloop()
