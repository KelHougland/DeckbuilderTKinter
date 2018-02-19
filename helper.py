import card
import deck
import collection


opusiii=["{0:03}".format(i) for i in range(1,155)]
opusii=["{0:03}".format(i) for i in range(1,149)]
opusi=["{0:03}".format(i) for i in range(1,216)]
promo=["{0:03}".format(i) for i in range(1,4)]

# here are some helper functions

def init_index():
    crd_index=open("crd_indx.txt",'r')
    crd_indx={}
    for aline in crd_index:
        val=aline.split()
        val[3]=int(val[3])
        if val[7].isalpha()==False:
            val[7]=int(val[7])
        else:
            val[7]=val[7]
        val[8]=int(val[8])
        crd_indx[val[0]]=card.card(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], '100')
    crd_index.close()
    return crd_indx

def init_collection(coll_file):
    crd_index=open(coll_file,'r')
    crd_indx={}
    for aline in crd_index:
        val=aline.split()
        val[3]=int(val[3])
        if val[7].isalpha()==False:
            val[7]=int(val[7])
        else:
            val[7]=val[7]
        val[8]=int(val[8])
        crd_indx[val[0]]=card.card(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8])
    crd_index.close()
    return crd_indx