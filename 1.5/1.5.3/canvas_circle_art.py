#####
# canvas_circle_art.py
#
# Draws shapes by dragging on a canvas.
# Three sliders control the fill color  
# Editor shows the current color in tkinter's '#rrggbb' hexadecimal format
#
# (c) 2013 PLTW
# 
# 
#####
import tkinter

####
# Create the main window
####
root = tkinter.Tk()
root.wm_title('Color-Shape Art Creation')

######
# Create a text editor window for displaying information
#######
editor = tkinter.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)

######
# Create a canvas and place it
#######
canvas = tkinter.Canvas(root, height=300, width=300, background='#FFFFFF')
canvas.grid(row=0, column=1, rowspan=3)

######
# Instantiate three IntVars
#####
# Create the model's variables
red_intvar = tkinter.IntVar()
green_intvar = tkinter.IntVar()
blue_intvar = tkinter.IntVar()
# Create a list of circles on the canvas
shapes = []

#######
# Define a new class, an abstraction of the sliders
#######
class ColorSlider(tkinter.Scale): # ColorSlider is a subclass of tkinter.Scale
    '''A Scale that reports to editor and stores in IntVar
    '''
    def __init__(self, parent, myLabel, model_intvar, editor, canvas):
        '''Creates a new ColorSlider'''
        # Define the event handler for the slider moving 
        def slider_changed(new_val):
            # Handler passes data from this controller to two views 
            
            
            
            # Create a hex string from the model data
            tk_color_string = color(red_intvar, green_intvar, blue_intvar)# the sliders' data
            # Tell the text window view about it
            editor.insert(tkinter.END, tk_color_string+'\n')
            editor.see(tkinter.END)
            # Tell the canvas view about it
            # The canvas view holds the model data in its internal canvas items
            # The viewer exposes the data through itemconfig() and itemcoords()
            canvas.itemconfig(shapes[-1],fill=tk_color_string)

        # To finish creating a ColorSlider, call the constructor for a regular
        # tkinter.Scale, associated with the model data and the event handler
        tkinter.Scale.__init__(self, parent, orient=tkinter.HORIZONTAL, from_=0, to=255,
                                variable=model_intvar, label=myLabel, command=slider_changed)
                
######
# Instantiate three sliders
#####

# Create and place the controllers
red_slider = ColorSlider(root, 'Red:', red_intvar, editor, canvas)
red_slider.grid(row=1, column=0, sticky=tkinter.W)

green_slider = ColorSlider(root, 'Green:', green_intvar, editor, canvas)
green_slider.grid(row=2, column=0, sticky=tkinter.W)

blue_slider = ColorSlider(root, 'Blue:', blue_intvar, editor, canvas)
blue_slider.grid(row=3, column=0, sticky=tkinter.W)    

######
# Inform user of mouse interface
######
message = tkinter.Label(root, text='Drag mouse to\ndraw circles.\nDrag sliders\nto change color.')
message.grid(column=0, row=0, sticky=tkinter.N)

#######
# Draw a bunch of circles on the canvas
######

for x in range(10,300,40):
    y = x # So that circles are along diagonal line y=x 
    r = 30 # All the circles will have this radius
    new_circle = canvas.create_oval(x-r, y-r, x+r, y+r, outline='#000000')
    shapes.append(new_circle) # aggregate a list of the shapes on the canvas
canvas.itemconfig(shapes[4],outline='green')

#####
# Create canvas mouse event handlers
#####

# Initialize globals so function defs can assign to them
startx, starty = 300, 300 

# Define canvas' mouse-button event handler
def down(event): # A mouse event will be passed in with x and y attributes
    global startx, starty # Use global variables for assignment
    startx = event.x # Store the mouse down coordinates in the global variables
    starty = event.y

def up(event):
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    r = (startx-event.x)**2 + (starty-event.y)**2  # Pythagorean theorem
    r = int(r**.5)                                 # square root to get distance
    new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                    fill=tk_color_string, outline='#000000')
    shapes.append(new_shape) # aggregate the canvas' item
    
# Subscribe handlers to the Button-1 and ButtonRelease-1 events
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

######
# Functions to transform Intvars into tkinter color strings
#######
def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a string representing two hexadecimal digits
    '''
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits

def color(r,g,b):
    '''Takes three IntVar and returns a color tkinter string like #FFFFFF.        
    '''
    rx=hexstring(r)
    gx=hexstring(g)
    bx=hexstring(b)
    return '#'+rx+gx+bx

# Enter event loop
root.mainloop()
