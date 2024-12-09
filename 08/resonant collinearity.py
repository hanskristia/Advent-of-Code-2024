filnavn = "eks1.txt"
filnavn = "input.txt"

with open(filnavn) as fil:

    kart = []
    antenner = {}
    y = 0
    for linje in fil:
        
        rad =  []
        x=0
        for i in linje.strip():
            rad.append(i)
            if i != ".":
                if i == "#":
                    rad[-1]="#" # For enklere testing av eksempler som inneholder fasit
                elif i in antenner:
                    antenner[i].append((y,x))
                else:
                    antenner[i]=[(y,x)]
            x+=1
        kart.append(rad)
        y+=1
lengde = x
høyde = y

def antinoder(a:tuple[int],b:tuple[int]):
    diffs = (a[0]-b[0], a[1]-b[1])
    # print(f"a{a},b{b}, delta:{diffs}")

    a_n=(a[0]+diffs[0] , a[1]+diffs[1])
    b_n=(b[0]-diffs[0] , b[1]-diffs[1])
    # print(lovligNode(a))
    # print(lovligNode(b))
    for node in (a_n,b_n):
        # if node[0]==0:
        # print(f"{node} fra - a{a},b{b}, delta:{diffs}")
        # print(antenner)
        if lovligNode(node):
            # print(node)
            # if kart[node[0]][node[1]]==".":
            kart[node[0]][node[1]]="#"
    # Må sjekke a - dif og b + dif

def printKart(kart):
    print("    ",end="")
    for i in list(range(len(kart[0]))):
        print(f"{i:^5}" ,end="")
    print()
    for i,linje in enumerate(kart):
        print(i," ", linje)

def lovligNode(a:tuple):
    return not (min(a)<0 or a[0] >= høyde or a[1] >= lengde)

# antinoder((1,2),(3,3)) # -> antinoder 5,4 og -1,1.
printKart(kart)

# Denne endrer kartet
for i,j in antenner.items():
    antall = len(j)
    for a in range(antall):
        for b in range(a+1,antall):
            antinoder(j[a],j[b])

printKart(kart)
løsning = sum([i.count("#") for i in kart])
print(løsning)