import Tkinter # often people import Tkinter as *

#####
# Create root window
####
root = Tkinter.Tk()

#####
# Create Model
######
radius_intvar = Tkinter.IntVar()
radius_intvar.set(100) #initialize radius
# center of circle
x = 150
y = 150

######
# Create Controller
#######
# Event handler for slider
def radius_changed(new_intval):
   # Get data from model
   # Could do this: r = int(new_intval)
   r = radius_intvar.get()
   # Controller updating the view
   canvas.coords(circle_item, 0, y+r-300,300, y+r)
# Instantiate and place slider
radius_slider = Tkinter.Scale(root, from_=0, to=300, variable=radius_intvar,
                              label='Radius', command=radius_changed)
radius_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \n to adjust \n circle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()