from tkinter import *
from PIL import Image, ImageTk
from random import randrange
import collection
import card
import deck
import helper

## make the deck and collection windows top levels of the main window
## each the card should have a "make a frame function"


class   Wind:

    def __init__(self,master):
        self.master=master
        self.init_window()
        self.make_mainmenus()

    def init_window(self):
        self.bckgnd = PhotoImage(file = 'bckgnd.gif')
        self.bg_label = Label(self.master,image = self.bckgnd)
        self.bg_label.pack()
        self.master.title("FFTCG DeckBuilder and Collection Archive")

    def load_indx(self):
        global crd_indx
        crd_indx = helper.init_index()

    def load_collection(self):
        # this should allow a user to choose a file from a directory
        global crd_indx
        crd_indx = helper.init_collection("collection.txt")

    def load_deck(self):
        # this should load a deck, for now it just says
        print("FIX THIS FUNCTION")

    def make_deck1(self):
        self.hide_mainmenus()
        print("Make this WORK")


    def coll_update(self):
        print("blah")

    def make_coll(self):
        print("blah blah")

    def make_mainmenus(self):
        self.menu_var = Menu(self.master)
        self.master.config(menu = self.menu_var)
        
        self.file_menu = Menu(self.menu_var)
        self.menu_var.add_cascade(label = "File", menu = self.file_menu)     
        self.file_menu.add_command(label = "Load All Cards to Use", command = self.load_indx)
        self.file_menu.add_command(label = "Load a Collection to use", command = self.load_collection)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.master.destroy)

        self.deck_menu = Menu(self.menu_var)
        self.menu_var.add_cascade(label = "Decks", menu = self.deck_menu)
        self.deck_menu.add_command(label = "Load a Deck", command = self.load_deck)
        self.deck_menu.add_command(label = "Make a New Deck", command = self.make_deck1)

        self.coll_menu = Menu(self.menu_var)
        self.menu_var.add_cascade(label = "Collections", menu = self.coll_menu)
        self.coll_menu.add_command(label = "Update an Exisiting Collection", command = self.coll_update)
        self.coll_menu.add_command(label = "Start a New Collection", command = self.make_coll)


    def hide_mainmenus(self):
        self.menu_var.entryconfig("File", state = "disabled")
        self.menu_var.entryconfig("Decks", state = "disabled")
        self.menu_var.entryconfig("Collections", state = "disabled")






















def main():
    
    mainwindow = Tk()
    disp_wind=Wind(mainwindow)

    mainwindow.mainloop()


if __name__=="__main__":
    main()