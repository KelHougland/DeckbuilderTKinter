from tkinter import *
from PIL import Image, ImageTk
twig=Tk()
img=Image.open("C:/Users/knhou/Google Drive/Python Projects/deckbuilder/images/opusi_001.jpg")
photo=ImageTk.PhotoImage(img)
label=Label(twig,image=photo)
label.pack()
twig.mainloop()