
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


def fiksSide(side):
    # prøver en rekursiv løsning som bytter to og to tall med hverandre om den bryter en regel
    # Må da sjekke hele listen på nytt ... 
    # Er det en bedre måte? F.eks Å bygge opp en løsning, ved å finne tallet med minst regler, sett det bakerst. Osv? 
    # Alternativt, finn det tallet med flest regler og sett det fremst. 
    # Reduserer reglene til kun de som er relevante for denne siden.
    relevanteRegler={}
    for tall in side:
        if tall in regler:
            for verdi in regler[tall]:
                if verdi in side:
                    if tall in relevanteRegler:
                        relevanteRegler[tall].append(verdi)
                    else:
                        relevanteRegler[tall] = [verdi]
    # print(relevanteRegler)
    
    # Da kan jeg ta alle som er tomme bakerst. og fjerne disse fra de andres regler:
    ny_side = []
    while side:
        fjerne_regeler=[]
        fjerne_tall=[]
        for tall in side:
            if tall not in relevanteRegler:
                ny_side.append(tall)
                fjerne_tall.append(tall)
                for verdi,liste in relevanteRegler.items():
                    if tall in liste:
                        liste.remove(tall)
                        if not liste:
                            fjerne_regeler.append(verdi)
        for nøkkel in fjerne_regeler:
            relevanteRegler.pop(nøkkel)       
        for tall in fjerne_tall:
            side.remove(tall)     

        # print(side)
        # print(ny_side)
        # print(relevanteRegler)
    ny_side.reverse() # unødvendig skal ha midten uansett
    # print(ny_side)
    return midten(ny_side)
fiksSide(sider[-1])
# print(sjekkSide(sider[1]))
for side in sider:
    if not sjekkSide(side):
        løsning += int(fiksSide(side))
        
    
print(løsning)
            
            
