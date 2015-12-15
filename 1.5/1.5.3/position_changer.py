#####
# radius_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter

#####
# Create root window 
####
root = tkinter.Tk()

#####
# Create Model
######
position_intvar = tkinter.IntVar()
position_intvar.set(150) #initialize position
# center of circle
r = 100
x = 150 


######
# Create Controller
#######
# Event handler for slider
def position_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    y = position_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
# Instantiate and place slider
position_slider = tkinter.Scale(root, from_=1, to=300, variable=position_intvar,    
                              label='y Coordinate', command=position_changed)
position_slider.grid(row=1, column=0, sticky=tkinter.W)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
y = position_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()
