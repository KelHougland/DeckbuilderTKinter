
# Import the files I need to use
from tkinter import *
from PIL import Image, ImageTk
from random import randrange






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






# def main():


# if __name__=="__main__":
#     main()
