from tkinter import *

root = Tk()
root.title("Silly cat application")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
text = Label(root, text="Cats are silly")
text.pack()
text2 = Label(root, text="-cool people")
text2.pack()
root.configure(background="black")
# Create Label in our window
image = PhotoImage(file="wow.gif")
img = Label(root, image=image)
img.pack()
root.mainloop()