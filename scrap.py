
    def make_deck2(self):
        self.new_deck = deck(self.deck_entry.get())
        self.deck_namebutton.grid_forget()
        self.deck_entry.grid_forget()
        self.refresh_cards(crd_indx)

    def refresh_cards(self,indx):
        self.use_indx = crd_indx
        self.frames4cards = {}
        for i in range(len(self.use_indx)):
            card_ref = self.use_indx[list(self.use_indx.keys())[i]]
            card_ref.frame=Frame(self.deck_window, padX = 3, padY = 3)
            card_ref.frame.pack()
            card_ref.canvas=Canvas(card_ref.frame, width = 120, height = 167)
            card_ref.canvas_image = card_ref.img.subsample(4, 4)
            card_ref.canvas.create_image(0, 0, image = card_ref.canvas_image, anchor = "nw")
            card_ref.canvas.grid(row = 0, column = 0, columnspan = 2)
            card_ref.add_button = Button(card_ref.frame, text = "Add", command = self.new_deck.add_card(card_ref))
            card_ref.rm_button = Button(card_ref.frame, text = "Remove", command = self.new_deck.rm_card(card_ref))
            card_ref.add_button.grid(row = 1, column =0)
            card_ref.rm_button.grid(row = 1, column = 1)

    def make_deck1(self):
        self.deck_window = Toplevel(self.master)
        deck_window.title("Make a New Deck")
        deck_window.configure(background = 'black')
        
        self.deck_name = StringVar()
        self.deck_entry = Entry(deck_window, textvariable = self.deck_name) # (place for input, where it is stored)
        self.deck_namebutton = Button(deck_window, text = "Enter Your Deck Name", command = self.make_deck2)

        self.deck_namebutton.grid(row = 0, column = 0)
        self.deck_entry.grid(row = 0, column = 1) 
        








