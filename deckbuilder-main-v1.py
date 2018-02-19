from tkinter import *
from PIL import Image, ImageTk
from random import randrange
import collection
import card
import deck
import helper

## make the deck and collection windows top levels of the main window
## each the card should have a "make a frame function"

class Deck_Wind:

    def __init__(self,master):
        self.master = master
        self.init_window()
    
    def refresh_cards(self):
        self.use_indx = crd_indx
        self.canvas = Canvas(self.master, width = 975, height = 800)
        self.canvas.grid(row = 0, column = 0)
        
        for i in range(len(self.use_indx)):
            xlocation = (i%4*243)+3
            ylocation = i//4*400            
            
            card_ref = self.use_indx[list(self.use_indx.keys())[i]]  

            card_ref.canvas_image = card_ref.img.subsample(2, 2)
            card_ref.canvas_image = PhotoImage(card_ref.canvas_image, master = self.canvas)
            card_ref.image_label = Label(self.canvas, image = card_ref.canvas_image)

            card_ref.add_button = Button(self.master, text = "Add")

            self.canvas.create_window(xlocation, ylocation, anchor = NW, window = card_ref.add_button)
            #self.canvas.create_line(xlocation,ylocation,xlocation+20,ylocation+20)


            

            
            

    def make_deck(self):
        self.deck_name = self.deck_entry.get()
        self.new_deck = deck.deck(self.deck_name)
        self.name_entry.grid_forget()
        self.name_button.grid_forget()
        self.refresh_cards()
        

    def init_window(self):
        self.master.title("Make a new Deck")
        self.master.configure(background = "black")

        self.deck_entry = StringVar()
        
        self.name_entry = Entry(self.master, textvariable = self.deck_entry)
        self.name_button = Button(self.master, text = "Enter Deck Name", command = self.make_deck)

        self.name_button.grid(row = 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)

        self.deck_entry.set("::Here::")















class   Wind:

    def __init__(self,master):
        self.master=master
        self.init_window()
        self.make_menus()

    def init_window(self):
        self.bckgnd = PhotoImage(file = 'C:/Users/knhou/Google Drive/Python Projects/deckbuilder/bckgnd.gif')
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
        self.deck_window = Toplevel()
        self.deck_functions = Deck_Wind(self.deck_window)


    def coll_update(self):
        print("blah")

    def make_coll(self):
        print("blah blah")

    def make_menus(self):
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






















def main():
    
    mainwindow = Tk()
    disp_wind=Wind(mainwindow)

    mainwindow.mainloop()


if __name__=="__main__":
    main()