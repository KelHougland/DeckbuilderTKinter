
class deck:

    def __init__(self,init_name):
        self.name=init_name
        self.available=50
        self.deck_list=[]
        filename="{0}.txt".format(self.name)
        self.deck_file=open(filename,'w+')


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
        for i in self.deck_list:
            wrtline=str(i) + " " + str(i.showname)
            self.deck_file.write(wrtline + '\n')
        self.deck_file.close()


