class collection:

    def __init__(self,own_name):
        self.name=own_name
        self.total=0
        self.coll_list=[]
        filename="{0}.txt".format(self.name)
        self.coll_file=open(filename,'w+')        

    def add_card(self,acard):
        self.total+=1
        if acard.amt==0:
            self.coll_list.append(acard)
        acard.amt+=1
        if "Foil"==True:
            acard.foil+=1
        
    def rm_card(self,acard):
        self.total-=1
        acard.amt-=1
        if "Foil"==True:
            acard.foil-=1
        if acard.amt==0:
            self.coll_list.remove(acard)    

    def sv_collection(self):
        for i in self.coll_list:
            wrtline=str(i) + " " + str(i.showname) + " " + str(i.amt) +" " +str(i.foil)
            self.coll_file.write(wrtline + '\n')
        self.coll_file.close()

