
filnavn = "eks1.txt"
filnavn = "input.txt"

with open(filnavn) as fil:
    regler = {}
    sider = []
    reg = True
    for linje in fil:
        linje=linje.strip()
        if linje =="":
            reg = False
            continue
        if reg:
            x,y = linje.split("|")
            if x in regler:
                # print("legger til ",x, " finnes fra før")
                regler[x].append(y)
                # print(regler)
            else:
                # print("legger til ",x," - ",y, " fantes ikke fra før")
                regler[x]=[y]
                # print(regler)
        else:
            sider.append(linje.split(","))

# print(regler)
# print(sider)

def sjekkSide(side):
    # print(side)
    # print(regler)
    passert=[]
    for tall in side: 
        if tall in regler: # om det er et tall med regler:
            if any([tidligere in regler[tall] for tidligere in passert]):
                return False
            # for tidligere in passert:
            #     if tidligere in regler[tall]:
            #         return False
        else:
            # print(tall," Har ingen regler")
            pass
        passert.append(tall)
    return True
løsning = 0
def midten(liste):
    return liste[len(liste)//2]
# print(sjekkSide(sider[1]))
for side in sider:
    test = sjekkSide(side)
    if test:
        # print(midten(side))
        løsning += int(midten(side))
    else:
        # print(side)
        pass
    
print(løsning)
            
            
