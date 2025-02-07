filnavn = "eks1.txt" # 140
filnavn = "eks2.txt" # 1930
filnavn = "input.txt"

kart:list[list[int]] = []

# Skriver noen kode flere ganger, trenger egt bedre måter å arbeide med kart på.
with open(filnavn) as fil:
    y = -1
    for linje in fil:
        y+=1
        rad = []
        x=-1
        for i in linje.strip():
            x+=1
            rad.append(i)
        kart.append(rad)
høyde = y
lengde = x

def innenforKart(x,y):
    return  not( min(x,y) < 0 or y > høyde or x > lengde)

def printKart(kart):
    print("    ",end="")
    for i in list(range(len(kart[0]))):
        print(f"{i:^3}" ,end="")
    print()
    print()
    
    for i,linje in enumerate(kart):
        print(i," ", end="")
        for j in linje:
            print(f"{j:>3}",end="")
        print()

retninger = [(1,0),(-1,0),(0,1),(0,-1)]

def likeNaboer(x:int,y:int)->int:
    # if not innenforKart(x,y):
    #     return -1 #??
    ant = 0
    val = kart[y][x]
    for i in retninger:
        
        y_0,x_0 = y+i[0], x+i[1]
        if innenforKart(x_0,y_0) and kart[y_0][x_0]==val:
            ant+=1 # Dette kan nok løses bedre med en liste itterasjon?
    return ant

def finnNaboer(kart):
    naboer=[]
    for i in range(len(kart)):
        temp = []
        for j in range(len(kart[0])):
            temp.append(likeNaboer(j,i))
        naboer.append(temp)
    return naboer


naboer = finnNaboer(kart)

retninger = [(1,0),(-1,0),(0,1),(0,-1)]
def sjekkNaboer(liste,sjekket,y,x,target,curr)->list:
    # printKart(sjekket)
    
    for ret in retninger:
        y_0,x_0 = y+ret[0], x+ret[1]
        if not innenforKart(x_0,y_0):
           
            continue

        if sjekket[y_0][x_0]:

            continue

        if liste[y_0][x_0] == target:

            sjekket[y_0][x_0] = True
            curr.append((y_0,x_0))
            sjekkNaboer(liste,sjekket,y_0,x_0,target,curr)
    return curr
        

# For å finne grupper : flood fill? eller hva nå den heter
def finnGrupper(liste):
    sjekket = [[False for j in range(len(liste[0]))]  for i in range(len(liste))]
    grupper = []
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            if not sjekket[i][j]:
                sjekket[i][j]=True
                grupper.append(sjekkNaboer(kart,sjekket,i,j,kart[i][j],[(i,j)]))
    return grupper


def prisGruppe(gruppe:list[tuple]):
    areal = len(gruppe)
    omkrets = 0
    for koord in gruppe:
        i,j = koord
        omkrets+= 4-naboer[i][j]
    return areal * omkrets


res = 0
for gruppe in finnGrupper(kart):
    res += prisGruppe(gruppe)
print(res)