
# Import the files I need to use
from tkinter import *
from PIL import Image, ImageTk
from random import randrange
# These generate the card numbers for the three releases thus far

opusiii=["{0:03}".format(i) for i in range(1,155)]
opusii=["{0:03}".format(i) for i in range(1,149)]
opusi=["{0:03}".format(i) for i in range(1,216)]
promo=["{0:03}".format(i) for i in range(1,4)]

# here are some helper functions

def init_index():
    crd_index=open("crd_indx.txt",'r')
    global crd_indx
    crd_indx={}
    for aline in crd_index:
        val=aline.split()
        val[3]=int(val[3])
        if val[7].isalpha()==False:
            val[7]=int(val[7])
        else:
            val[7]=val[7]
        val[8]=int(val[8])
        crd_indx[val[0]]=card(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8])
    crd_index.close()


# this is the code for resizing images, it will come in handy for making buttons for the deck
#img = Image.open("flower.png")
#img = img.resize((34, 26), Image.ANTIALIAS)

## make a dropdown seleciton bars that limit the cards shown



class deck_window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        # specify the window size


        self.deck_name=StringVar() # initialize the string variable for user input
        self.deck_name.set("Deck Name Here")
        self.deck_entry=Entry(self.master,textvariable=self.deck_name) # (place for input, where it is stored)

        self.deck_namebutton=Button(self.master,text="Enter Your Deck Name",command=self.make_deck)


        self.deck_namebutton.pack()
        self.deck_entry.pack() # places the entry on the window at a grid loc

        # self.deck_namebutton.grid(row=0,column=0)
        # self.deck_entry.grid(row=1,column=0) # places the entry on the window at a grid loc

    def init_window(self):
        self.master.title("Make a New Deck") # this is where I name the windows I want to make
        self.master.configure(background='black')


    def make_deck(self):
        self.new_deck=deck(self.deck_name.get())
        self.deck_namebutton.pack_forget()
        self.deck_entry.pack_forget()
        self.refresh_cards(crd_indx)

    def refresh_cards(self,indx):
        self.use_indx=crd_indx
        self.buttons4cards={}
        for i in range(len(self.use_indx)):
            self.buttons4cards[i] = Button(self.master,text=self.use_indx[list(self.use_indx.keys())[i]].showname,command=self.use_indx[list(self.use_indx.keys())[i]].image_window)
            self.buttons4cards[i].pack


    # def refresh_cards(self,indx):
    #     self.use_indx=crd_indx
    #     self.buttons4cards={}
    #     for i in range(len(self.use_indx)):
    #         ref=self.use_indx[list(self.use_indx.keys())[i]]
    #         self.buttons4cards[ref]=self.use_indx[ref].make_button(self.master)
    #         self.buttons4cards[ref].grid(row=i//4*2,column=i%4*2)



        # for i in range(len(self.use_indx)):
        #     self.buttons4cards[i] = Button(self.master,text=self.use_indx[list(self.use_indx.keys())[i]].showname)
        #     #self.buttons4cards[i].configure(image=self.imgs4indx[i])
        #     self.buttons4cards[i].grid(row=i//4,column=i%4)





##### button function in card class
##### load whole index of buttons, but only grid those buttons that match search criteria
##### add drop down menues for search


# The card class gives and generates information, it needs element, crystal cost, name, number, role, type, job, power if necessesary

class card:

    def __init__(self,crd_code,crd_name,crd_element,crd_cost,crd_role,crd_type,crd_job,crd_power,crd_total):
        self.code=crd_code
        self.img=Image.open("C:/Users/knhou/Google Drive/Python Projects/deckbuilder/images/{0}.png".format(self.code))
        self.name=crd_name
        self.element=crd_element
        self.cost=crd_cost
        self.role=crd_role
        self.type=crd_type
        self.job=crd_job
        self.power=crd_power
        self.amt=int(crd_total)
        self.foil=0
        self.showname=''
        for i in self.name:
            if i=="_":
                self.showname+=" "
            else:
                self.showname+=i
        self.numindeck=0


    def add_card(self):
        self.amt+=1

    def trade_card(self):
        if self.amt>0:
            self.amt-=1

    def image_window(self):

        twig=Tk()
        twig.geometry("480x668")
        twig.title(self.showname)
        testref=self.img
        self.photo=ImageTk.PhotoImage(testref)
        label=Label(twig,image=self.photo)
        label.grid(row=0,column=0)

        twig.mainloop()

    def make_button(self,wind):
        a=Button(wind,text=self.showname,command=image_window())
        return a






# Deck class is the actual deck that people build, dream decks can be built from index, normal decks from collection

