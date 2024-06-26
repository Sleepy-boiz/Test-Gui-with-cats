from tkinter import *

root = Tk()  # create parent window

def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

# Create volume up button
vol_up = Button(root, text="+")
vol_up.pack()
root.mainloop()
#The function volumeUp() is called whenever the vol_up button is clicked in the window. Now that we have a basic understanding of how to use the Button widget, the next step is to add more functionality to our TV remote. When the turn_on button is clicked, let's create a window that opens up and displays an image. Then for vol_down let's also print out a message to keep things simple for now. The following displays the code and each button has a command parameter.

PYTHON
from tkinter import *

root = Tk()  # create parent window

def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

def volumeDown():
    '''output message to terminal to tell that the button is working'''
    print("Volume Decrease -1")

# use Button and Label widgets to create a simple TV remote
def turnOnTV():
    '''callback method used for turn_on button'''
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(root)
    window.title("TV")
    image = PhotoImage(file="rain.gif")

    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()

turn_on = Button(root, text="ON", command=turnOnTV)
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()

root.mainloop()