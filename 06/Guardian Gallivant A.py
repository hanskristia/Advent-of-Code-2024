filnavn = "eks1.txt"
filnavn = "input.txt"

with open(filnavn) as fil:

    kart:list[list] = []
    
    for linje in fil:
        rad = []
        if "^" in linje:
            start_x = linje.find("^") 
            start_y = len(kart)
        for bokstav in linje.strip():
            rad.append(bokstav)
        kart.append(rad)    
    lengde = len(kart[0])-1
    høyde = len(kart)-1
def printKart(kart):
    print("    ",end="")
    for i in list(range(len(kart[0]))):
        print(f"{i:^5}" ,end="")
    print()
    for i,linje in enumerate(kart):
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
i=0
x,y= start_x,start_y
    
while True:
# for _ in range(10):
    endring_y,endring_x = retninger[i]
    neste_x = x + endring_x
    neste_y = y + endring_y 
    if påKartet(neste_x,neste_y):
        if kart[neste_y][neste_x]=="#":
            # Snur retning:
            # print("snur")
            i= (i+1)%4
            # print(f"i:{i}, x {x}, y {y}")
            # printKart(kart)
        else:
            # Går videre
            kart[y][x] ="X"
            x,y = neste_x,neste_y
            kart[y][x]= visninger[i]
    else:
        kart[y][x] ="X"
        break

# printKart(kart)

ruter = 0
for linje in kart:
    ruter+= linje.count("X")
print(ruter)
