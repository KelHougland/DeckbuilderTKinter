from tkinter import *
import deck




class card:

    def __init__(self,crd_code,crd_name,crd_element,crd_cost,crd_role,crd_type,crd_job,crd_power,crd_total):
        self.code=crd_code
        self.img=PhotoImage("C:/Users/knhou/Google Drive/Python Projects/deckbuilder/images/{0}.gif".format(self.code))
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

    def rm_card(self):
        if self.amt>0:
            self.amt-=1