class deck:

    def __init__(self,init_name):
        self.name=init_name
        self.available=50
        self.deck_lst=[]


    def add_card(self,acard):
        if self.available>0 and acard.numindeck<4:
            self.available-=1
            acard.numindeck+=1
            self.deck_list.append(acard)

    def rm_card(self,acard):
        if acard.numindeck>0:
            self.available+=1
            acard.numindeck-=1


    def sv_deck(self):
        filename="{0}.txt".format(self.name)
        self.deck_file=open(filename,'w+')
        for i in self.deck_list:
            wrtline=str(i) + " " + str(i.showname)
            self.deck_file.write(wrtline + '\n')
        self.deck_file.close()




# collection is the index of cards that the player owns

class collection:

    def __init__(self,own_name):
        self.name=own_name
        self.total=0

    def add_card(self,acard):
        self.total+=1
        acard.amt+=1
        if "Foil"==True:
            acard.foil+=1

    def sv_collection(self):
        filename="{0}.txt".format(self.name)
        self.coll_file=open(filename,'w+')
        for i in self.deck_list:
            wrtline=str(i) + " " + str(i.showname) + " " + str(i.amt) +" " +str(i.foil)
            self.deck_file.write(wrtline + '\n')
        self.deck_file.close()





# this here's the code that makes the buttons work
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window() # put basic stuff here to prevent clutter, also () means do this now
        # self.background=Image.open('C:/Users/knhou/Google Drive/Python Projects/deckbuilder/bckgnd.jpg')
        # render=ImageTk.PhotoImage(self.background)
        # img=Label(self,image=render)
        # img.image=render
        # img.place(x=0,y=0, relwidth=1, relheight=1)

        # next we initialize the menu to use for making the things
        menuvar=Menu(self.master) #Menu is tkinter, menu is variable
        self.master.config(menu=menuvar) # this and above define the menu
        options=Menu(menuvar) # this creates a menu variable
        options.add_command(label='Load Index for Use',command=init_index)
        #options.add_command(label="Load Collection for Use",command=init_collection)
        options.add_command(label='Exit',command=self.client_exit) # adds an exit button to the menue
        menuvar.add_cascade(label="Options",menu=options) # adds the cascading menu to the window

        deck_menu=Menu(menuvar) # this adds a deck thing to the main menue
        deck_menu.add_command(label="Load an Existing Deck")
        deck_menu.add_command(label="Make a New Deck",command=self.newdeck) # this defines what the button does
        menuvar.add_cascade(label="Decks",menu=deck_menu)# adds the cascading menu to the window

        coll_menu=Menu(menuvar) # this adds the collection menu
        coll_menu.add_command(label="Start a New Collection")
        coll_menu.add_command(label="Load an Existing Collection")
        menuvar.add_cascade(label="Collections",menu=coll_menu)

        testpic=Image.open('C:/Users/knhou/Google Drive/Python Projects/deckbuilder/bckgnd.jpg')
        render=ImageTk.PhotoImage(testpic)
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0,relwidth=1, relheight=1)


    def newdeck(self):
        branch=Tk()

        branch.geometry("1200x800")

        newwindow=deck_window(branch)
        branch.mainloop()



        # toy_menu=Menu(menuvar) # this adds the collection menu
        # toy_menu.add_command(label="Show Image",command=self.showImg)
        # toy_menu.add_command(label="Show Text",command=self.showTxt)
        # menuvar.add_cascade(label="Toy",menu=toy_menu)

    # def showImg(self):
    #     testpic=Image.open('C:/Users/knhou/Google Drive/Python Projects/deckbuilder/bckgnd.jpg')
    #     render=ImageTk.PhotoImage(testpic)
    #     img=Label(self,image=render)
    #     img.image=render
    #     img.place(x=0,y=0,relwidth=1, relheight=1)

    # def showTxt(self):
    #     text=Label(self,text="Hey there good looking")
    #     text.pack()


    def init_window(self):
        self.master.title("FFTCG DeckBuilder and Collection Archive") # this is where I name the windows I want to make
        self.pack(fill=BOTH,expand=1)


        #quitButton=Button(self, text="Quit",command=self.client_exit)
        #quitButton.place(x=0,y=0)

    def client_exit(self):
        self.master.destroy() # window.destroy () closes the window named

def main():
    root = Tk() # imports root from tkinter
    root.geometry("480x360")

    # specify the window size
# background=Image.open('C:/Users/knhou/Google Drive/Python Projects/deckbuilder/bckgnd.jpg')
# render=ImageTk.PhotoImage(background)
# img=Label(root,image=render)
# img.image=render
# img.place(x=0,y=0, relwidth=1, relheight=1)

    app = Window(root) # makes a new window class for a specific application
    root.mainloop() # makes the window

if __name__=="__main__":
    main()
