filnavn = "eks1.txt"
# filnavn = "input.txt"

with open(filnavn) as fil:

    kart:list[list[str,list]] = []
    
    for linje in fil:
        rad = []
        if "^" in linje:
            start_x = linje.find("^") 
            start_y = len(kart)
        for bokstav in linje.strip():
            rad.append([bokstav,[]])
        kart.append(rad)    
    lengde = len(kart[0])-1
    høyde = len(kart)-1
def printKart(kart):
    print("    ",end="")
    for i in list(range(len(kart[0]))):
        print(f"{i:^5}" ,end="")
    print()
    for i,linje in enumerate(kart):
        linje=str([i[0] for i in linje])
        print(i," ", linje)

printKart(kart)
print(f"x:{start_x},y:{start_y}")

def påKartet(x,y):
    utenfor = min(x,y)<0 or x > lengde or y>høyde  
    # print(x,y, utenfor)
    return not utenfor
# Opp, Høyre, Ned, Venstre
retninger = [(-1,0),(0,1),(1,0),(0,-1)]
visninger = ["^",">","v","<"]
vei=["|","-"]
i=0
x,y= start_x,start_y
forrige="."    
while True:
# for _ in range(10):
    endring_y,endring_x = retninger[i]
    neste_x = x + endring_x
    neste_y = y + endring_y 
    if påKartet(neste_x,neste_y):
        if kart[neste_y][neste_x][0]=="#":
            # Snur retning:
            # print("snur")
            i= (i+1)%4
            print(f"i:{i}, x {x}, y {y}")
            printKart(kart)

            kart[y][x][0] = "+"
            kart[y][x][1].append(visninger[i])

            forrige = "snudde"
        else:
            # Går videre
            if forrige == ".":
                kart[y][x][0] = vei[i%2]
            elif forrige == vei[(i+1)%2]:
                print(kart[y][x][1])
                print(visninger)
                print(visninger[i])
                print(f"i:{i}, x {x}, y {y}, forrige: {forrige}")
                kart[y][x][0] = "+"
                
                # Må sjekke om kan bli loop?
            else:
                print(f"i:{i}, x {x}, y {y}, forrige: {forrige}")
            kart[y][x][1].append(visninger[i])

            x,y = neste_x,neste_y
            forrige = kart[y][x][0]
            kart[y][x][0]= visninger[i]
    else:
        kart[y][x][0] = vei[i%2]
        break

printKart(kart)
for y,linje in enumerate(kart):
    for x, verdi in enumerate(linje):
        for vei in verdi[1]:
            neste_indeks =  (visninger.index(vei)+1)%4
            neste = visninger[neste_indeks]
            if neste in verdi[1]:
                print( x, y, verdi[1])
                print(" En mulig løsning!")
# om vi har to følgende retninger i den andre listen kan vi lage en loop
        
ruter = 0
for linje in kart:
    ruter+= linje.count("+")
print(ruter)
